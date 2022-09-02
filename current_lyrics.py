import requests
from musixmatch import Musixmatch


def get_curr_track_info():
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


def get_lyrics(song, artist):
    # Auth MusixMatch API
    token = 'f5850d5632895b51bffdc58767606547'
    musixmatch = Musixmatch(token)

    # Get lyrics
    lyrics = musixmatch.matcher_lyrics_get(song, artist)
    testo = lyrics['message']['body']['lyrics']['lyrics_body']

    return testo


def main():
    # canzone = get_curr_track_info(spo_token)[0]
    # artista = get_curr_track_info(spo_token)[1]

    canz_id = str(get_curr_track_info())
    testo = get_lyrics(song_name, song_artist)

    print(song_name + ', ' + song_artist + ' Song ID = ' + canz_id + ' ' + testo)

    return 1


if __name__ == '__main__':
    main()
