import requests
from typing import Optional


class LRCProvider:
    """
    Base class for all of the synced (LRC format) lyrics providers.
    """

    session = requests.Session()

    def __init__(self) -> None:
        self.session.headers.update(
            {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            }
        )

    def get_lrc_by_id(self, track_id: str) -> Optional[str]:
        """
        Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.

        ### Arguments
        - track_id: The ID of the track defined in the provider database. e.g. Spotify/Deezer track ID
        """
        raise NotImplementedError

    def get_lrc(self, search_term: str) -> Optional[str]:
        """
        Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.
        """
        raise NotImplementedError
