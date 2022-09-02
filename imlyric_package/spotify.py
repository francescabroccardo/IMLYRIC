"""
This module allows to interact with the APIs of spotify to get information about playlists.
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_URI = 'https://accounts.spotify.com/api/'
SPOTIFY_CLIENT_ID = 'bd8cd579afdc49cbb7e9703f95b05bb9'
SPOTIFY_CLIENT_SECRET = '5d28350a18bc4b188f934b7f62c45efb'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                                         client_secret=SPOTIFY_CLIENT_SECRET))


def get_featured_playlists():
    results = sp.featured_playlists()['playlists']['items']
    return results


def get_tracks_of_playlist(id):
    results = sp.playlist_items(id)['items']
    print(results)
    return results
