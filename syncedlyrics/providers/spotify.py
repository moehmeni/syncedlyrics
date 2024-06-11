"""Spotify LRC provider (the API is powered by Musixmatch)"""

from typing import Optional
from .base import LRCProvider
from ..utils import Lyrics


class Spotify(LRCProvider):
    """Spotify provider class"""

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_track_id(cls, search_term: str) -> Optional[str]:
        """Returns a Spotify track ID for given `search_term`"""
        # TODO: self.client.search(search_term) and processing the results
        raise NotImplementedError

    def get_lrc_by_id(self, track_id: str) -> Optional[Lyrics]:
        # TODO:
        raise NotImplementedError

    def get_lrc(self, search_term: str) -> Optional[Lyrics]:
        # TODO: Use https://github.com/akashrchandran/spotify-lyrics-api
        # Note: as of recently, only premium users can get lyrics from spotify, so this would require an account access token.
        raise NotImplementedError
