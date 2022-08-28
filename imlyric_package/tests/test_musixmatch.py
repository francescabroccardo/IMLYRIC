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
