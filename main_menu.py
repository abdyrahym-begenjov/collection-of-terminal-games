from translator import *
from common_utils import *
from the_cities_game import *
from time import sleep
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
    print(Style.BRIGHT+translator('COLLECTION OF TERMINAL GAMES', lang))
    super_print(['Creator: Abdyrahym Begenjov', 10*' ','(GitHub: abdyrahym-begenjov)'], lang)
    super_print(['The Cities Game', 6*' ', 'Settings', 6*' ','Exit'], lang)
    choose_game=super_input('Choose a game or parameter: ', lang)
    choose_game=new_word(choose_game, lang)
    match choose_game:
        case 'The Cities Game':
            super_print('Loading...', lang)
            sleep(2)
            clear_screen()
            the_cities_game(base, data)
            clear_screen()
        case 'Settings':
            clear_screen()
            while True:
                super_print(['Name:', data['name']], lang)
                super_print(['Language:', data['language']], lang)
                change=super_input('Do you want to change parameters (Enter \"Name\" or \"Language\")?: ', lang)
                change=new_word(change, lang)
                match change:
                    case 'Name':
                        name=enter_name(data, base, lang)
                        clear_screen()
                    case 'Language':
                        lang=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()
        case 'Exit':
            clear_screen()
            exit_confirm=super_input('Do you want to exit (\"Yes\" or \"No\")?: ', lang)
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                super_print('Goodbye!!!', lang)
                super_input('Enter to exit: ', lang)
                break
        case _:
            clear_screen()