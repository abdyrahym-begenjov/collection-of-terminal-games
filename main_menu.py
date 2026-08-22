from translator import *
from common_utils import *
from the_cities_game import *
from rsp import *
from hangman import *
from snakes_and_ladders import *
from quiz import *
from colorama import init, Style

init(autoreset=True)

while True:
    data=pyread('data.json')
    base=pyread('base.json')

    name=data['name']
    lang=data['language']

    if lang=='':
        lang=enter_lang(data)
        clear_screen()

    if name=='':
        name=enter_name(data, base, lang)
        clear_screen()
        return_cursor()

    super_print('COLLECTION OF TERMINAL GAMES', lang, 'White', Style.BRIGHT)
    super_print(['Creator: Abdyrahym Begenjov', 45*' ','(GitHub: abdyrahym-begenjov)'], lang)
    print('-'*125)
    super_print(['🟩🟩🟩🟩🟩', ' '*8, '⬜⬜⬜⬜⬜'], lang)
    super_print(['🟩⬛🟩⬛🟩', ' '*8, '⬜⬛⬜⬛⬜', ' '*45,'The Cities Game'], lang, 'Blue')
    super_print(['🟩🟩🟩🟩🟩', ' '*8, '⬜⬜⬜⬜⬜', ' '*45, 'Rock, Scissors, Paper'], lang, 'Blue')
    super_print(['🟩🟩🟩🟩🟩', ' '*8, '⬜⬛⬜⬛⬜', ' '*45, 'Hangman'], lang, 'Blue')
    super_print([' '*3, '🟩', ' '*12, '⬜⬜⬜⬜⬜', ' '*45, 'Snakes and Ladders'], lang, 'Blue')
    super_print([' '*3, '🟩', ' '*12, '🟩🟩🟩🟩🟩', ' '*45, 'Quiz'], lang, 'Blue')
    super_print([' '*3, '🟩', ' '*20, '🟩', ' '*45, 'Settings'], lang, 'Dark Grey')
    super_print([' '*3, '🟩', ' '*20, '🟩', ' '*45, 'Help'], lang, 'Cyan')
    super_print([' '*3, '🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩', ' '*45, 'Exit'], lang, 'Light Red')
    print('-'*125)
    choose_game=super_input('Choose a game or parameter: ', lang)
    choose_game=new_word(choose_game, lang)
    match choose_game:
        case 'The Cities Game':
            func_loading(lang)
            the_cities_game(base, data)
            clear_screen()

        case 'Rock, Scissors, Paper':
            func_loading(lang)
            rsp(base, data)
            clear_screen()
        
        case 'Hangman':
            func_loading(lang)
            hangman(base, data)
            clear_screen()
        
        case 'Snakes And Ladders':
            func_loading(lang)
            snakes_and_ladders(base, data)
            clear_screen()

        case 'Quiz':
            func_loading(lang)
            quiz(base, data)
            clear_screen()

        case 'Settings':
            name, lang=settings(data, base, name, lang)
        
        case 'Help':
            clear_screen()
            if lang=='ru':
                information=pyread('info_ru.txt')
            else:
                information=pyread('info_en.txt')
            super_print(information, lang)
            exit_to_mode(lang)
            
        case 'Exit':
            if exit_to_game(lang)=='Yes':
                super_print('Goodbye!!!', lang)
                super_input('Enter to exit: ', lang)
                break
            else:
                clear_screen()
        case _:
            clear_screen()