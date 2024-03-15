"""Utility functions for `syncedlyrics` package"""

from bs4 import BeautifulSoup, FeatureNotFound
import rapidfuzz
from typing import Union, Callable, Optional
import datetime
import re

R_FEAT = re.compile(r"\((feat.+)\)", re.IGNORECASE)


def is_lrc_valid(lrc: str, allow_plain_format: bool = False) -> bool:
    """Checks whether a given LRC string is valid or not."""
    if not lrc:
        return False
    if not allow_plain_format:
        conds = ["[" in l for l in lrc.split("\n")[5:8]]
        return all(conds)

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


def format_time(time_in_seconds: float):
    """Returns a [mm:ss.xx] formatted string from the given time in seconds."""
    time = datetime.timedelta(seconds=time_in_seconds)
    minutes, seconds = divmod(time.seconds, 60)
    return f"{minutes:02}:{seconds:02}.{time.microseconds//10000:02}"


def str_score(a: str, b: str) -> float:
    """Returns the similarity score of the two strings"""
    # if user does not specify any "feat" in the search term,
    # remove the "feat" from the search results' names
    a, b = a.lower(), b.lower()
    if "feat" not in b:
        a, b = R_FEAT.sub("", a), R_FEAT.sub("", b)
    return rapidfuzz.fuzz.token_set_ratio(a, b)


def str_same(a: str, b: str, n: int) -> bool:
    """Returns `True` if the similarity score of the two strings is greater than `n`"""
    return round(str_score(a, b)) >= n


def sort_results(
    results: list,
    search_term: str,
    compare_key: Union[str, Callable[[dict], str]] = "name",
) -> list:
    """
    Sorts the API results based on the similarity score of the `compare_key` with
    the `search_term`.

    ## Parameters
    - `results`: The API results
    - `search_term`: The search term
    - `compare_key`: The key to compare the `search_term` with. Can be a string or a
    function that takes a track and returns a string.
    """
    if isinstance(compare_key, str):
        compare_key = lambda t: t[compare_key]
    sort_key = lambda t: str_score(compare_key(t), search_term)
    return sorted(results, key=sort_key, reverse=True)


def get_best_match(
    results: list,
    search_term: str,
    compare_key: Union[str, Callable[[dict], str]] = "name",
    min_score: int = 65,
) -> Optional[dict]:
    """
    Returns the best match from the API results based on the similarity score of the `compare_key`
    with the `search_term`.
    """
    if not results:
        return None
    results = sort_results(results, search_term, compare_key=compare_key)
    best_match = results[0]

    value_to_compare = (
        best_match[compare_key]
        if isinstance(compare_key, str)
        else compare_key(best_match)
    )
    if not str_same(value_to_compare, search_term, n=min_score):
        return None
    return best_match
