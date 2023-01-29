import os
import logging
from syncedlyrics import search

logging.basicConfig(level=logging.INFO)
q = os.getenv("TEST_Q", "bad guy billie eilish")


def test_provider(provider: str, allow_plain_format=True) -> bool:
    try:
        search(q, allow_plain_format, providers=[provider])
        print(f"{provider} -> {q} ✅")
        return True
    except Exception as e:
        print(f"{provider} -> {q} ❌")
        print(f"Error: {e}")
        return False


def test_all_providers():
    providers = ["Lyricsify", "NetEase", "Megalobiz"]
    for p in providers:
        test_provider(p)


if __name__ == "__main__":
    test_all_providers()
