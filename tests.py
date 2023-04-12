"""Some simple tests for geting notifed for API changes of the providers"""

import os
from syncedlyrics import search

q = os.getenv("TEST_Q", "bad guy billie eilish")

def _test_provider(provider: str):
	lrc = search(q, allow_plain_format=True, providers=[provider])
	assert isinstance(lrc, (str, type(None)))

def test_netease():
	_test_provider("NetEase")

def test_lyricsify():
	_test_provider("Lyricsify")

def test_megalobiz():
	_test_provider("Megalobiz")
	
def test_musixmatch():
	_test_provider("Musixmatch")
