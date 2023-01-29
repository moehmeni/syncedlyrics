"""Lyricsify (lyricsify.com) LRC provider"""

from typing import Optional
from bs4 import BeautifulSoup, SoupStrainer
from .base import LRCProvider
import rapidfuzz
from ..utils import generate_bs4_soup


class Lyricsify(LRCProvider):
    """Lyricsify LRC provider class"""

    ROOT_URL = "https://www.lyricsify.com"
    SEARCH_ENDPOINT = ROOT_URL + "/search?q="

    def __init__(self) -> None:
        super().__init__()
        self.parser = "html.parser"

    def get_lrc(self, search_term: str) -> Optional[str]:
        search_page_url = self.SEARCH_ENDPOINT + search_term.replace(" ", "+")

        # Just processing the `a` tags whose `href` attribute starts with /lyric/
        # and whose text is similar to the query too. https://github.com/maxbachmann/RapidFuzz#scorers
        _t = lambda s: s.lower().replace("-", "")
        text_match = lambda t: rapidfuzz.fuzz.token_sort_ratio(_t(search_term), _t(t))
        href_match = lambda h: h.startswith("/lyric/")
        a_tags_boud = SoupStrainer("a", href=href_match)
        soup = generate_bs4_soup(self.session, search_page_url, parse_only=a_tags_boud)
        a_tag = soup.find_all("a", string=lambda t: text_match(t) > 80, limit=4)
        if not a_tag:
            return None

        # The one with the highest similarity score
        a_tag = sorted(a_tag, key=lambda tag: text_match(tag.string))[-1]

        # Fetching and extracting the LRC page
        r = self.session.get(self.ROOT_URL + a_tag["href"])
        lyrics_id = a_tag["href"].split(".")[-1]
        lrc_tag_bound = SoupStrainer(id=f"lyrics_{lyrics_id}_details")
        soup = BeautifulSoup(r.text, features=self.parser, parse_only=lrc_tag_bound)
        return soup.get_text()
