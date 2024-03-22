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
| `-p` | Space-separated list of [providers](#providers) to include in searching |
| `-l` | Language code of the translation ([ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format) |
| `-v` | Use this flag to show the logs |
| `--allow-plain` | Return a plain text (not synced) lyrics if no LRC format was found |
| `--enhanced` | Return an [Enhanced](https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag) (word-level karaoke) format

### Python
```py
# This simple
lrc = syncedlyrics.search("[TRACK_NAME] [ARTIST_NAME]")

# Or with options:
syncedlyrics.search("...", allow_plain_format=True, save_path="{search_term}_1234.lrc", providers=["NetEase"])

# Get a translation along with the original lyrics (separated by `\n`):
syncedlyrics.search("...", lang="de")

# Get a word-by-word (karaoke) synced-lyrics if available
syncedlyrics.search("...", enhanced=True)
```

## Providers
- [Musixmatch](https://www.musixmatch.com/)
- [Deezer](https://deezer.com/)
- [Lrclib](https://github.com/tranxuanthang/lrcget/issues/2#issuecomment-1326925928)
- [NetEase](https://music.163.com/)
- [Genius](https://genius.com) (For plain format)
- ~~[Megalobiz](https://www.megalobiz.com/)~~ (Website not working anymore)
- ~~[Lyricsify](https://www.lyricsify.com/)~~ (Broken duo to Cloudflare protection)

Feel free to suggest more providers or make PRs to fix the broken ones.

## License
[MIT](https://github.com/rtcq/syncedlyrics/blob/master/LICENSE)

## Citation
If you use this library in your research, you can cite as follows:
```
@misc{syncedlyrics,
  author = {Momeni, Mohammad},
  title = {syncedlyrics},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/moehmeni/syncedlyrics}},
}
```
