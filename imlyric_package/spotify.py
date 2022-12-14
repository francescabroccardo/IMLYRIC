"""
This module allows to interact with the APIs of spotify to get information about playlists.
"""
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_URI = 'https://accounts.spotify.com/api/'
SPOTIFY_CLIENT_ID = 'bd8cd579afdc49cbb7e9703f95b05bb9'
SPOTIFY_CLIENT_SECRET = '5d28350a18bc4b188f934b7f62c45efb'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                                         client_secret=SPOTIFY_CLIENT_SECRET))


def get_featured_playlists():
    """
    :return: the list of featured playlists
    """
    results = sp.featured_playlists()['playlists']['items']
    return results


def get_tracks_of_playlist(id):
    """
    :param id: playlist
    :return: the list of tracks in the playlist id
    """
    results = sp.playlist_items(id)['items']
    return results


def get_curr_track_id():
    """
    :return: the id of the track the user is currently listening
    """
    token = 'BQDfXRTqChB9KaxvfyYHcV8TocDKvvxtxpNJ58b7nNohg1S8Q9TEaeKq0tmNIDmuqGt-xNd2uIBWqJUDmYijCX6GPGKLulPvezaHWxXMkBgdXvgmPaZoXAz37GBr4mlbV1P0XIdJBhwxH2YTXIe9H-Ypg8sN8b-C9yWwMBaJGx55ohXGJ3lbhYy17vhvXzo5Dv3VG4iO'
    query = 'https://api.spotify.com/v1/me/player/currently-playing'  # got by Spotify for Developers webpage

    response = requests.get(
        query,
        headers={'Authorization': f'Bearer {token}'}
    )
    json_resp = response.json()['item']

    track_id = json_resp['id']
    track_name = json_resp['name']
    artists = [artist for artist in json_resp['artists']]

    link = json_resp['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])
    first_artist = artist_names.split(',')[0]

    current_track_info = {
        'id': track_id,
        'track_name': track_name,
        'artist': first_artist,
        'link': link
    }

    current_track_id = None

    if current_track_info['id'] != current_track_id:
        global song_name
        global song_artist
        global song_id

        song_name = current_track_info['track_name']
        song_artist = current_track_info['artist']
        song_id = current_track_info['id']

    else:
        return 0

    return song_id


def add_song(fav_song_id):
    """
    :param fav_song_id: song to add
    :return: 1 if fav_song_id is added to the library, -1 otherwise
    """
    token = 'BQDo8YQtSFRivxQZAmCl_JOk6Uhzw9IQYbIrw020vVnr_nU4cHgyucWshBd_KpkG_WGaOhXa2a2Ku_CIwtvbcyzbdd-n2-9QvPVHC8gJUjjL43jmjU_GMB1nC8mor8YaCsT2gEnCHYDpIKyx4CGf3qcA9DX0a6o7Hpuf0-fTGa28ZLtH7ZrKGRTeDwN6lDcK0TbFaEDajw1uzZGv'
    query = 'https://api.spotify.com/v1/me/tracks?ids={canzone}'.format(canzone=fav_song_id)

    response = requests.put(
        query,
        data={'ids': fav_song_id},
        headers={'Authorization': f'Bearer {token}'}
    )

    if response.status_code == 200:
        print('Song added succesfully!')
    else:
        print('Failed to add the song, error: ' + str(response.status_code) + ", " + response.reason)
        return 0

    return 1
