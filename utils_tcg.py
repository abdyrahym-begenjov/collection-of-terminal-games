from translator import *
from random import choice, randint
from common_utils import *
from time import sleep

def game(p, lst1, base, lang):
    while True:
        name=super_input(['[', p[0], ']', 'Enter name: '], lang, Fore.LIGHTYELLOW_EX)
        name=name.strip()
        if name=='':
            super_print('Error!!!', lang, Fore.RED)
        elif len(name)>16:
            super_print('The name must not exceed 16 characters', lang, Fore.RED)
        elif name in lst1:
            super_print('This name is already taken', lang, Fore.RED)
        else:
            if name not in base['The Cities Game']:
                base['The Cities Game'][name]=[0, 0]
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
            super_print('Moment of Truth  🥁', lang, Fore.LIGHTCYAN_EX)
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
        super_print('Parameters of game: Easy (10), Normal (20), Hard (30)', lang, Fore.LIGHTCYAN_EX)
        parameter=super_input('Enter the parameter of game: ', lang, Fore.LIGHTCYAN_EX)
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
    super_print('LEADERBOARD:', lang)
    base=list(base['The Cities Game'].items())
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

class Player:
    def __init__(self, name):
        self.name=name
        self.hearts=3
        self.points=0
        self.out=False
        self.blaster=True
        self.game_pass=True
        self.replacement=True
        self.gp=False

def play(obj, word, max_points, result1, cities_list, cities_set, losers, have_winner, lang):
    if obj.out==False:
        super_print(['[', obj.name, ']'], lang, Fore.LIGHTYELLOW_EX)
        while True:
            if obj.gp==True:
                super_print('PASS', lang, Fore.BLUE)
                obj.gp=False
                break
            if word[-1] in ('ъ', 'ы', 'ь'):
                word=word[:-1]
            city=word
            super_print(word, lang, Fore.LIGHTBLUE_EX)
            word=super_input(['You have', obj.hearts, '❤️ . Enter the word or ability: '], lang)
            word=word.title().strip()
            if word=='':
                super_print('You must enter the word!!!', lang, Fore.RED)
                word=city
            elif word=='Blaster' or word=='Бластер':
                if obj.blaster==True:
                    while obj.blaster:
                        super_print('BLASTER  🔫', lang, Fore.BLUE)
                        da_blin=super_input('Who do you want to use the blaster on?: ', lang, Fore.BLUE)
                        if da_blin==obj.name:
                            super_print('Don\'t write your name!!!', lang, Fore.RED)
                        elif da_blin in [i.name for i in result1]:
                            for i in result1:
                                if da_blin==i.name:
                                    if i.hearts==0:
                                        super_print('This player is out. Choose another one.', lang, Fore.RED)
                                    else:
                                        super_print([da_blin, '🔫', obj.name], lang, Fore.BLUE)
                                        i.hearts-=1
                                        if i.hearts==0:
                                            print('-'*125)
                                            super_print(f'[{i.name}]', lang, Fore.LIGHTYELLOW_EX)
                                            super_print('You are eliminated from the game!!!', lang, Fore.RED)
                                            if losers==[]:
                                                super_print('You don\'t get anything because you took the last place.', lang, Fore.RED)
                                                i.points=0
                                            else:
                                                super_print(['You received', i.points, 'points.'], lang, Fore.LIGHTBLUE_EX)
                                            print('-'*125)
                                            super_print(['[', obj.name, ']'], lang, Fore.LIGHTYELLOW_EX)
                                            i.out=True
                                            losers.append(i.name)
                                        obj.blaster=False
                                        break
                        else:
                            super_print('Error!!!', lang, Fore.RED)
                else:
                    super_print('NO', lang, Fore.RED)
                word=city
            elif word=='Game Pass' or word=='Пропуск':
                if obj.game_pass==True:
                    super_print('GAME PASS  🦘', lang, Fore.BLUE)
                    obj.gp=True
                    obj.game_pass=False
                else:
                    super_print('NO', lang, Fore.RED)
                word=city
            elif word=='Replacement' or word=='Замена':
                if obj.replacement==True:
                    super_print('REPLACEMENT  🦝', lang, Fore.BLUE)
                    while True:
                        letter=city[-1].upper()
                        new_list=[i for i in cities_list if i.startswith(letter) and i not in cities_set]
                        if new_list==[]:
                            super_print('There are no suitable cities', lang, Fore.RED)
                        else:
                            city1=city
                            city=choice(new_list)
                            super_print([city1, '-->', city], lang, Fore.BLUE)
                        obj.replacement=False
                        break
                else:
                    super_print('NO', lang, Fore.RED)
                word=city
            elif word in cities_set:
                super_print('This word has already been used.', lang, Fore.RED)
                word=city
            elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
                obj.points+=1
                cities_set.add(word)
                break
            else:
                super_print('Error!!!', lang, Fore.RED)
                obj.hearts-=1
                word=city
                break
        super_print(['Points:', obj.points], lang)
        if obj.points>=max_points:
            super_print('You have received the maximum points', lang, Fore.GREEN)
            super_print('You are WINNER!!!', lang, Fore.GREEN)
        if obj.hearts<=0:
            super_print('You are eliminated from the game!!!', lang, Fore.LIGHTRED_EX)
            if losers==[]:
                super_print('You don\'t get anything because you took the last place.', lang, Fore.LIGHTRED_EX)
                obj.points=0
            else:
                super_print(['You received', obj.points, 'points.'], lang, Fore.LIGHTBLUE_EX)
            obj.out=True
            losers.append(obj.name)
        print('-'*125)
        spisok2_result=(obj.points, obj.out, obj.hearts, word, cities_set, losers, have_winner)
    else:
        spisok2_result=(obj.points, obj.out, obj.hearts, word, cities_set, losers, have_winner)
    return spisok2_result

