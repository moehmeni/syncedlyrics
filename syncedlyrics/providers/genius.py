"""Genius (genius.com) provider API"""

from typing import Optional
from .base import LRCProvider
from ..utils import generate_bs4_soup


class Genius(LRCProvider):
    """Genius provider class"""

    SEARCH_ENDPOINT = "https://genius.com/api/search/multi?per_page=5&q="

    def __init__(self) -> None:
        super().__init__()
        self.session.cookies.update(
            {
                "_genius_ab_test_cohort": "29",
                "_ga": "GA1.2.1932994869.1708636187",
                "genius_outbrain_rollout_percentage": "72",
                "GLAM-AID": "645b8d4017074db690c166e551a00a57",
                "_fbp": "fb.1.1708636187849.640059451",
                "_pbjs_userid_consent_data": "3524755945110770",
                "OptanonAlertBoxClosed": "2024-02-22T21:09:53.510Z",
                "eupubconsent-v2": "CP6YQRgP6YQRgAcABBENAoEsAP_gAEPgAChQg1NX_H__bW9r8Xr3aft0eY1P99j77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIEu3bBIQFlHJDUTVigaogVryDMakWcgTNKJ6BkiFMRM2dYCF5vmQtj-QKY5vp9d3fx2D-t_dv83dzyz8VHn3e5fme0eJCdA58tDfv9bRKb-9IPd_58v4v0_F_rk2_eT1l_tevp7B-uft87_XU-9_fffpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQagCzDQqIA-yJCQi0HCKBACoKwgIoEAAAAJA0QEAJgwKdgYBLrCRACAFAAMEAIAAUZAAgAAEgAQiACQAoEAAEAgUAAIAAAgEADAwABgAtBAIAAQHQIUwIAFAsAEjMiIUwIQoEggJbKBBICgQVwgCLHAggERMFAAACQAVgAAAsFgMSSAlYkECXEG0AABAAgEEIFQik6MAQwJmy1U4om0ZWkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAACAA.f_wACHwAAAAA",
                "_lr_env_src_ats": "false",
                "_cb": "BqGrFxCkTR8b6HCQ0",
                "__qca": "P0-1896753254-1708636186826",
                "_cc_id": "44fcafb624124a0c66e939f55a947710",
                "_ab_tests_identifier": "631cb00c-2030-48bb-a0fb-cd8bcbde8820",
                "_gid": "GA1.2.174602884.1710502146",
                "panoramaId_expiry": "1710588548654",
                "panoramaId": "088684ec241b4535fa6d8c0fd7c7a9fb927a251f662936cd21c4d192551d0efa",
                "pbjs-unifiedid": "%7B%22TDID%22%3A%22b97d9da1-81b0-4848-b682-ec00b7c6929b%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-02-15T11%3A29%3A08%22%7D",
                "pbjs-unifiedid_last": "Fri%2C%2015%20Mar%202024%2011%3A29%3A10%20GMT",
                "genius_first_impression": "1710519994351",
                "AMP_TOKEN": "%24NOT_FOUND",
                "_gat": "1",
                "GLAM-JID": "5e113fe9d40040179efc20b4f75e8777",
                "GLAM-SID": "5ac7cd368bd14b5faa8d6926b854ce10",
                "__j_state": "%7B%22landing_url%22%3A%22https%3A%2F%2Fgenius.com%2FBillie-eilish-bad-guy-lyrics%22%2C%22pageViews%22%3A1%2C%22prevPvid%22%3A%22a9dfde70fa974fc2ac6ecca66f1c4aea%22%2C%22extreferer%22%3A%22https%3A%2F%2Fgenius.com%2FBillie-eilish-bad-guy-lyrics%22%2C%22user_worth%22%3A0%7D",
                "mp_mixpanel__c": "0",
                "_lr_retry_request": "true",
                "__gads": "ID=8d4cf17bbb16edbf:T=1708636195:RT=1710519997:S=ALNI_MYZWhrjuVovskQAIuhrvz2IR7KKbQ",
                "__gpi": "UID=00000d5f533f0fde:T=1708636195:RT=1710519997:S=ALNI_Mb1bc4uxDepgUqJPgxsSIqujbluiQ",
                "__eoi": "ID=8e9808f101d4011c:T=1708636195:RT=1710519997:S=AA-AfjYPDV6N87f3wI5c7VYO5Z_A",
                "_csrf_token": "27ByewCJkMRlA86a296F4f08hqClIrCX9W3YaIyr5WE%3D",
                "_rapgenius_session": "BAh7BzoPc2Vzc2lvbl9pZEkiJWE3NzlmODU2ZjQwMmQ5M2NkZTY0NzZkZGQyMjIyMWFiBjoGRUY6EF9jc3JmX3Rva2VuSSIxMjdCeWV3Q0prTVJsQTg2YTI5NkY0ZjA4aHFDbElyQ1g5VzNZYUl5cjVXRT0GOwZG--c65a10adf61437ea4d3998326657231efd873559",
                "mp_77967c52dc38186cc1aadebdd19e2a82_mixpanel": "%7B%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22AMP%22%3A%20false%2C%22genius_platform%22%3A%20%22web%22%2C%22%24device_id%22%3A%20%2218dd2a7a0e21725-066bbd18dfd9c9-1e525637-384000-18dd2a7a0e21725%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22Logged%20In%22%3A%20false%2C%22Is%20Editor%22%3A%20null%2C%22Is%20Moderator%22%3A%20null%2C%22Mobile%20Site%22%3A%20false%2C%22%24user_id%22%3A%20%221932994869.1708636187%22%2C%22Tag%22%3A%20%22pop%22%2C%22distinct_id%22%3A%20%221932994869.1708636187%22%7D",
                "OptanonConsent": "isGpcEnabled=0&datestamp=Fri+Mar+15+2024+17%3A26%3A41+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3985c75e-b193-403a-8b77-73dc026af290&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CV2STACK42%3A1&geolocation=%3B&AwaitingReconsent=false",
                "_ga_BJ6QSCFYD0": "GS1.2.1710519996.4.1.1710520000.56.0.0",
                "_chartbeat2": ".1708636193663.1710520001574.0000000010000001.CeExKpDQEitPD5IKxLD5UtuuCW30jh.1",
                "_cb_svref": "external",
                "_chartbeat4": "t=fdVciCHybOTBeCK3mQyy5GDcZwzq&E=0&x=0&c=0.04&y=1221&w=1221",
            }
        )
        self.session.headers.update(
            {
                "authority": "genius.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "en-US,en;q=0.9,fa;q=0.8",
                "cache-control": "max-age=0",
                "if-none-match": 'W/"fbd489530e862287ea58d9f45e5b69c2"',
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            }
        )

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
