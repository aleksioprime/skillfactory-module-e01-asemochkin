import pytest
import game

# проверка принадлежности загаданного слова списку слов в задании
def test_get_word():
    result_word = game.get_word()
    assert result_word in ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

# проверка валидности вводимых символов в качестве угадываемой буквы в слове
@pytest.mark.parametrize("letters", ['v', 'r', 'p', 'T', 'Ю'])
def test_input_true_letter(letters):
    result = game.check_letter(letters)
    assert result == result

# проверка невалидности вводимых символов в качестве угадываемой буквы в слове
@pytest.mark.parametrize("letters", ['1', '', '$', '[', 'skill'])
def test_input_false_letter(letters):
    with pytest.raises(ValueError):
        game.check_letter(letters)

# вариант тестирования вывода угаданных букв в загаданном слове
def test_get_guessed_part_one():
    letters = {'l', 'k', 'r'}
    word = 'skillfactory'
    result = game.get_guessed_part(letters, word)
    assert result == '_ K _ L L _ _ _ _ _ R _'

# вариант тестирования вывода угаданных букв в загаданном слове
def test_get_guessed_part_two():
    letters = {'t', 'i', 'g', 's'}
    word = 'testing'
    result = game.get_guessed_part(letters, word)
    assert result == 'T _ S T I _ G'

# вариант тестирования вывода угаданных букв в загаданном слове
def test_get_guessed_part_three():
    letters = {'v', 'a', 'g', 'e'}
    word = 'coverage'
    result = game.get_guessed_part(letters, word)
    assert result == '_ _ V E _ A G E'

# тестрование функции определения победы в игре на полностью совпадающий угаданных букв с загаданным словом
def test_iswin_true():
    letters = {'t','s','u','n','e','i'}
    word = 'unittest'
    result = game.is_win(letters, word)
    assert result == True

# тестирование функции определения победы при подаче не всех угаданных букв в загаданном слове
def test_iswin_false():
    letters = {'b','a','x','o'}
    word = 'blackbox'
    result = game.is_win(letters, word)
    assert result == False