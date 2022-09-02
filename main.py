import argparse
from imlyric_package.musixmatch import *
from imlyric_package.spotify import *


def parse_arguments():
    """Parse the command arguments"""
    parser = argparse.ArgumentParser(
        description="Retrieve lyrics information for a given song",
        prog="IMLYRIC",
        epilog="Powered by Musixmatch and Spotify")
    parser.add_argument('--current_track', action='store_true',
                        help="to find lyrics of the track thes user is listening")
    parser.add_argument("--featured_playlist", action='store_true',
                        help="to find lyrics of tracks of the featured playlist")
    parser.add_argument("--album", help="name of the album")
    parser.add_argument("--artist", help="name of the artist")
    parser.add_argument("--track", help="title of the song")
    parser.add_argument("--version", action="version", version="IMLYRIC 1.0")
    return parser.parse_args()


def throw_console_errors(message):
    """Show arguments' errors"""
    return argparse.ArgumentParser().error(message)


def main(arguments):
    if arguments.featured_playlist:
        playlists = get_featured_playlists()
        print("List of playlists: ")
        for i, x in enumerate(playlists):
            print(f"{i + 1}: {x['name']}")
        n = int(input("Choose playlist: ")) - 1
        id_playlist = playlists[n]['id']
        print("List of tracks: ")
        tracks = get_tracks_of_playlist(id_playlist)
        for i, x in enumerate(tracks):
            if x['track']:
                print(f"{i + 1}: {x['track']['name']}")
        n = int(input("Choose track: ")) - 1
        track_name = tracks[n]['track']['name']
        artist_name = tracks[n]['track']['artists'][0]['name']
        print(
            f"Artist: {artist_name}\nTrack: {track_name}\nLyrics:\n{get_lyrics_artist_track(track_name, artist_name)}")
    elif arguments.artist and arguments.album and arguments.track:
        track = get_track(arguments.artist, arguments.album, arguments.track)
        artist_name, album_name, track_name = track['artist_name'], track['album_name'], track['track_name']
        track_id = track['track_id']
        print(f"Artist: {artist_name}\nAlbum: {album_name}\nTrack: {track_name}\nLyrics:\n{get_lyrics_id(track_id)}")
    elif arguments.artist and arguments.track:
        print(
            f"Artist: {arguments.artist}\nTrack: {arguments.track}\nLyrics:\n{get_lyrics_artist_track(arguments.track, arguments.artist)}")


if __name__ == "__main__":
    arguments = parse_arguments()  # parse the command-line arguments
    try:
        main(arguments)
    except Exception as err:
        throw_console_errors(str(err))
