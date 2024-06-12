"""Some simple tests for geting notifed for API changes of the providers"""

import os
import syncedlyrics
import logging

logging.basicConfig(level=logging.DEBUG)

q = os.getenv("TEST_Q", "bad guy billie eilish")


def _test_provider(provider: str, **kwargs):
    lrc = syncedlyrics.search(search_term=q, providers=[provider], **kwargs)
    logging.debug(lrc)
    assert isinstance(lrc, str)
    return lrc


def test_netease():
    _test_provider("NetEase")


def test_musixmatch():
    _test_provider("Musixmatch")


def test_musixmatch_translation():
    lrc = _test_provider("Musixmatch", lang="es")
    # not only testing there is a result, but the translation is also included
    assert syncedlyrics.utils.has_translation(lrc)


def test_musixmatch_enhanced():
    _test_provider("Musixmatch", enhanced=True)


def test_lrclib():
    _test_provider("Lrclib")


def test_genius():
    _test_provider("Genius")


def test_plaintext_only():
    lrc = _test_provider("Lrclib", plain_only=True)
    assert syncedlyrics.utils.identify_lyrics_type(lrc) == "plaintext"


def test_synced_only():
    lrc = _test_provider("Lrclib", synced_only=True)
    assert syncedlyrics.utils.identify_lyrics_type(lrc) == "synced"


# Not working (at least temporarily)
# def test_deezer():
#     _test_provider("Deezer")


# Fails randomly on CI
# def test_megalobiz():
#     _test_provider("Megalobiz")
