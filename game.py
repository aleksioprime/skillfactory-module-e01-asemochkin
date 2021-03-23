import random

# получение загаданнного слова, выбранного из списка
def get_word():
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    return random.choice(words)

# проверка введённых данных на корректность
def check_letter(letter):
        if len(letter) != 1:
            raise ValueError("Вы ввели много символов или ничего не ввели")
        elif not letter.isalpha():
            raise ValueError('Вы ввели не букву')
        else:
            return letter

# получение строки угаданных букв в загаданном слове для вывода на экран
def get_guessed_part(letters, word):
    return ' '. join(list(map(lambda x: x.upper() if x in letters else '_', word)))

# проверка выполнения условия выигрыша (угаданы все буквы в загаданном слове) 
def is_win(letters, word):
    if len(letters) == len(set(word)):
        return True
    else: 
        return False

# функция самой игры, возвращает флаг победы в игре
def game():
    # начальные параметры: счётчик штрафных очков, флаг победы в игре, пустое множество угаданных букв
    penalty = 0
    win = False;
    guessed_letters = set()
    # получение загаданного слова и вывод на экран кол-во букв в нём
    hidden_word = get_word()
    print('Загаданное слово состоит из', len(hidden_word), 'букв')
    # цикл игры с условием выхода из него по набору 4 штрафных очков 
    while penalty < 4:
        # получение буквы (ввод с клавиатуры и проверка на валидность)
        letter = check_letter(input("Введите букву: "))
        # проверка существования такой буквы в загаданном слове
        if letter.lower() not in hidden_word:
            # если нет буквы в слове, то повышается счётчик штрафов
            penalty += 1 
        else:
            # если буква есть в слове, то она добавляется в множество угаданных букв
            guessed_letters.add(letter)
        # на экране печатается строка угаданных и неугаданных букв в слове
        print(get_guessed_part(guessed_letters, hidden_word))
        # если выполняются условия победы в игре, то меняется флаг win и выходим из цикла
        if is_win(guessed_letters, hidden_word):
            win = True
            break
    # функция возвращает флаг победы в игре 
    return win

if __name__ == '__main__':
    if game():
        print('Вы выиграли')
    else:
        print('Вы проиграли')