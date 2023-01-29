"""Utility functions for `syncedlyrics` package"""

from bs4 import BeautifulSoup, FeatureNotFound


def is_lrc_valid(lrc: str, allow_plain_format: bool = False) -> bool:
    """Checks whether a given LRC string is valid or not."""
    if not lrc:
        return False
    if not allow_plain_format:
        if not ("[" in lrc and "]" in lrc):
            return False

    return True


def save_lrc_file(path: str, lrc_text: str):
    """Saves the `.lrc` file"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(lrc_text)


def generate_bs4_soup(session, url: str, **kwargs):
    """Returns a `BeautifulSoup` from the given `url`.
    Tries to use `lxml` as the parser if available, otherwise `html.parser`
    """
    r = session.get(url)
    try:
        soup = BeautifulSoup(r.text, features="lxml", **kwargs)
    except FeatureNotFound:
        soup = BeautifulSoup(r.text, features="html.parser", **kwargs)
    return soup
