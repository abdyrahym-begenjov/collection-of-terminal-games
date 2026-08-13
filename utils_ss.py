from common_utils import *
from translator import *
from random import randint
from time import sleep

class Player:
    def __init__(self, name):
        self.name=name
        self.level=0
        self.status=5
        self.play=True

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.money_ice=1
        self.money_rocket=1
        self.money_teleport=1
        self.money_double=1
        self.moneys=4
    def teleport(self, obj1):
        result=self.level
        self.level=obj1.level
        obj1.level=result
        self.money_teleport=0
        self.moneys-=1
        return self.level, obj1.level
    def rocket(self):
        self.level+=10
        self.money_rocket=0
        self.moneys-=1
        return self.level

class Computer(Player):
    pass

def ice(obj):
    obj.play=False
    return obj.play
def double(num):
    return num*2

def game(p, c, lst1, base, lang):
    while True:
        name=super_input([f'[{p[0]}]', 'Enter name: '], lang, 'Yellow')
        name=name.strip().title()
        if name in lst1:
            super_print('This name is already taken', lang, 'Red')
        elif name in game_system_words:
            super_print('Don\'t write a word that is in the game system.', lang, 'Red')
        elif len(name)>16:
            super_print('The name must not exceed 16 characters', lang, 'Red')
        else:
            if name=='':
                name=c[0]
                c.pop(0)
            p.pop(0)
            break
    if name not in base['Snakes and Ladders'] and name.startswith(('COMPUTER', 'КОМПЬЮТЕР')):
        if name.startswith('КОМПЬЮТЕР'):
            if translator(name, 'en1') in base:
                pass
            else:
                base['Snakes and Ladders'][translator(name, 'en1')]=0
        elif name.startswith('COMPUTER'):
            base['Snakes and Ladders'][name]=0
    fill_base(name, base, lang)
    return name

def selection_of_order(lst1, game_count, lang, Computer, Human):
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
            delete_cursor()
            super_print('Moment of Truth 🥁', lang, 'Dark Grey')
            match game_count:
                case 2:
                    sleep(2)
                case 3:
                    sleep(4)
                case 4:
                    sleep(6)
            clear_screen()
            return_cursor()
            result=[f'{i}: {c}' for i, c in lst]
            text=', '.join(result)
            print(text)
            break
        else:
            continue

    new_lst=list(map(lambda x: x[0], lst))
    result1=[]
    for i in new_lst:
        if i in [translator('COMPUTER1', lang), translator('COMPUTER2', lang), translator('COMPUTER3', lang)]:
            result1.append(Computer(i))
        else:
            result1.append(Human(i))
    return result1

def selection_of_parameters(lang):
    while True:
        parameters=super_input('Enter the parameter of game: ', lang, 'Dark Grey')
        parameters=new_word(parameters, lang)
        match parameters:
            case 'Easy':
                parameters=[50, [13, 31], [47], [8, 38], [22]]
                break
            case 'Normal':
                parameters=[75, [25, 36, 49], [73, 68], [20, 38, 57], [3, 12]]
                break
            case 'Hard':
                parameters=[100, [24, 64, 63, 62], [13, 49, 80], [4, 32, 70, 61], [15, 55, 87], [95]]
                break
            case _:
                super_print('Error!!!', lang, 'Red')
    return parameters

def draw_leaderboard(base, lang):
    super_print('LEADERBOARD:', lang)
    base=list(base['Snakes and Ladders'].items())
    base.sort(key=lambda x: x[1], reverse=True)
    max_value=base[0][1]
    min_value=base[-1][1]
    base=dict(base)

    line1=f'|{translator('NAME |', lang):>18} {translator('POINTS', lang):<16}|'
    line=(Style.BRIGHT+'-')*len(line1)
    super_print(line, lang, 'Cyan')
    super_print(line1, lang, 'Cyan', Style.BRIGHT)
    super_print(line, lang, 'Cyan')

    for i, j in base.items():
        name=translator(i, lang) if i.startswith('COMPUTER') else i
        a=str(j)
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}|'
        if j==max_value:
            super_print(line2, lang, 'Green')
            super_print(line, lang, 'Green')
        elif j==min_value:
            super_print(line2, lang, 'Red')
            super_print(line, lang, 'Red')
        else:
            super_print(line2, lang, 'Yellow')
            super_print(line, lang, 'Yellow')

