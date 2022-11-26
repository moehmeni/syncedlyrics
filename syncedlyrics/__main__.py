import argparse
import logging
import syncedlyrics

if __name__ == "__main__":
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
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    lrc = syncedlyrics.search(args.search_term, args.allow_plain, args.output)
    if lrc:
        print(lrc)
