from translator import *
from common_utils import *
from the_cities_game import *
from time import sleep

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
    print(translator('COLLECTION OF TERMINAL GAMES', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(f'{translator('The Cities Game', lang)}        {translator('Settings', lang)}       {translator('Exit', lang)}')
    choose_game=input(translator('Choose a game or parameter: ', lang))
    choose_game=new_word(choose_game, lang)
    match choose_game:
        case 'The Cities Game':
            print(translator('Loading...', lang))
            sleep(2)
            clear_screen()
            the_cities_game(base, data)
            clear_screen()
        case 'Settings':
            clear_screen()
            while True:
                print(f'{translator("Name", lang)}: {data['name']}')
                print(f'{translator("Language", lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
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
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()