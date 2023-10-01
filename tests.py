"""Some simple tests for geting notifed for API changes of the providers"""

import os
from syncedlyrics import search
import logging
import time

logging.basicConfig(level=logging.DEBUG)

q = os.getenv("TEST_Q", "cranberries zombie")


def _test_provider(provider: str):
    lrc = search(q, allow_plain_format=True, providers=[provider])
    assert isinstance(lrc, str)


def test_netease():
    try:
        _test_provider("NetEase")
    except AssertionError as e:
        # Netease sometimes returns different results (only seen during CI).
        logging.warning("First attempt failed. Trying again.")
        time.sleep(3)
        _test_provider("NetEase")


def test_megalobiz():
    _test_provider("Megalobiz")


def test_musixmatch():
    _test_provider("Musixmatch")


def test_lrclib():
    _test_provider("Lrclib")
