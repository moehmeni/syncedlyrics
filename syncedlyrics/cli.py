import argparse
import logging
from syncedlyrics import search


def cli_handler():
    """
    Console entry point handler function.
    This parses the CLI arguments passed to `syncedlyrics -OPTIONS` command
    """
    parser = argparse.ArgumentParser(
        description="Search for an LRC format (synchronized lyrics) of a music"
    )
    parser.add_argument("search_term", help="The search term to find the track.")
    parser.add_argument(
        "-o", "--output", help="Path to save '.lrc' lyrics", default="{search_term}.lrc"
    )
    parser.add_argument(
        "--allow-plain",
        help="Return a plain text (not synced) lyrics if not LRC was found",
        action="store_true",
    )
    parser.add_argument(
        "-v", "--verbose", help="Use this flag to show the logs", action="store_true"
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    lrc = search(args.search_term, args.allow_plain, args.output)
    if lrc:
        print(lrc)
