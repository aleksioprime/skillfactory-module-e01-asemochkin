import pytest
import game

def test_word():
    result_word = game.get_word()
    assert result_word in ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']