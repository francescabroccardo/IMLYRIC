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

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])
    first_artist = artist_names.split(',')[0]
    print(artist_names)

    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artist": first_artist,
        "link": link
    }

    return current_track_info


def get_info_song():
    current_track_id = None
    current_track_info = get_current_track(spo_token)

    if current_track_info['id'] != current_track_id:
        song_name = current_track_info['track_name']
        song_artist = current_track_info['artist']
    return song_name, song_artist


def main():
    lyrics = "ABC"

    return lyrics


if __name__ == '__main__':
    main()
    get_current_track(access_token):
    get_info_song()
