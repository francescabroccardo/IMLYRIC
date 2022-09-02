"""
Tests for the musixmatch module
"""
from unittest import TestCase
from imlyric_package.musixmatch import *


class TestMusixmatch(TestCase):
    def test_get_lyrics_id_none(self):
        """
        Tests get_lyrics_id with a wrong input.
        """
        self.assertRaises(Exception, get_lyrics_id, None)

    def test_get_lyrics_id_wrong(self):
        """
        Tests get_lyrics_id with None as input.
        """
        self.assertRaises(Exception, get_lyrics_id, "a")

    def test_get_lyrics_id_right(self):
        """
        Tests get_lyrics_id with a valid input.
        """
        res = get_lyrics_id(227377601)
        self.assertRegex(res, "When I find myself in times of trouble.*")

    def test_get_lyrics_artist_track_none(self):
        """
        Tests get_lyrics_artist_track with None as input.
        """
        self.assertRaises(Exception, get_lyrics_artist_track, None, "a")

    def test_get_lyrics_artist_track_wrong(self):
        """
        Tests get_lyrics_artist_track with a wrong input
        """
        self.assertRaises(Exception, get_lyrics_artist_track, "0i2ojwoirnrwe", "iwreirewirujr")

    def test_get_lyrics_artist_track_right(self):
        """
        Tests get_lyrics_artist_track with a valid input.
        """
        res = get_lyrics_artist_track("The Beatles", "Let it be")
        self.assertRegex(res, "When I find myself in times of trouble.*")

    def test_get_track_none(self):
        """
        Tests get_track with None as input.
        """
        self.assertRaises(Exception, get_track, None, None, "3oko33koww")

    def test_get_track_wrong(self):
        """
        Tests get_track with a wrong input
        """
        self.assertRaises(Exception, get_track, "0i2ojwoirnrwe", "iwreirewirujr", "3oko33koww")

    def test_get_track_right(self):
        """
        Tests get_track with a valid input.
        """
        track = get_track("The Beatles", "The Beatles Boxset", "Let it be")
        artist_name, album_name = track['artist_name'], track['album_name']
        track_name, track_id = track['track_name'], track['track_id']
        self.assertEqual(artist_name, "The Beatles")
        self.assertEqual(album_name, "The Beatles Boxset")
        self.assertEqual(track_name, "Let It Be")
        self.assertEqual(track_id, 227377601)
