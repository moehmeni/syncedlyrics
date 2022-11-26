# syncedlyrics
 Get an LRC format (synchronized) lyrics for your music.

## Installation
```
pip install syncedlyrics
```
## Usage
### CLI
```
python -m syncedlyrics "SEARCH_TERM"
```
#### Available Options
| Flag | Description |
| --- | --- |
| `-o` | Path to save '.lrc' lyrics", default="{search_term}.lrc |
| `-v` | Use this flag to show the logs |
| `--allow-plain` | Return a plain text (not synced) lyrics if not LRC was found |

### Python
```py
import syncedlyrics
lrc = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")
```
Or with options:
```py
syncedlyrics.search("...", allow_plain_format=True, save_path="{search_term}_1234.lrc")
```

## Providers
- NetEase (music.163.com)

Feel free to suggest more providers please.

## License
[MIT](https://github.com/rtcq/syncedlyrics/blob/master/LICENSE)

## Notes
I also found a [repo](https://github.com/fashni/MxLRC) for MusixMatch API, but it has annoying API rate limits at the moment