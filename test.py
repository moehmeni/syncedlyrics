import unittest
import os
from syncedlyrics import search

q = os.getenv("TEST_Q", "bad guy billie eilish")


class ProvidersTestCase(unittest.TestCase):
    def _test_provider(self, provider: str):
        lrc = search(q, allow_plain_format=True, providers=[provider])
        self.assertIsInstance(lrc, (str, type(None)))

    def test_netease(self):
        self._test_provider("NetEase")

    def test_lyricsify(self):
        self._test_provider("Lyricsify")

    def test_megalobiz(self):
        self._test_provider("Megalobiz")


if __name__ == "__main__":
    unittest.main()
