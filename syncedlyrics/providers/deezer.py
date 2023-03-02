"""Deezer LRC provider (API powered by LyricFind)"""

from typing import Optional
from .base import LRCProvider

# Currently broken
# TODO: Fix invalid CSRF token

# Mostly based on https://gist.github.com/akashrchandran/95915c2081815397c454bd8aa4a118b5


class Deezer(LRCProvider):
    """Deezer provider class"""

    SEARCH_ENDPOINT = "https://api.deezer.com/search?q="
    API_ENDPOINT = "http://www.deezer.com/ajax/gw-light.php"
    token = "null"

    def __init__(self) -> None:
        super().__init__()
        self.token = self._api_call("deezer.getUserData")["results"]["checkForm"]

    def _api_call(self, method: str, json=None) -> dict:
        params = {
            "api_version": "1.0",
            "api_token": self.token,
            "input": "3",
            "method": method,
        }
        response = self.session.post(self.API_ENDPOINT, params=params, json=json)
        return response.json()

    def get_lrc_by_id(self, track_id: str) -> Optional[str]:
        lrc_response = self._api_call("song.getLyrics", json={"sng_id": track_id})
        lrc_json_objs = lrc_response["results"].get("LYRICS_SYNC_JSON")
        if not lrc_json_objs:
            # Returning the plain text lyrics
            return lrc_response["results"].get("LYRICS_TEXT")
        lrc = ""
        for chunk in lrc_json_objs:
            if chunk.get("lrc_timestamp") and chunk.get("line"):
                lrc += f"{chunk['lrc_timestamp']} {chunk['line']}\n"
        return lrc or None

    def get_lrc(self, search_term: str) -> Optional[str]:
        search_results = self.session.get(self.SEARCH_ENDPOINT + search_term).json()
        if not search_results.get("data"):
            return
        song = search_results.get("data")[0]
        return self.get_lrc_by_id(song["id"])
