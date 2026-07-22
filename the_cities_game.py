from translator import *
from common_utils import *
from utils_tcg import *

def the_cities_game(base, data):
    while True:
        name=data['name']
        lang=data['language']
        cities_list=data['cities']

        super_print(['The Cities Game', 2*' ', '🏙️'], lang, Fore.CYAN)
        super_print('Game      Rules      Highscores      Exit', lang, Fore.CYAN)
        mode=super_input('Choose a game mode: ', lang, Fore.CYAN)
        mode=new_word(mode, lang)
        clear_screen()
        match mode:
            case 'Game':
                while True:
                    super_print('Infinity          Party', lang, Fore.LIGHTCYAN_EX)
                    mode_game=super_input('Choose a game mode: ', lang, Fore.LIGHTCYAN_EX)
                    mode_game=new_word(mode_game, lang)
                    if mode_game=='Infinity' or mode_game=='Party':
                        break
                    else:
                        clear_screen()
                clear_screen()

                if mode_game=='Party':
                    mode_party(name, cities_list, base, lang)       
                else:
                    mode_infinity(name, cities_list, base, lang)

                end=super_input('Enter to exit mode: ', lang)
                clear_screen()
    
            case 'Rules':
                if lang=='ru':
                    rules=pyread('ru_rules_tcg.txt')
                else:
                    rules=pyread('en_rules_tcg.txt')
                super_print(rules, lang)
                end=super_input('Enter to exit mode: ', lang)
                clear_screen()

            case 'Highscores':
                draw_leaderboard(base, lang)
                end=super_input('Enter to exit mode: ', lang)
                clear_screen()

            case 'Exit':
                exit_confirm=super_input('Do you want to exit (\"Yes\" or \"No\"): ', lang)
                exit_confirm=new_word(exit_confirm, lang)
                if exit_confirm=='No':
                    clear_screen()
                else:
                    super_input('Goodbye!!!', lang)
                    super_input('Enter to exit: ', lang)
                    break
            case _:
                clear_screen()