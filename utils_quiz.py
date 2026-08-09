from common_utils import *
from translator import *
from random import choice

def choose_parameter(lang):
    while True:
        print(translator('Parameters of game: Easy (15), Normal (25), Hard (40), Dangerous (40 with surprise)', lang))
        parameter=input(translator('Enter the parameter of game: ', lang))
        parameter=new_word(parameter, lang)
        match parameter:
            case 'Easy':
                nums_question=15
                seconds=45
                break
            case 'Normal':
                nums_question=25
                seconds=60
                break
            case 'Hard' | 'Dangerous':
                nums_question=40
                seconds=90
                break
            case _:
                print(translator('Error!!!', lang))
    return parameter, nums_question, seconds

def final_result(regular, irregular, number, lang, countdown):
    print(f'{translator('Time: ', lang)}{countdown}. {translator('Regular: ', lang)}{regular}  {translator('Irregular: ', lang)}{irregular}')
    if regular==number:
        print(translator('You Win!!!', lang))
        print('⭐'*3)
        final=True
        is_game_over=False
    elif (regular/number)*100>=70:
        print(translator('Good Work!!!', lang))
        print('⭐'*2)
        final=True
        is_game_over=False
    elif (regular/number)*100>50:
        print(translator('Weak, but still you\'re great!!!', lang))
        print('⭐')
        final=True
        is_game_over=False
    elif (regular/number)*100==50:
        print(translator('The final question to determine the outcome of the game.', lang))
        nums_question+=1
        final=False
        is_game_over=False
    else:
        print(translator('Game Over!!!', lang))
        print('💩')
        final=True
        is_game_over=True
    return final, is_game_over

def answer_question(lang, v, heart, countdown=None, seconds=None):
    while True:
        if countdown and seconds:
            answer=input(f'{translator('Time: ', lang)}{countdown}. {translator('Enter the variant of answer: ', lang)}')
        else:
            answer=input(f'{translator("You have", lang)} {heart} ❤️ . {translator('Enter the variant of answer: ', lang)}')
        answer=answer.upper().strip()
        if answer in v:
            break
        else:
            print(translator('You must enter the variant!!!', lang))
    if countdown:
        return answer, seconds
    else:
        return answer

def draw_leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=list(base['Quiz'].items())
    base.sort(key=lambda x: x[1][0]+x[1][1], reverse=True)
    base=dict(base)

    lst=['Timer', 'Infinity', 'Overall Result']
    lst=[translator(i, lang) for i in lst]
    lst=[f'{i.upper().strip():<16}|' for i in lst]
    lst=' '.join(lst)
    line1=f'|{translator('NAME |', lang):>18} {lst:<16}'
    line='-'*len(line1)
    print(line)
    print(line1)
    print(line)

    for i, j in base.items():
        name=i
        a=str(j[0])
        b=str(j[1])
        c=j[0]+j[1]
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}| {b:<16}| {c:<16}|'
        print(line2)
        print(line)

def choose_bomb(question, v):
    dict_variants={'Q': 0, v[0]: 1, v[1]: 2, v[2]: 3, v[3]: 4}
    old_question=question.copy()
    q=old_question[5]
    old_question.pop(5)
    old_question.pop(dict_variants[q])
    dict_variants={j: i for i, j in dict_variants.items()}
    old_question_index=[old_question.index(i) for i in old_question]
    bomb_list=[dict_variants[i] for i in old_question_index[1:4]]
    bomb=choice(bomb_list)
    return bomb