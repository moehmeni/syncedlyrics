"""Lrclib (lrclib.net) LRC provider"""

from typing import Optional
from .base import LRCProvider
from ..utils import Lyrics, sort_results


class Lrclib(LRCProvider):
    """Lrclib LRC provider class"""

    ROOT_URL = "https://lrclib.net"
    API_ENDPOINT = ROOT_URL + "/api"
    SEARCH_ENDPOINT = API_ENDPOINT + "/search"
    LRC_ENDPOINT = API_ENDPOINT + "/get/"

    def __init__(self) -> None:
        super().__init__()

    def get_lrc_by_id(self, track_id: str) -> Optional[Lyrics]:
        url = self.LRC_ENDPOINT + track_id
        r = self.session.get(url)
        if not r.ok:
            return None
        track = r.json()
        lrc = Lyrics()
        lrc.synced = track.get("syncedLyrics")
        lrc.unsynced = track.get("plainLyrics")
        return lrc

    def get_lrc(self, search_term: str) -> Optional[Lyrics]:
        url = self.SEARCH_ENDPOINT
        r = self.session.get(url, params={"q": search_term})
        if not r.ok:
            return None
        tracks = r.json()
        if not tracks:
            return None
        tracks = sort_results(
            tracks, search_term, lambda t: f'{t["artistName"]} - {t["trackName"]}'
        )
        _id = str(tracks[0]["id"])
        # Getting the first track that its `syncedLyrics` is not empty
        # _id = None
        # for track in tracks:
        #     if (track.get("syncedLyrics", "") or "").strip():
        #         _id = str(track["id"])
        #         break
        # if not _id:
        #     return None
        return self.get_lrc_by_id(_id)
