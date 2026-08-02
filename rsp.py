from random import choice
from time import sleep
from translator import *
from common_utils import *
from utils_rsp import *

def rsp(base, data):
    name=data['name']
    lang=data['language']

    while True:
        super_print('Rock, Scissors, Paper', lang, 'Cyan')
        match choose_mode(lang):
            case 'Game':
                while True:
                    num=super_input('How many wins are we playing to?: ', lang, 'Dark Grey')
                    try:
                        num=int(num)
                        if num<=0:
                            super_print('The number must not be less than or equal to zero!!!', lang, 'Red')
                        else:
                            break
                    except ValueError:
                        super_print('Error!!!', lang, 'Red')

                super_print('Loading...', lang, 'Dark Grey')
                sleep(2)
                clear_screen()

                words=[translator('Rock', lang), translator('Scissors', lang), translator('Paper', lang)]
                up=0
                cp=0

                while True:
                    user=super_input('Enter the word: ', lang)
                    user=new_word(user, lang)
                    computer=choice(words)
                    computer=new_word(computer, lang)
                    match user, computer:
                        case ('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock'):
                            cp+=1
                        case ('Paper', 'Rock') | ('Scissors', 'Paper') | ('Rock', 'Scissors'):
                            up+=1
                        case ('Rock', 'Rock') | ('Paper', 'Paper') | ('Scissors', 'Scissors'):
                            pass
                        case _:
                            super_print('Error!!!', lang, 'Red')
                            continue
                    super_print(['Computer:', computer], lang, 'Dark Grey')
                    super_print(['User:', up, 5*' ', 'Computer:', cp], lang, 'Light Blue')
                    if cp==num:
                        super_print('Computer wins', lang, 'Red')
                        super_print('Game Over!!!', lang, 'Red')
                        base['Rock, Scissors, Paper'][name][1]+=num
                        break
                    elif up==num:
                        super_print('You win!!!', lang, 'Green')
                        base['Rock, Scissors, Paper'][name][0]+=num
                        break
                pywrite('base.json', base)
                exit_to_mode(lang)

            case 'Rules':
                if lang=='ru':
                    rules=pyread('ru_rules_rsp.txt')
                else:
                    rules=pyread('en_rules_rsp.txt')
                super_print(rules, lang)
                exit_to_mode(lang)

            case 'Highscores':
                draw_leaderboard(base, lang)
                exit_to_mode(lang)

            case 'Exit':
                break
            case _:
                clear_screen()