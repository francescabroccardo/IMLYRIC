"""
This module allows to interact with the API of MUSIXMATCH.
"""

import requests
from imlyric_package.musixmatch_api import *


def get_lyrics_artist_track(artist, track):
    url = base_url + lyrics_matcher
    resp = requests.get(url, params={'q_track': track, 'q_artist': artist, 'apikey': api_key})
    if resp.status_code == 200:
        obj = resp.json()
        if obj['message']['header']['status_code'] == 200:
            return obj['message']['body']['lyrics']['lyrics_body']
    raise Exception


def get_lyrics_id(track_id):
    url = base_url + lyrics_track_matcher
    resp = requests.get(url, params={'track_id': track_id, 'apikey': api_key})
    if resp.status_code == 200:
        obj = resp.json()
        if obj['message']['header']['status_code'] == 200:
            return obj['message']['body']['lyrics']['lyrics_body']
    raise Exception


def get_track(artist, album, track):
    url = base_url + track_matcher
    resp = requests.get(url,
                        params={'q_track': track, 'q_artist': artist, 'q_album': album, 'apikey': api_key})
    if resp.status_code == 200:
        obj = resp.json()
        if obj['message']['header']['status_code'] == 200:
            return obj['message']['body']['track']
    raise Exception
