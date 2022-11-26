import requests
from typing import Optional


class LRCProvider:
    """
    Base class for all of the synced (LRC format) lyrics providers.
    """

    session = requests.Session()

    def __init__(self) -> None:
        pass

    def get_lrc(search_term: str) -> Optional[str]:
        """
        Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.
        """
        raise NotImplementedError
