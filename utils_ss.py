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
        name=input(f'[{p[0]}] {translator('Enter name: ', lang)}')
        if name in lst1:
            print(translator('This name is already taken', lang))
        elif len(name)>16:
            print(translator('The name must not exceed 16 characters', lang))
        else:
            if name=='':
                name=c[0]
                c.pop(0)
            p.pop(0)
            break
    if name not in base['Snakes and Ladders']:
        if name.startswith('КОМПЬЮТЕР'):
            if translator(name, 'en1') in base:
                pass
            else:
                base['Snakes and Ladders'][translator(name, 'en1')]=0
        elif name.startswith('COMPUTER'):
            base['Snakes and Ladders'][name]=0
        else:
            base['The Cities Game'][name]=[0, 0]
            base['Rock, Scissors, Paper'][name]=[0, 0]
            base['Hangman'][name]=[0, 0]
            base['Snakes and Ladders'][name]=0
        pywrite('base.json', base)
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
            print(translator('Moment of Truth 🥁', lang))
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
        parameters=input(translator('Enter the parameter of game: ', lang))
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
                print(translator('Error!!!', lang))
    return parameters

def draw_leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=list(base['Snakes and Ladders'].items())
    base.sort(key=lambda x: x[1], reverse=True)
    base=dict(base)

    line1=f'|{translator('NAME |', lang):>18} {translator('POINTS', lang):<16}|'
    line='-'*len(line1)
    print(line)
    print(line1)
    print(line)

    for i, j in base.items():
        name=translator(i, lang) if i.startswith('COMPUTER') else i
        a=str(j)
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}|'
        print(line2)
        print(line)

def brosok(obj, base, lang, parameters, result1, final_num, points_list, w, Human, Computer):
    if len(parameters)==6:
        parameter, snakes, lsnakes, ladders, lladders, ssnake=parameters
    else:
        parameter, snakes, lsnakes, ladders, lladders=parameters
        ssnake=[100]
    isdouble=False
    isteleportation=False
    if obj.status==5 and obj.play!=False:
        if isinstance(obj, Human):
            while True:
                enter=input(f'[{obj.name}] {translator('Enter: ', lang)}')
                enter=enter.lower().strip()
                if lang=='ru':
                    enter=translator(enter, 'en1')
                match enter:
                    case 'teleport':
                        if obj.money_teleport==0:
                            print(translator('NO', lang))
                            isteleportation=False
                        else:
                            while True:
                                print(translator('TELEPORTATION 🌀', lang))
                                da_blin=input(translator('Choose player for teleportation: ', lang))
                                if da_blin==obj.name:
                                    print(translator('Don\'t write your name!!!', lang))
                                elif da_blin in [i.name for i in result1]:
                                    print(f'{obj.name} --> {da_blin}')
                                    for i in result1:
                                        if da_blin==i.name:
                                            obj.level, i.level=obj.teleport(i)
                                    break
                                else:
                                    print(translator('Error!!!', lang))
                            isteleportation=True
                        break
                    case 'double':
                        if obj.money_double==0:
                            print(translator('NO', lang))
                            isdouble=False
                        else:
                            print(translator('DOUBLE ✖️', lang))
                            obj.money_double=0
                            obj.moneys-=1
                            isdouble=True
                    case 'rocket':
                        if obj.money_rocket==0:
                            print(translator('NO', lang))
                        elif obj.level+10>=parameter:
                            print(translator('NO', lang))
                        else:
                            print(translator('ROCKET   +10 🚀', lang))
                            obj.level=obj.rocket()
                    case 'ice':
                        if obj.money_ice==0:
                            print(translator('NO', lang))
                        else:
                            while True:
                                print(translator('ICE 🧊', lang))
                                da_blin=input(translator('Choose player to freeze: ', lang))
                                if da_blin==obj.name:
                                    print(translator('Don\'t write your name!!!', lang))
                                elif da_blin in [i.name for i in result1]:
                                    print(f'{translator('ICE:', lang)} {da_blin}')
                                    for i in result1:
                                        if da_blin==i.name:
                                            i.play=ice(i)
                                    obj.money_ice=0
                                    obj.moneys-=1
                                    break
                                else:
                                    print(translator('Error!!!', lang))
                    case _:
                        break
        if isteleportation==False:
            if isinstance(obj, Computer):
                print(f'[{obj.name}] {translator('Generate: ', lang)}')
            num=randint(1, 6)
            if isdouble==True:
                print(f'{num}x2')
                num=double(num)
            print(f'{num}')
            obj.level+=num
            if obj.level==parameter:
                print(obj.level)
                obj.status=final_num[0]
                print(w[0])
                final_num.pop(0)
                w.pop(0)
                point=points_list.pop(0)
                if isinstance(obj, Human) and obj.moneys==4:
                    print(translator('Since you didn\'t use any abilities, you get double points', lang))
                    point*=2
                if obj.name.startswith('КОМПЬЮТЕР'):
                    base['Snakes and Ladders'][translator(obj.name, 'en1')]+=point
                else:
                    base['Snakes and Ladders'][obj.name]+=point
                pywrite('base.json', base)
            elif obj.level>parameter:
                print(translator('Number is bigger than parameter', lang))
                obj.level-=num
                print(obj.level)
            elif obj.level in snakes:
                print('🐍')
                obj.level-=6
                print(obj.level)
            elif obj.level in lsnakes:
                print('🐍🐍')
                obj.level-=12
                print(obj.level)
            elif obj.level in ssnake:
                print(f'{translator('Dangerous', lang)} 🐍')
                obj.level-=60
                print(obj.level)
            elif obj.level in ladders:
                print('🪜')
                obj.level+=6
                print(obj.level)
            elif obj.level in lladders:
                print('🪜🪜')
                obj.level+=12
                print(obj.level)
            else:
                print(obj.level)
        else:
            print(obj.level)
        spisok2_result=(obj.level, obj.status)
    elif obj.play==False:
        print(f'{obj.name} {translator('is frozen!', lang)}')
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result