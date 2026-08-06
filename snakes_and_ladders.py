from random import randint
from time import sleep
from translator import *
from utils_ss import *
from common_utils import *

def snakes_and_ladders(base, data):
    name=data['name']
    lang=data['language']

    while True:
        print(translator('Snakes and Ladders', lang))
        match choose_mode(lang):
            case 'Game':
                p=[translator('Player 2', lang), translator('Player 3', lang), translator('Player 4', lang)]
                c=[translator('COMPUTER1', lang), translator('COMPUTER2', lang), translator('COMPUTER3', lang)]
            
                while True:
                    game_count=input(translator('Enter number of the players: ', lang))
                    if game_count in ('2', '3', '4'):
                        try:
                            game_count=int(game_count)
                            break
                        except ValueError:
                            clear_screen()
                    else:
                        clear_screen()
                clear_screen()

                print(translator('Parameters of game: Easy (50), Normal (75), Hard (100)', lang))

                parameters=selection_of_parameters(lang)
                clear_screen()

                lst1=[name]

                for i in range(game_count-1):
                    x=game(p, c, lst1, base, lang)
                    lst1.append(x)

                result1=selection_of_order(lst1, game_count, lang, Computer, Human)

                for n, i in enumerate(result1, 1):
                    print(f'{n}) {i.name}')

                start1=input(translator('Enter to start game: ', lang))
                func_loading(lang)
                print(translator('Let\'s Go!!!', lang))
                w=[translator('First Winner', lang), translator('Second Winner', lang), translator('Third Winner', lang), translator('Forth Winner', lang)]
                points_list=[3, 2, 1, 0]
                final_num=[1, 2, 3, 4]

                while True:
                    for player in result1:
                        player.level, player.status=brosok(player, base, lang, parameters, result1, final_num, points_list, w, Human, Computer)
                        player.play=True
                    spisok=[]
                    for player in result1:
                        spisok.append((player.name, player.level, player.status))
                    spisok.sort(key=lambda x: x[2], reverse=False)
                    spisok1=list(map(lambda x: x[0], spisok))
                    spisok2=list(map(lambda x: x[2], spisok))
                    if 1 in spisok2 and game_count==2:
                        print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆')
                        print(f'2) {spisok1[1]} - {translator('LOSER', lang)} 😫')
                        break
                    elif 1 in spisok2 and 2 in spisok2 and game_count==3:
                        print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆')
                        print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)} 😀')
                        print(f'3) {spisok1[2]} - {translator('LOSER', lang)} 😫')
                        break
                    elif 1 in spisok2 and 2 in spisok2 and 3 in spisok2 and game_count==4:
                        print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆')
                        print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)} 😀')
                        print(f'3) {spisok1[2]} - {translator('BRONZE MEDALIST', lang)} 😐')
                        print(f'4) {spisok1[3]} - {translator('LOSER', lang)} 😫')
                        break

                exit_to_mode(lang)

            case 'Rules':
                if lang=='ru':
                    rules=pyread('ru_rules_ss.txt')
                else:
                    rules=pyread('en_rules_ss.txt')
                print(rules)
                exit_to_mode(lang)

            case 'Highscores':
                draw_leaderboard(base, lang)
                exit_to_mode(lang)

            case 'Exit':
                break
            case _:
                clear_screen()