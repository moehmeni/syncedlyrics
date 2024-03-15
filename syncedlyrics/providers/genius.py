"""Genius (genius.com) provider API"""

from typing import Optional
from .base import LRCProvider
from ..utils import generate_bs4_soup


class Genius(LRCProvider):
    """Genius provider class"""

    SEARCH_ENDPOINT = "https://genius.com/api/search/multi?per_page=5&q="

    def get_lrc(self, search_term: str) -> Optional[str]:
        params = {"q": search_term, "per_page": 5}
        cookies = {
            "obuid": "e3ee67e0-7df9-4181-8324-d977c6dc9250",
        }
        r = self.session.get(self.SEARCH_ENDPOINT, params=params, cookies=cookies)
        if not r.ok:
            return None
        data = r.json()
        data = data["response"]["sections"][1]["hits"]
        if not data:
            return None
        url = data[0]["result"]["url"]
        soup = generate_bs4_soup(self.session, url)
        els = soup.find_all("div", attrs={"data-lyrics-container": True})
        if not els:
            return None
        lrc = ""
        for el in els:
            lrc += el.get_text(separator="\n", strip=True).replace("\n[", "\n\n[")
        return lrc
