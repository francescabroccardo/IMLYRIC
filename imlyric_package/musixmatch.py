"""
This module allows to interact with the API of MUSIXMATCH.
"""

import requests

MUSISXMATCH_URI = 'https://api.musixmatch.com/ws/1.1/'
MUSISXMATCH_API_KEY = 'f5850d5632895b51bffdc58767606547'


def get_lyrics_artist_track(artist, track):
    url = MUSISXMATCH_URI + 'matcher.lyrics.get'
    resp = requests.get(url, params={'q_track': track, 'q_artist': artist, 'apikey': MUSISXMATCH_API_KEY})
    if resp.status_code == 200:
        obj = resp.json()
        if obj['message']['header']['status_code'] == 200:
            return obj['message']['body']['lyrics']['lyrics_body']
    raise Exception


def get_lyrics_id(track_id):
    url = MUSISXMATCH_URI + 'track.lyrics.get'
    resp = requests.get(url, params={'track_id': track_id, 'apikey': MUSISXMATCH_API_KEY})
    if resp.status_code == 200:
        obj = resp.json()
        if obj['message']['header']['status_code'] == 200:
            return obj['message']['body']['lyrics']['lyrics_body']
    raise Exception
