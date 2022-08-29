import requests

# spotify authentication
spo_getcurrent_url = 'https://api.spotify.com/v1/me/player/currently-playing'  # got by Spotify for Developers webpage
spo_token = 'BQDpxsDbh2Frq-JGm9f4ZO_7EXqbe2kI0KbGBKRfVuzuqbgIrHOb8OP00yguqyoXyUADDBjyqr7c8e_Y3knLY6HUfV_SXZ_AnzGIlameBnY6QXR1GHJmNJn4zWR2AFw-srIhpnIiKlSJSk5TVLElfBfmhztbwjiX44sDPcAaEO9yhGeIrFIga7r1Exl0zrf37mjAUxXz'


# Get current spotify track info
def get_current_track(access_token):
    response = requests.get(
        spo_getcurrent_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    current_track_info = {
        'track_name': 'abc',
        'id': 'abc',
        'artist': 'abc'
    }

    return current_track_info


def get_info_song():
  song_name = 'ABC'
  song_name = 'ABC'
  return song_name, song_artist


def main():
    lyrics = "ABC"

    return lyrics


if __name__ == '__main__':
    main()
    get_info_song()