def brosok(obj, base, lang, parameters, result1, final_num, points_list, w, Human, Computer):
    if len(parameters)==6:
        parameter, snakes, lsnakes, ladders, lladders, ssnake=parameters
    else:
        parameter, snakes, lsnakes, ladders, lladders=parameters
        ssnake=[100]
    isdouble=False
    isteleportation=False
    if obj.status==5 and obj.play!=False:
        print('-'*125)
        if isinstance(obj, Human):
            while True:
                enter=super_input([f'[{obj.name}]', 'Enter: '], lang, 'Light Blue')
                enter=enter.lower().strip()
                if lang=='ru':
                    enter=translator(enter, 'en1')
                match enter:
                    case 'teleport':
                        if obj.money_teleport==0:
                            super_print('NO', lang, 'Red')
                            isteleportation=False
                        else:
                            while True:
                                super_print('TELEPORTATION 🌀', lang, 'Blue')
                                da_blin=super_input('Choose player for teleportation: ', lang, 'Blue')
                                if da_blin==obj.name:
                                    super_print('Don\'t write your name!!!', lang, 'Red')
                                elif da_blin in [i.name for i in result1]:
                                    super_print(f'{obj.name} --> {da_blin}', lang, 'Blue')
                                    for i in result1:
                                        if da_blin==i.name:
                                            obj.level, i.level=obj.teleport(i)
                                    break
                                else:
                                    super_print('Error!!!', lang, 'Red')
                            isteleportation=True
                        break
                    case 'double':
                        if obj.money_double==0:
                            super_print('NO', lang, 'Red')
                            isdouble=False
                        else:
                            super_print('DOUBLE ✖️', lang, 'Blue')
                            obj.money_double=0
                            obj.moneys-=1
                            isdouble=True
                    case 'rocket':
                        if obj.money_rocket==0:
                            super_print('NO', lang, 'Red')
                        elif obj.level+10>=parameter:
                            super_print('You cannot use the \"Rocket\" as this action will take you beyond the finish line!!!', lang, 'Red')
                        else:
                            super_print('ROCKET   +10 🚀', lang, 'Blue')
                            obj.level=obj.rocket()
                    case 'ice':
                        if obj.money_ice==0:
                            super_print('NO', lang, 'Red')
                        else:
                            while True:
                                super_print('ICE 🧊', lang, 'Blue')
                                da_blin=super_input('Choose player to freeze: ', lang, 'Blue')
                                if da_blin==obj.name:
                                    super_print('Don\'t write your name!!!', lang, 'Red')
                                elif da_blin in [i.name for i in result1]:
                                    super_print(['ICE:', da_blin], lang, 'Blue')
                                    for i in result1:
                                        if da_blin==i.name:
                                            i.play=ice(i)
                                    obj.money_ice=0
                                    obj.moneys-=1
                                    break
                                else:
                                    super_print('Error!!!', lang, 'Red')
                    case _:
                        break
        if isteleportation==False:
            if isinstance(obj, Computer):
                super_print([f'[{obj.name}] ', 'Generate: '], lang, 'Dark Grey')
            num=randint(1, 6)
            if isdouble==True:
                super_print(['Steps:', f'{num}x2'], lang, 'Magenta')
                num=double(num)
            super_print(['Steps:', str(num)], lang)
            obj.level+=num
            if obj.level==parameter:
                super_print(['Position:', str(obj.level)], lang, 'Yellow')
                obj.status=final_num[0]
                super_print(w[0], lang, 'Green')
                final_num.pop(0)
                first_winner=w.pop(0)
                point=points_list.pop(0)
                if isinstance(obj, Human) and obj.moneys==4 and first_winner=='First Winner':
                    super_print('Since you didn\'t use any abilities, you get double points.', lang, 'Green')
                    point*=2
                if obj.name.startswith('КОМПЬЮТЕР'):
                    base['Snakes and Ladders'][translator(obj.name, 'en1')]+=point
                else:
                    base['Snakes and Ladders'][obj.name]+=point
                pywrite('base.json', base)
            elif obj.level>parameter:
                super_print('Number is bigger than parameter', lang, 'Red')
                obj.level-=num
                super_print(['Position:', str(obj.level)], lang, 'Yellow')
            elif obj.level in snakes:
                print('🐍')
                obj.level-=6
                super_print(['Position:', str(obj.level)], lang, 'Light Red')
            elif obj.level in lsnakes:
                print('🐍🐍')
                obj.level-=12
                super_print(['Position:', str(obj.level)], lang, 'Light Red')
            elif obj.level in ssnake:
                super_print(['Dangerous', ' 🐍'], lang, 'Light Red')
                obj.level-=60
                super_print(['Position:', str(obj.level)], lang, 'Light Red')
            elif obj.level in ladders:
                print('🪜')
                obj.level+=6
                super_print(['Position:', str(obj.level)], lang, 'Green')
            elif obj.level in lladders:
                print('🪜🪜')
                obj.level+=12
                super_print(['Position:', str(obj.level)], lang, 'Green')
            else:
                super_print(['Position:', str(obj.level)], lang, 'Yellow')
        else:
            super_print(['Position:', str(obj.level)], lang, 'Blue')
        spisok2_result=(obj.level, obj.status)
    elif obj.play==False:
        print('-'*125)
        super_print([obj.name, 'is frozen!'], lang, 'Blue')
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result