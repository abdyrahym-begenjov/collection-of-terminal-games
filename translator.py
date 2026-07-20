rutranslate={
    '(GitHub: abdyrahym-begenjov)': '(GitHub: abdyrahym-begenjov)',
    'The Cities Game': 'Города',
    'COLLECTION OF TERMINAL GAMES': 'КОЛЛЕКЦИЯ ТЕРМИНАЛЬНЫХ ИГР',
    'Choose a game or parameter: ': 'Выберите игру или параметр: ',
    'Enter the word:': 'Введите слово:',
    'Error!!!': 'Ошибка!!!',
    'Game Over!!!': 'Игра окончена!!!',
    'This word has already been used.': 'Это слово уже было использовано.',
    'You have': 'У вас есть',
    '❤️ . Enter the word: ': '❤️ . Введите слово: ',
    '❤️ . Enter the word or ability: ': '❤️ . Введите слово или способность: ',
    'You received': 'Вы получили',
    'points.': 'баллов.',
    'Absolute Champion!!!  🏆': 'Абсолютный чемпион!!!   🏆',
    'Loser!!!': 'Неудачник!!!',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'You must enter the word!!!': 'Вы должны ввести слово!!!',
    'Enter to exit: ': 'Введите для выхода: ',
    'Enter your name: ': 'Введите свое имя: ',
    'Enter to exit mode: ': 'Войдите в режим выхода: ',
    'Game      Rules      Highscores      Exit': 'Игра      Правилы      Рекорды      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change parameters (Enter \"Name\" or \"Language\"): ': 'Хотите ли вы изменить параметры (введите \"Имя\" или \"Язык\"): ',
    'Do you want to exit (\"Yes\" or \"No\"): ': 'Вы хотите завершить (\"Да\" или \"Нет\"): ',
    'Goodbye!!!': 'До свидания!!',
    'Name: ': 'Имя: ',
    'Language: ': 'Язык: ',
    'No': 'Нет',
    'Game': 'Игра',
    'Rules': 'Правилы',
    'Highscores': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход',
    'NAME |': 'ИМЯ |',
    'POINTS': 'БАЛЛЫ',
    'LEADERBOARD:': 'ЛИДЕРБОРД:',
    'You are ABSOLUTE CHAMPION!!!': 'Вы АБСОЛЮТНЫЙ ЧЕМПИОН!!!',
    'You\'ve broken a new highscore!!!': 'Вы побили новый рекорд!!!',
    'WINNER': 'ПОБЕДИТЕЛЬ',
    'ROUND-UP': 'ВТОРОЕ МЕСТО',
    'BRONZE MEDALIST': 'БРОНЗОВЫЙ ПРИЗЁР',
    'LOSER': 'ЛУЗЕР',
    'This name is already taken': 'Это имя уже занято',
    'The name must not exceed 16 characters': 'Имя не должно превышать 16 символов',
    'Easy': 'Лёгкий',
    'Normal': 'Нормальный',
    'Hard': 'Сложный',
    'Player 2': 'Игрок 2',
    'Player 3': 'Игрок 3',
    'Player 4': 'Игрок 4',
    'Moment of Truth  🥁': 'Момент истины  🥁',
    'Enter number of the players: ': 'Введите количество игроков: ',
    'Parameters of game: Easy (10), Normal (20), Hard (30)': 'Параметры игры: Лёгкий (10), Нормальный (20), Сложный (30)',
    'Enter the parameter of game: ': 'Введите параметр игры: ',
    'Infinity': 'Бесконечность',
    'Party': 'Вечеринка',
    'Overall Result': 'Общий Результат',
    'Points:': 'Баллы:',
    'You have received the maximum points': 'Вы получили максимальные очки',
    'You are WINNER!!!': 'Вы ПОБЕДИТЕЛЬ!!!',
    'You are eliminated from the game!!!': 'Вы выбываете из игры!!!',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Infinity          Party': 'Бесконечность          Вечеринка',
    'Enter name: ': 'Введите имя: ',
    'Enter language: ': 'Введите язык: ',
    'Blaster': 'Бластер',
    'Game Pass': 'Пропуск',
    'Replacement': 'Замена',
    'PASS': 'ПРОПУСК',
    'BLASTER  🔫': 'БЛАСТЕР  🔫',
    'Who do you want to use the blaster on?: ': 'На кого вы хотите использовать бластер?: ',
    'Don\'t write your name!!!': 'Не пишите свое имя!!!',
    'This player is out. Choose another one.': 'Этот игрок выбыл. Выберите другого.',
    'NO': 'НЕТ',
    'GAME PASS  🦘': 'ПРОПУСК НА ИГРУ  🦘',
    'REPLACEMENT  🦝': 'ЗАМЕНА  🦝',
    'There are no suitable cities': 'Подходящих городов нет',
    'You don\'t get anything because you took the last place.': 'Вы ничего не получаете, т.к вы заняли последнее место.',
    'Since you didn\'t use any abilities, you get double points': 'Поскольку вы не использовали никаких способностей, вы получаете двойные очки'
             }


entranslate={j: i for i, j in rutranslate.items()}


def translator(word, language):
    match language:
        case 'en':
            return word
        case 'en1':
            if word not in entranslate:
                return 'Error!!!'
            return entranslate[word]
        case 'ru':
            if word not in rutranslate:
                return word
            return rutranslate[word]
        case _:
            return '???'