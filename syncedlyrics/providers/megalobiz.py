"""Megalobiz (megalobiz.com) LRC provider"""

from typing import Optional
from bs4 import SoupStrainer
from .base import LRCProvider
from ..utils import generate_bs4_soup


class Megalobiz(LRCProvider):
    """Megabolz provider class"""

    ROOT_URL = "https://www.megalobiz.com"
    SEARCH_ENDPOINT = ROOT_URL + "/search/all?qry={q}&searchButton.x=0&searchButton.y=0"

    def get_lrc(self, search_term: str) -> Optional[str]:
        url = self.SEARCH_ENDPOINT.format(q=search_term)

        def href_match(h: Optional[str]):
            if h and h.startswith("/lrc/maker/"):
                return True
            return False

        a_tags_boud = SoupStrainer("a", href=href_match)
        soup = generate_bs4_soup(self.session, url, parse_only=a_tags_boud)
        # Selecting the first a tag
        # TODO: We can also sort a tags based on a string similarity as done for
        # Lyricsify provider before, but for now this seem to be enough
        a_tag = soup.find("a")
        if not a_tag:
            return None
        # Scraping from the LRC page
        lrc_id = a_tag["href"].split(".")[-1]
        soup = generate_bs4_soup(self.session, self.ROOT_URL + a_tag["href"])
        return soup.find("div", {"id": f"lrc_{lrc_id}_details"}).get_text()
