"""
Search for an LRC format (synchronized lyrics) of a music.

```py
import syncedlyrics
lrc_text = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")
```
"""

from typing import Optional
import logging
from .providers import NetEase, Deezer
from .utils import is_lrc_valid, save_lrc_file


def search(
    search_term: str, allow_plain_format: bool = False, save_path: str = None
) -> Optional[str]:
    """
    Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.
    ### Arguments
    - `search_term` str: The search term to find the track.
    - `allow_normal_format` bool: Return a plain text (not synced) lyrics if not LRC was found.
    - `save_path` str: Path to save `.lrc` lyrics. No saving if `None`.
    """
    for provider in [
        Deezer(),
        NetEase(),
    ]:
        lrc = provider.get_lrc(search_term)
        if is_lrc_valid(lrc, allow_plain_format):
            break
    if not lrc:
        logging.info(f'No synced-lyrics found for "{search_term}" :(')
    if save_path:
        save_path = save_path.format(search_term=search_term)
        save_lrc_file(save_path, lrc)
    return lrc
