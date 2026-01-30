"""NetEase (music.163.com) china-based provider"""

from typing import Optional
from .base import LRCProvider
from ..utils import Lyrics, get_best_match


class NetEase(LRCProvider):
    """NetEase provider class"""

    ROOT_URL = "https://music.163.com"
    API_ENDPOINT_METADATA = "https://music.163.com/api/search/pc"
    API_ENDPOINT_LYRICS = "https://music.163.com/api/song/lyric"

    def __init__(self) -> None:
        super().__init__()
        self.session.headers.update(
            {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            }
        )

    def _ensure_cookies(self):
        """Bootstrap cookies from a lightweight homepage hit if none exist."""
        if not self.session.cookies:
            resp = self.session.get(self.ROOT_URL)
            # Use homepage as referer for subsequent API calls
            self.session.headers.update({"referer": resp.url})

    def search_track(self, search_term: str) -> Optional[dict]:
        """Returns a `dict` containing some metadata for the found track."""
        self._ensure_cookies()
        params = {"limit": 10, "type": 1, "offset": 0, "s": search_term}
        response = self.session.get(self.API_ENDPOINT_METADATA, params=params)
        results = response.json().get("result", {}).get("songs")
        if not results:
            return None
        cmp_key = lambda t: f"{t.get('name')} {t.get('artists')[0].get('name')}"
        track = get_best_match(results, search_term, cmp_key)
        # Update the session cookies from the new sent cookies for the next request.
        self.session.cookies.update(response.cookies)
        self.session.headers.update({"referer": response.url})
        return track

    def get_lrc_by_id(self, track_id: str) -> Optional[Lyrics]:
        params = {"id": track_id, "lv": 1}
        response = self.session.get(self.API_ENDPOINT_LYRICS, params=params)
        lrc = Lyrics()
        lrc.add_unknown(response.json().get("lrc", {}).get("lyric"))
        return lrc

    def get_lrc(self, search_term: str) -> Optional[Lyrics]:
        track = self.search_track(search_term)
        if not track:
            return None
        return self.get_lrc_by_id(track["id"])
