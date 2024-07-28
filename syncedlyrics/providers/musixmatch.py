"""Musixmatch LRC provider"""

from typing import Optional, List
import time
import json
import os
from .base import LRCProvider
from ..utils import Lyrics, get_best_match, format_time, get_cache_path

# Inspired from https://github.com/Marekkon5/onetagger/blob/0654131188c4df2b4b171ded7cdb927a4369746e/crates/onetagger-platforms/src/musixmatch.rs
# Huge part converted from Rust to Py by ChatGPT :)
# Whyyyy did you convert it from a good language to a bad one? :P


class Musixmatch(LRCProvider):
    """Musixmatch provider class"""

    ROOT_URL = "https://apic-desktop.musixmatch.com/ws/1.1/"

    def __init__(self, lang: Optional[str] = None, enhanced: bool = False) -> None:
        super().__init__()
        self.lang = lang
        self.enhanced = enhanced
        self.token = None

    def _get(self, action: str, query: List[tuple]):
        if action != "token.get" and self.token is None:
            self._get_token()
        query.append(("app_id", "web-desktop-app-v1.0"))
        if self.token is not None:
            query.append(("usertoken", self.token))
        t = str(int(time.time() * 1000))
        query.append(("t", t))
        url = self.ROOT_URL + action
        response = self.session.get(url, params=query)
        return response

    def _get_token(self):
        token_path = get_cache_path("syncedlyrics", False) / "musixmatch_token.json"
        current_time = int(time.time())
        if token_path.exists():
            with open(token_path, "r") as token_file:
                cached_token_data = json.load(token_file)
            cached_token = cached_token_data.get("token")
            expiration_time = cached_token_data.get("expiration_time")
            if cached_token and expiration_time and current_time < expiration_time:
                self.token = cached_token
                return
        # Token not cached or expired, fetch a new token
        d = self._get("token.get", [("user_language", "en")]).json()
        if d["message"]["header"]["status_code"] == 401:
            time.sleep(10)
            return self._get_token()
        new_token = d["message"]["body"]["user_token"]
        expiration_time = current_time + 600  # 10 minutes expiration
        # Cache the new token
        self.token = new_token
        token_data = {"token": new_token, "expiration_time": expiration_time}
        token_path.parent.mkdir(parents=True, exist_ok=True)
        with open(token_path, "w") as token_file:
            json.dump(token_data, token_file)

    def get_lrc_by_id(self, track_id: str) -> Optional[Lyrics]:
        r = self._get(
            "track.subtitle.get",
            [("track_id", track_id), ("subtitle_format", "lrc")],
        )
        if self.lang is not None:
            r_tr = self._get(
                "crowd.track.translations.get",
                [
                    ("track_id", track_id),
                    ("subtitle_format", "lrc"),
                    ("translation_fields_set", "minimal"),
                    ("selected_language", self.lang),
                ],
            )
            body_tr = r_tr.json()["message"]["body"]
            if not body_tr["translations_list"]:
                raise Exception("Couldn't find translations")
        if not r.ok:
            return None
        body = r.json()["message"]["body"]
        if not body:
            return None
        lrc_str = body["subtitle"]["subtitle_body"]
        if self.lang is not None:
            for i in body_tr["translations_list"]:
                org, tr = (
                    i["translation"]["subtitle_matched_line"],
                    i["translation"]["description"],
                )
                lrc_str = lrc_str.replace(org, org + "\n" + f"({tr})")
        lrc = Lyrics()
        lrc.synced = lrc_str
        return lrc

    def get_lrc_word_by_word(self, track_id: str) -> Optional[Lyrics]:
        lrc = Lyrics()
        r = self._get("track.richsync.get", [("track_id", track_id)])
        if r.ok and r.json()["message"]["header"]["status_code"] == 200:
            lrc_raw = r.json()["message"]["body"]["richsync"]["richsync_body"]
            lrc_raw = json.loads(lrc_raw)
            lrc_str = ""
            for i in lrc_raw:
                lrc_str += f"[{format_time(i['ts'])}] "
                for l in i["l"]:
                    t = format_time(float(i["ts"]) + float(l["o"]))
                    lrc_str += f"<{t}> {l['c']} "
                lrc_str += "\n"
            lrc.synced = lrc_str
        return lrc

    def get_lrc(self, search_term: str) -> Optional[Lyrics]:
        r = self._get(
            "track.search",
            [
                ("q", search_term),
                ("page_size", "5"),
                ("page", "1"),
            ],
        )
        status_code = r.json()["message"]["header"]["status_code"]
        if status_code != 200:
            self.logger.warning(f"Got status code {status_code} for {search_term}")
            return None
        body = r.json()["message"]["body"]
        if not isinstance(body, dict):
            return None
        tracks = body["track_list"]
        cmp_key = lambda t: f"{t['track']['track_name']} {t['track']['artist_name']}"
        track = get_best_match(tracks, search_term, cmp_key)
        if not track:
            return None
        track_id = track["track"]["track_id"]
        if self.enhanced:
            lrc = self.get_lrc_word_by_word(track_id)
            if lrc and lrc.synced:
                return lrc
        return self.get_lrc_by_id(track_id)
