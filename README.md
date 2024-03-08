# syncedlyrics
 Get an LRC format (synchronized) lyrics for your music.
 
 [![Downloads](https://static.pepy.tech/badge/syncedlyrics/month)](https://pepy.tech/project/syncedlyrics)

## Installation
```
pip install syncedlyrics
```
## Usage
### CLI
```
syncedlyrics "SEARCH_TERM"
```

#### Available Options
| Flag | Description |
| --- | --- |
| `-o` | Path to save `.lrc` lyrics, default="{search_term}.lrc" |
| `-p` | Space-separated list of providers to include in searching |
| `-l` | Language code of the translation ([ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format) |
| `-v` | Use this flag to show the logs |
| `--allow-plain` | Return a plain text (not synced) lyrics if no LRC format was found |

### Python
```py
lrc = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")
```
Or with options:
```py
syncedlyrics.search("...", allow_plain_format=True, save_path="{search_term}_1234.lrc", providers=["NetEase"])
```
Get a translation along with the original lyrics (separated by `\n`):
```py
syncedlyrics.search("...", lang="de")
```

## Providers
- [Musixmatch](https://www.musixmatch.com/)
- [Deezer](https://deezer.com/)
- [Lrclib](https://github.com/tranxuanthang/lrcget/issues/2#issuecomment-1326925928)
- [NetEase](https://music.163.com/)
- [Megalobiz](https://www.megalobiz.com/)
- ~~[Lyricsify](https://www.lyricsify.com/)~~ (Broken duo to Cloudflare protection)

Feel free to suggest more providers or make PRs to fix the broken ones.

## License
[MIT](https://github.com/rtcq/syncedlyrics/blob/master/LICENSE)
