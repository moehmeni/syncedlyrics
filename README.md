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
You can also get a translation along the original lines (if available on Musixmatch):
```
syncedlyrics "SEARCH_TERM" -l es
```

#### Available Options
| Flag | Description |
| --- | --- |
| `-o` | Path to save `.lrc` lyrics, default="{search_term}.lrc" |
| `-p` | Comma-separated list of providers to include in searching |
| `-l` | Language of the translation along with the lyrics **(Curently only by Musixmatch)** |
| `-v` | Use this flag to show the logs |
| `--allow-plain` | Return a plain text (not synced) lyrics if no LRC format was found |

### Python
```py
import syncedlyrics
lrc = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")
```
Or with options:
```py
syncedlyrics.search("...", allow_plain_format=True, save_path="{search_term}_1234.lrc", providers=["NetEase"])
```
Translated version (Note language codes should follow [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)):
```
syncedlyrics.search("...", lang="de")
```

## Providers
- [Musixmatch](https://www.musixmatch.com/)
- [Lrclib](https://github.com/tranxuanthang/lrcget/issues/2#issuecomment-1326925928)
- [NetEase](https://music.163.com/)
- [Megalobiz](https://www.megalobiz.com/)
- ~~[Lyricsify](https://www.lyricsify.com/)~~ (Broken, should bypass Cloudflare protection)
- ~~[Deezer](https://deezer.com/)~~ (Broken)

Feel free to suggest more providers or make PRs to fix the broken ones.

## License
[MIT](https://github.com/rtcq/syncedlyrics/blob/master/LICENSE)
