"""Megalobiz (megalobiz.com) LRC provider"""

from typing import Optional
from bs4 import SoupStrainer
from .base import LRCProvider
from ..utils import Lyrics, generate_bs4_soup, get_best_match


class Megalobiz(LRCProvider):
    """Megabolz provider class"""

    ROOT_URL = "https://www.megalobiz.com"
    SEARCH_ENDPOINT = ROOT_URL + "/search/all?qry={q}&searchButton.x=0&searchButton.y=0"

    def get_lrc(self, search_term: str) -> Optional[Lyrics]:
        url = self.SEARCH_ENDPOINT.format(q=search_term.replace(" ", "+"))

        def href_match(h: Optional[str]):
            if h and h.startswith("/lrc/maker/"):
                return True
            return False

        a_tags_boud = SoupStrainer("a", href=href_match)
        soup = generate_bs4_soup(self.session, url, parse_only=a_tags_boud)

        def a_text(a):
            # In MegaLobiz, we have some `a` tags that have the following text:
            # artist track ( lyrics ) [05:10.47] (we don't want that extra text)
            part = a.get_text().replace("by", "").split()[: search_term.count(" ") + 1]
            return " ".join(part)

        a_tag = get_best_match(soup.find_all("a"), search_term, a_text)
        if not a_tag:
            return None
        # Scraping from the LRC page
        lrc_id = a_tag["href"].split(".")[-1]
        soup = generate_bs4_soup(self.session, self.ROOT_URL + a_tag["href"])
        lrc_str = soup.find("div", {"id": f"lrc_{lrc_id}_details"}).get_text()
        lrc = Lyrics()
        lrc.add_unknown(lrc_str)
        return lrc
