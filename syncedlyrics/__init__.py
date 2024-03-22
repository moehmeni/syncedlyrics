"""
Search for an LRC format (synchronized lyrics) of a music.

```py
import syncedlyrics
lrc_text = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")
```
"""

import logging
from typing import List, Optional

from .providers import Deezer, Lrclib, Musixmatch, NetEase, Genius
from .utils import is_lrc_valid, save_lrc_file

logger = logging.getLogger(__name__)


def search(
    search_term: str,
    allow_plain_format: bool = False,
    save_path: Optional[str] = None,
    providers: Optional[List[str]] = None,
    lang: Optional[str] = None,
    enhanced: bool = False,
) -> Optional[str]:
    """
    Returns the synced lyrics of the song in [LRC](https://en.wikipedia.org/wiki/LRC_(file_format)) format if found.
    ### Arguments
    - `search_term`: The search term to find the track
    - `allow_normal_format`: Return a plain text (not synced) lyrics if not LRC was found
    - `save_path`: Path to save `.lrc` lyrics. No saving if `None`
    - `providers`: A list of provider names to include in searching; loops over all the providers as soon as an LRC is found
    - `lang`: Language of the translation along with the lyrics. **Only supported by Musixmatch**
    - `enhanced`: Returns word by word synced lyrics if available. **Only supported by Musixmatch**
    """
    _providers = [
        Musixmatch(lang=lang, enhanced=enhanced),
        Lrclib(),
        Deezer(),
        NetEase(),
        Genius(),
    ]
    if providers and any(providers):
        # Filtering the providers
        _providers = [
            p
            for p in _providers
            if p.__class__.__name__.lower() in [p.lower() for p in providers]
        ]
    if not _providers:
        logger.error(
            f"Providers {providers} not found in the list of available providers."
        )
        return None
    lrc = None
    for provider in _providers:
        logger.debug(f"Looking for an LRC on {provider.__class__.__name__}")
        _l = provider.get_lrc(search_term)
        if enhanced and not _l:
            # Since enhanced is only supported by Musixmatch, break if no LRC is found
            break
        if is_lrc_valid(_l, allow_plain_format):
            logger.info(
                f'synced-lyrics found for "{search_term}" on {provider.__class__.__name__}'
            )
            lrc = _l
            break
        else:
            logger.debug(
                f"Skip {provider.__class__.__name__} as the synced-lyrics is not valid. (allow_plain_format={allow_plain_format})"
            )
            logger.debug(f"Lyrics: {_l}")
    if not lrc:
        logger.info(f'No synced-lyrics found for "{search_term}" :(')
        return None
    if save_path:
        save_path = save_path.format(search_term=search_term)
        save_lrc_file(save_path, lrc)
    return lrc
