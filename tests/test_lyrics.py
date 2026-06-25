import pytest
import re
from collections import Counter

class TestLyricsTokenization:
    def test_verse_splitting(self):
        lyrics = "Verse 1\nLine one\nLine two\n\nChorus\nSing along\nSing along"
        verses = [v.strip() for v in lyrics.split("\n\n") if v.strip()]
        assert len(verses) == 2

    def test_rhyme_detection(self):
        lines = ["I see the stars at night","They shine so bright","The moon gives off its light"]
        endings = [line.split()[-1].lower() for line in lines]
        assert "night" in endings and "bright" in endings and "light" in endings

    def test_word_frequency_in_lyrics(self):
        lyrics = "love love love hate love hate"
        freq = Counter(lyrics.split())
        assert freq["love"] == 4
        assert freq["hate"] == 2

    def test_repetition_detection(self):
        lyrics = "na na na na hey hey goodbye"
        tokens = lyrics.split()
        freq = Counter(tokens)
        repeated = [w for w,c in freq.items() if c > 1]
        assert "na" in repeated

    def test_unique_word_ratio(self):
        lyrics = "I love you and you love me"
        tokens = lyrics.split()
        ratio = len(set(tokens)) / len(tokens)
        assert 0 < ratio <= 1.0

class TestLyricsAnalysis:
    def test_sentiment_positive_lyrics(self):
        positive = {"love","happy","joy","wonderful","amazing","great"}
        text = "I love this wonderful amazing day"
        found = sum(1 for w in text.split() if w.lower() in positive)
        assert found >= 2

    def test_artist_comparison(self):
        artist_a = {"love","heart","dream","hope"}
        artist_b = {"power","fight","win","strong"}
        overlap = artist_a & artist_b
        assert len(overlap) == 0

    def test_line_count(self):
        lyrics = "Line 1\nLine 2\nLine 3\nLine 4"
        lines = [l for l in lyrics.split("\n") if l.strip()]
        assert len(lines) == 4