def mode_infinity(name, cities_list, base, lang):
    start=super_input('Enter to start game: ', lang, Fore.LIGHTCYAN_EX)
    super_print('Loading...', lang, Fore.LIGHTCYAN_EX)
    sleep(2)
    clear_screen()

    word=choice(cities_list)
    hearts=3
    points=0
    number=1
    cities_set=set()

    while True:
        if word[-1] in ('ъ', 'ы', 'ь'):
            word=word[:-1]
        city=word
        if len(cities_set)==len(cities_list):
            super_print('You are ABSOLUTE CHAMPION!!!', lang, Fore.GREEN)
            super_print(['You received', points, 'points.'], lang, Fore.LIGHTBLUE_EX)
            print(star(points, lang))
            break
        if hearts!=0:
            super_print([f'{number})', word], lang, Fore.LIGHTBLUE_EX)
            word=super_input(['You have', hearts, '❤️ . Enter the word: '], lang)
            word=word.title().strip()
        if hearts<=0:
            super_print('Game Over!!!', lang, Fore.LIGHTRED_EX)
            super_print(['You received', points, 'points.'], lang, Fore.LIGHTBLUE_EX)
            print(star(points, lang))
            break    
        elif word=='':
            super_print('You must enter the word!!!', lang, Fore.RED)
            word=city
        elif word in cities_set:
            super_print('This word has already been used.', lang, Fore.RED)
            word=city
        elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
            number+=1
            points+=1
            cities_set.add(word)
        else:
            super_print('Error!!!', lang, Fore.RED)
            hearts-=1
            word=city
            
    if base['The Cities Game'][name][0]<points:
        super_print('You\'ve broken a new highscore!!!', lang, Fore.GREEN)
        base['The Cities Game'][name][0]=points
        pywrite('base.json', base)

def mode_party(name, cities_list, base, lang):
    p=[translator('Player 2', lang), translator('Player 3', lang), translator('Player 4', lang)]
    lst1=[name]
    while True:
        game_count=super_input('Enter number of the players: ', lang, Fore.LIGHTCYAN_EX)
        if game_count in ('2', '3', '4'):
            try:
                game_count=int(game_count)
                break
            except ValueError:
                clear_screen()
        else:
            clear_screen()
    
    clear_screen()
    max_points=choose_parameter(lang)
    clear_screen()
    for _ in range(game_count-1):
        lst1.append(game(p, lst1, base, lang))
                
    result1, new_lst=selection_of_order(lst1, game_count, lang, Player)
    for n, i in enumerate(result1, 1):
        print(f'{n}) {i.name}')
                
    start=super_input('Enter to start game: ', lang, Fore.LIGHTCYAN_EX)
    super_print('Loading...', lang, Fore.LIGHTCYAN_EX)
    sleep(2)
    clear_screen()

    final=False
    city=choice(cities_list)
    cities_set=set()
    have_winner=False
    losers=[]

    while True:
        for player in result1:
            player.points, player.out, player.hearts, city, cities_set, losers, have_winner=play(player, city, max_points, result1, cities_list, cities_set, losers, have_winner, lang)
            if have_winner==True:
                final=have_winner
                break
        spisok=[]
        for player in result1:
            spisok.append((player.name, player.points, player))
        spisok.sort(key=lambda x: (x[1], new_lst.index(x[0])), reverse=True)
        spisok1=[i[0] for i in spisok]
        spisok2=[i[1] for i in spisok]
        if final==True or len(losers)==game_count-1:
            winner=spisok[0][2]
            winner.points+=max_points
            if winner.blaster==True and winner.replacement==True and winner.game_pass==True:
                super_print(['[', winner.name, ']'], lang, Fore.LIGHTYELLOW_EX)
                super_print('Since you didn\'t use any abilities, you get double points', lang, Fore.GREEN)
                winner.points*=2
                super_print('-'*125, lang, Fore.LIGHTBLUE_EX)
            if game_count==2:
                super_print(['1)', spisok1[0], '-', 'WINNER', ' 😎🏆.', 'Points:', winner.points], lang, Fore.GREEN)
                super_print(['2)', spisok1[1], '-', 'LOSER', ' 😫.', 'Points:', spisok2[1]], lang, Fore.LIGHTRED_EX)
                break
            elif game_count==3:
                super_print(['1)', spisok1[0], '-', 'WINNER', '😎🏆.', 'Points:', winner.points], lang, Fore.GREEN)
                super_print(['2)', spisok1[1], '-', 'ROUND-UP', ' 😀.', 'Points:', spisok2[1]], lang, Fore.YELLOW)
                super_print(['3)', spisok1[2], '-', 'LOSER', ' 😫.', 'Points:', spisok2[2]], lang, Fore.LIGHTRED_EX)
                break
            elif game_count==4:
                super_print(['1)', spisok1[0], '-', 'WINNER', '😎🏆.', 'Points:', winner.points], lang, Fore.GREEN)
                super_print(['2)', spisok1[1], '-', 'ROUND-UP', ' 😀.', 'Points:', spisok2[1]], lang, Fore.YELLOW)
                super_print(['3)', spisok1[2], '-', 'BRONZE MEDALIST', ' 😐.', 'Points:', spisok2[2]], lang, Fore.MAGENTA)
                super_print(['4)', spisok1[3], '-', 'LOSER', ' 😫.', 'Points:', spisok2[3]], lang, Fore.LIGHTRED_EX)
                break
    for player in result1:
        base['The Cities Game'][player.name][1]+=int(player.points)
    pywrite('base.json', base)