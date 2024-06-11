"""Lyricsify (lyricsify.com) LRC provider"""

from typing import Optional
from bs4 import SoupStrainer
from .base import LRCProvider
from ..utils import Lyrics, generate_bs4_soup, get_best_match

# Currently broken
# TODO: Bypassing Cloudflare anti-bot system


class Lyricsify(LRCProvider):
    """Lyricsify LRC provider class"""

    ROOT_URL = "https://www.lyricsify.com"
    SEARCH_ENDPOINT = ROOT_URL + "/search?q="

    def __init__(self) -> None:
        super().__init__()
        self.parser = "html.parser"

    def get_lrc(self, search_term: str) -> Optional[Lyrics]:
        url = self.SEARCH_ENDPOINT + search_term.replace(" ", "+")
        href_match = lambda h: h.startswith("/lyric/")
        a_tags_boud = SoupStrainer("a", href=href_match)
        soup = generate_bs4_soup(self.session, url, parse_only=a_tags_boud)
        cmp_key = lambda t: t.get_text().lower().replace("-", "")
        a_tag = get_best_match(soup.find_all("a"), search_term, cmp_key)
        if not a_tag:
            return None
        # Scraping from the LRC page
        lrc_id = a_tag["href"].split(".")[-1]
        soup = generate_bs4_soup(self.session, self.ROOT_URL + a_tag["href"])
        lrc_str = soup.find("div", {"id": f"lyrics_{lrc_id}_details"}).get_text()
        lrc = Lyrics()
        lrc.add_unknown(lrc_str)
        return lrc
