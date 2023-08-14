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

## Providers
- [Lrclib](https://github.com/tranxuanthang/lrcget/issues/2#issuecomment-1326925928)
- [Musixmatch](https://www.musixmatch.com/)
- [NetEase](https://music.163.com/)
- [Megalobiz](https://www.megalobiz.com/)
- ~~[Lyricsify](https://www.lyricsify.com/)~~ (Broken, should bypass Cloudflare proteciton)
- ~~[Deezer](https://deezer.com/)~~ (Broken)

Feel free to suggest more providers or making PRs to fix the broken providers.

## License
[MIT](https://github.com/rtcq/syncedlyrics/blob/master/LICENSE)
