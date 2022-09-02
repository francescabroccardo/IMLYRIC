# IMLYRIC
GNU GENERAL PUBLIC LICENSE

The aim of our project is to create a simple software that behaves like a weather app. O

# Tutorial

As a prerequisite to use the program you should have at least Python 3.5. Then, you have to install the required dependencies. You can do that by executing:

`pip3 install -r requirements.txt`

Finally, to run the program, you simply need to execute:

`python3 main.py`

# APIs

The program exploits the APIs of:
- [Musixmatch](https://developer.spotify.com/documentation/web-api/): it allows to find lyrics information about songs;
- [Spotify](https://developer.spotify.com/documentation/web-api/):  it allows to find information about songs, playlists, albums, artists in Spotify.

# Testing

We have tested our main modules musixmatch.py module and spotify.py module. You can find both tests in the folder `imlyric_package/tests/`. To execute them, from the main folder, run
``` 
python3 -m unittest -v -b 
```
All tests run correctly.

# Authors
Francesca Broccardo 
Daniel Pezzettone
Federico Polin
Alessandro Brunelli

# License
[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)