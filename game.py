import random



def get_word():
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    return random.choice(words)

def input_letter(letters):
    while True:
        letter = input("Буква: ")
        if len(letter) != 1:
            print('[Error] Вы ввели много символов или ничего не ввели.', end=' ')
        elif not letter.isalpha():
            print('[Error] Вы ввели не букву.', end=' ')
        elif letter in letters:
            print('[Error] Вы уже вводили эту букву.', end=' ')
        else:
            return letter
        print('Повторите ввод')

def guess_letter(letters, word):
    return ' '. join(list(map(lambda x: x.upper() if x in letters else '_', word)))

def isWin(letters, word):
    if len(letters) == len(set(word)):
        return True
    else: 
        return False

def game():
    penalty = 0
    win = False;
    hidden_word = get_word()
    print('Загадано слово состоит из', len(hidden_word), 'букв')
    guessed_letters = []
    while penalty < 4:
        letter = input_letter(guessed_letters)
        if letter not in hidden_word:
            print('Ошибка, вам начислен штраф')
            penalty += 1 
        else:
            print('Вы угадали букву')
            guessed_letters.append(letter)
        print(guess_letter(guessed_letters, hidden_word), '| Штрафы:', penalty)
        if isWin(guessed_letters, hidden_word):
            win = True
            break
    return win

if __name__ == '__main__':
    if game():
        print('Вы выиграли')
    else:
        print('Вы проиграли')