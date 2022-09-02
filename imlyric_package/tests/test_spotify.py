"""
Tests for the spotify module
"""
from unittest import TestCase
from imlyric_package.spotify import *


class TestSpotify(TestCase):
    def test_get_featured_playlists(self):
        """
        Tests get_featured_playlists with a wrong input.
        """
        self.assertIsNotNone(get_featured_playlists())

    def test_get_tracks_of_playlist_none(self):
        """
        Tests get_tracks_of_playlist with None as input.
        """
        self.assertRaises(Exception, get_tracks_of_playlist, None)


    def test_get_tracks_of_playlist_wrong(self):
        """
        Tests get_tracks_of_playlist with a wrong input
        """
        self.assertRaises(Exception, get_tracks_of_playlist, "oqnrueouiq3ojenrneriwewelkfe")


    def test_get_tracks_of_playlist_right(self):
        """
        Tests get_tracks_of_playlist with None as input.
        """
        self.assertIsNotNone(get_tracks_of_playlist("37i9dQZF1DWVKDF4ycOESi"))
