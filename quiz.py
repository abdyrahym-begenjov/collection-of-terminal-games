from random import choice
from time import time
from translator import translator
from utils_quiz import *

def quiz(base, data):
    while True:
        name=data['name']
        lang=data['language']
        lst=data['questions']
        v=data['variants']

        super_print(['Quiz', ' ❓'], lang, 'Cyan')
        match choose_mode(lang):
            case 'Game':
                while True:
                    super_print('Timer      Infinity', lang, 'Cyan')
                    mode_game=super_input('Choose a game mode: ', lang, 'Cyan')
                    mode_game=new_word(mode_game, lang)
                    if mode_game=='Timer' or mode_game=='Infinity':
                        break            

                points, regular, irregular, number, heart=0, 0, 0, 0, 3

                clear_screen()
                if mode_game=='Timer':
                    parameter, nums_question, seconds=choose_parameter(lang)

                func_loading(lang)
                super_print('Let\'s Go!!!', lang, 'Green', Style.BRIGHT)

                while True:
                    match mode_game:
                        case 'Timer':
                            mins, secs=divmod(seconds, 60)
                            countdown=f'{mins:02d}:{secs:02d}'
                            if nums_question==0:
                                final, is_game_over=final_result(regular, irregular, number, lang, countdown)
                                if final and is_game_over==False:
                                    seconds=mins*60+secs
                                    points=int(regular+(seconds/(irregular+1)))
                                    super_print(['Points: ', str(points)], lang, 'Yellow')
                                    base['Quiz'][name][0]+=points
                                    pywrite('base.json', base)
                                    break
                                elif is_game_over:
                                    break
                                else:
                                    continue
                            elif seconds<=0:
                                super_print('Time: 00:00. Game Over!!!', lang, 'Red')
                                break
                        case 'Infinity':
                            if lst==[]:
                                super_print('You are ABSOLUTE CHAMPION!!!', lang, 'Green')
                                base[name][1]=points
                                pywrite('base.json', base)
                                break
                            elif heart==0:
                                super_print('Game Over!!!', lang, 'Red')
                                print(f'{translator("Points: ", lang)}{points}')
                                if base['Quiz'][name][1]<points:
                                    super_print('You\'ve broken a new highscore!!!', lang, 'Green')
                                    base['Quiz'][name][1]=points
                                    pywrite('base.json', base)
                                break
                    number+=1
                    question=choice(lst)
                    super_print(f'{number}) {question[0]}', lang, 'Blue', Style.BRIGHT)
                    super_print(f'{v[0]}) {question[1]:<35} {" ":>35} {v[2]}) {question[3]}', lang, 'Light Blue')
                    super_print(f'{v[1]}) {question[2]:<35} {" ":>35} {v[3]}) {question[4]}', lang, 'Light Blue')
                    if mode_game=='Timer':
                        start=time()
                        answer, seconds=answer_question(lang, v, heart, countdown, seconds)
                        end=time()
                        seconds=seconds-int(end-start)
                    else:
                        answer=answer_question(lang, v, heart)
                    if answer==question[5]:
                        super_print('YES', lang, 'Green')
                        if mode_game=='Timer':
                            regular+=1
                            seconds+=5
                        else:
                            points+=1
                    else:
                        super_print('NO', lang, 'Light Red')
                        if mode_game=='Timer' and parameter=='Dangerous':
                            bomb=choose_bomb(question, v)
                            if answer==bomb:
                                super_print('💣 BOOM!!!', lang, 'Light Red')
                                seconds-=10
                        if mode_game=='Infinity':
                            heart-=1
                        else:
                            irregular+=1
                    if mode_game=='Timer':
                        nums_question-=1
                    lst.remove(question)

                exit_to_mode(lang)

            case 'Rules':
                if lang=='ru':
                    rules=pyread('ru_rules_quiz.txt')
                else:
                    rules=pyread('en_rules_quiz.txt')
                super_print(rules, lang)
                exit_to_mode(lang)

            case 'Highscores':
                draw_leaderboard(base, lang)
                exit_to_mode(lang)

            case 'Exit':
                break

            case _:
                clear_screen()