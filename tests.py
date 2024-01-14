"""Some simple tests for geting notifed for API changes of the providers"""

import os
import syncedlyrics
import logging

logging.basicConfig(level=logging.DEBUG)

q = os.getenv("TEST_Q", "bad guy billie eilish")


def _test_provider(provider: str):
    lrc = syncedlyrics.search(q, allow_plain_format=True, providers=[provider])
    assert isinstance(lrc, str)


def test_netease():
    _test_provider("NetEase")


def test_megalobiz():
    _test_provider("Megalobiz")


def test_musixmatch():
    _test_provider("Musixmatch")


def test_lrclib():
    _test_provider("Lrclib")


def test_mx_translation():
    p = syncedlyrics.providers.Musixmatch()
    lrc = p.get_lrc(q, lang="de")
    assert isinstance(lrc, str)
