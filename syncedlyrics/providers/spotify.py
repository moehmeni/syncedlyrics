"""Spotify provider (the API is powered by Musixmatch)"""

from typing import Optional
from .base import LRCProvider

class Spotify(LRCProvider):
    """Spotify provider class"""

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_track_id(search_term : str) -> Optional[str]:
        """Returns a Spotify track ID for given `search_term`"""
        # TODO: self.client.search(search_term) and processing the results
        pass

    def get_lrc(search_term: str) -> Optional[str]:
        # TODO: Use https://github.com/akashrchandran/spotify-lyrics-api
        return super().get_lrc()
