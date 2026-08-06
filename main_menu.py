from translator import *
from common_utils import *
from the_cities_game import *
from rsp import *
from hangman import *
from snakes_and_ladders import *
from colorama import init, Style

init(autoreset=True)

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

while True:
    return_cursor()
    super_print('COLLECTION OF TERMINAL GAMES', lang, 'White', Style.BRIGHT)
    super_print(['Creator: Abdyrahym Begenjov', 10*' ','(GitHub: abdyrahym-begenjov)'], lang)
    super_print('The Cities Game', lang)
    super_print('Rock, Scissors, Paper', lang)
    super_print('Hangman', lang)
    super_print('Snakes and Ladders', lang)
    super_print('Settings', lang)
    super_print('Exit', lang)
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

        case 'Settings':
            name, lang=settings(data, base, name, lang)
            
        case 'Exit':
            if exit_to_game(lang)=='No':
                clear_screen()
            else:
                super_print('Goodbye!!!', lang)
                super_input('Enter to exit: ', lang)
                break
        case _:
            clear_screen()