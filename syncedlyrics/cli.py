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
        "-p",
        help="Providers to include in the searching (separated by space). Default: all providers",
        default="",
        choices=["deezer", "lrclib", "musixmatch", "netease", "genius"],
        nargs="+",
        type=str.lower,
    )
    parser.add_argument(
        "-l", "--lang", help="Language of the translation along with the lyrics"
    )
    parser.add_argument(
        "-o", "--output", help="Path to save '.lrc' lyrics", default="{search_term}.lrc"
    )
    parser.add_argument(
        "-v", "--verbose", help="Use this flag to show the logs", action="store_true"
    )
    parser.add_argument(
        "--allow-plain",
        help="Return a plain text (not synced) lyrics if not LRC was found",
        action="store_true",
    )
    parser.add_argument(
        "--enhanced",
        help="Returns word by word synced lyrics (if available)",
        action="store_true",
    )
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    lrc = search(
        args.search_term,
        args.allow_plain,
        args.output,
        args.p,
        lang=args.lang,
        enhanced=args.enhanced,
    )
    if lrc:
        print(lrc)
