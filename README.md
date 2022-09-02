# IMLYRIC

GNU GENERAL PUBLIC LICENSE

The aim of our project is to create a simple software that behaves like a weather app. O

# Prerequisites

As a prerequisite to use the program you should have at least Python 3.6. Then, you have to install the required
dependencies. You can do that by executing:

`pip3 install -r requirements.txt`

# Run the program

## Featured playlists

You can run:
`python3 main.py --featured_playlists`

to obtain a list of featured playlists in Spotify. The output is something similar to:

```
List of playlists: 
1: New Music Friday Italia
2: Alta Rotazione
...
```

You can then choose the number of a playlist to obtain the tracks of that playlist.

```
Choose playlist: 1
List of tracks: 
1: There’d Better Be A Mirrorball
2: Bellissima
...
```

Finally, you can choose the number of a track to obtain the lyrics.

```
Choose track: 1
Artist: Arctic Monkeys
Track: There’d Better Be A Mirrorball
Lyrics:
Don't get emotional, that ain't like you
...
```

## Lyrics of a track

You can obtain the lyrics of a track by providing the artist and the track. Optionally, you can provide the album as
well, this allows to better find the correct track if some information is partially wrong. For instance, you can run:

`python3 main.py --artist "Beatles" --album "Boxset" --track "Let it be"`

and see the output:

``` 
Artist: The Beatles
Album: The Beatles Boxset
Track: Let It Be
Lyrics:
When I find myself in times of trouble
...
```

# APIs

The program exploits the APIs of:

- [Musixmatch](https://developer.spotify.com/documentation/web-api/): it allows to find lyrics information about songs;
- [Spotify](https://developer.spotify.com/documentation/web-api/):  it allows to find information about songs,
  playlists, albums, artists in Spotify.

# Testing

We have tested our main modules musixmatch.py module and spotify.py module. You can find both tests in the
folder `imlyric_package/tests/`. To execute them, from the main folder, run

``` 
python3 -m unittest -v -b 
```

All tests run correctly.

# Authors

Francesca Broccardo Daniel Pezzettone Federico Polin Alessandro Brunelli

# License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
