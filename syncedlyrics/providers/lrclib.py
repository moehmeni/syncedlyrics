"""Lrclib (lrclib.net) LRC provider"""

from typing import Optional
from .base import LRCProvider


class Lrclib(LRCProvider):
    """Lrclib LRC provider class"""

    ROOT_URL = "https://lrclib.net"
    API_ENDPOINT = ROOT_URL + "/api"
    SEARCH_ENDPOINT = API_ENDPOINT + "/search"
    LRC_ENDPOINT = API_ENDPOINT + "/get/"

    def __init__(self) -> None:
        super().__init__()

    def get_lrc_by_id(self, track_id: str) -> Optional[str]:
        url = self.LRC_ENDPOINT + track_id
        r = self.session.get(url)
        if not r.ok:
            return
        track = r.json()
        return track.get("syncedLyrics", track.get("plainLyrics"))

    def get_lrc(self, search_term: str) -> Optional[str]:
        url = self.SEARCH_ENDPOINT
        r = self.session.get(url, params={"q": search_term})
        if not r.ok:
            return
        tracks = r.json()
        if not tracks:
            return
        _id = str(tracks[0]["id"])
        return self.get_lrc_by_id(_id)
