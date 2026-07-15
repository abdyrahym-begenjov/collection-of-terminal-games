from propython import *
from translator import *
from subprocess import run
from platform import system
from random import randint
from time import sleep

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
    clear_screen()
    while True:
        print('English |  Русский')
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        match chosen_language:
            case 'Русский':
                lang='ru'
                cities_list=pyread('goroda.json')
                break
            case 'English':
                lang='en'
                cities_list=pyread('cities.json')
                break
            case _:
                clear_screen()
    
    data['language']=lang
    data['cities']=cities_list
    pywrite('data.json', data)
    return lang

def enter_name(data, base, lang):
    clear_screen()
    while True:
        name=input(translator('Enter your name: ', lang))
        name=name.strip()
        if name=='':
            clear_screen()
            print(translator('Error!!!', lang))
        elif len(name)>16:
            clear_screen()
            print(translator('The name must not exceed 16 characters', lang))
        else:
            data['name']=name
            pywrite('data.json', data)
            if name not in base:
                base[name]=[0, 0]
                pywrite('base.json', base)
            return name

def game(p, lst1, base, lang):
    while True:
        name=input(f'[{p[0]}] {translator('Enter name: ', lang)}')
        name=name.strip()
        if name=='':
            print(translator('Error!!!', lang))
        elif len(name)>16:
            print(translator('The name must not exceed 16 characters', lang))
        elif name in lst1:
            print(translator('This name is already taken', lang))
        else:
            if name not in base:
                base[name]=[0, 0]
            p.pop(0)
            break
    return name

def selection_of_order(lst1, game_count, lang, Player):
    while True:
        lst=[]
        for i in lst1:
            move=randint(1, 6)
            lst.append((i, move))
        lst.sort(key=lambda x: x[1], reverse=True)    
        result=list(map(lambda x: x[1], lst))
        nr, r=[], []
        for i in result:
            if i not in nr:
                nr.append(i)
            else:
                r.append(i)
        if r==[]:
            print(translator('Moment of Truth  🥁', lang))
            match game_count:
                case 2:
                    sleep(2)
                case 3:
                    sleep(4)
                case 4:
                    sleep(6)
            clear_screen()
            result=[f'{i}: {c}' for i, c in lst]
            text=', '.join(result)
            print(text)
            break
        else:
            continue

    new_lst=[i[0] for i in lst]
    result1=[Player(i) for i in new_lst]
    return result1, new_lst

def choose_parameter(lang):
    while True:
        print(translator('Parameters of game: Easy (10), Normal (20), Hard (30)', lang))
        parameter=input(translator('Enter the parameter of game: ', lang))
        parameter=new_word(parameter, lang)
        match parameter:
            case 'Easy':
                max_points=10
                break
            case 'Normal':
                max_points=20
                break
            case 'Hard':
                max_points=30
                break
            case _:
                clear_screen()
    return max_points

def star(points, lang):
    match points:
        case n if n>=60:
            return translator('Absolute Champion!!!  🏆', lang)
        case n if n>=50:
            return '⭐⭐⭐⭐⭐'
        case n if n>=40:
            return '⭐⭐⭐⭐'
        case n if n>=30:
            return '⭐⭐⭐'
        case n if n>=20:
            return '⭐⭐'
        case n if n>=10:
            return '⭐'
        case _:
            return translator('Loser!!!', lang)

def draw_leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=list(base.items())
    base.sort(key=lambda x: x[1][0]+x[1][1], reverse=True)
    base=dict(base)

    lst=['Infinity', 'Party', 'Overall Result']
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

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word