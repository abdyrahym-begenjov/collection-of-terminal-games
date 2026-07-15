from translator import *
from random import choice

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
        print(f'[{obj.name}]')
        while True:
            if obj.gp==True:
                print(translator('PASS', lang))
                obj.gp=False
                break
            if word[-1] in ('ъ', 'ы', 'ь'):
                word=word[:-1]
            city=word
            print(word)
            word=input(f'{translator('You have', lang)} {obj.hearts} {translator('❤️ . Enter the word or ability: ', lang)}')
            word=word.title().strip()   
            if word=='':
                print(translator('You must enter the word!!!', lang))
                word=city
            elif word=='Blaster' or word=='Бластер':
                if obj.blaster==True:
                    while obj.blaster:
                        print(translator('BLASTER  🔫', lang))
                        da_blin=input(translator('Who do you want to use the blaster on?: ', lang))
                        if da_blin==obj.name:
                            print(translator('Don\'t write your name!!!', lang))
                        elif da_blin in [i.name for i in result1]:
                            for i in result1:
                                if da_blin==i.name:
                                    if i.hearts==0:
                                        print(translator('This player is out. Choose another one.', lang))
                                    else:
                                        print(f'{da_blin} 🔫 {obj.name}')
                                        i.hearts-=1
                                        if i.hearts==0:
                                            print('-'*125)
                                            print(f'[{i.name}]')
                                            print(translator('You are eliminated from the game!!!', lang))
                                            if losers==[]:
                                                print(translator('You don\'t get anything because you took the last place.', lang))
                                                i.points=0
                                            else:
                                                print(f'{translator('You received', lang)} {i.points} {translator('points.', lang)}')
                                            print('-'*125)
                                            print(f'[{obj.name}]')
                                            i.out=True
                                            losers.append(i.name)
                                        obj.blaster=False
                                        break
                        else:
                            print(translator('Error!!!', lang))
                else:
                    print(translator('NO', lang))
                word=city
            elif word=='Game Pass' or word=='Пропуск':
                if obj.game_pass==True:
                    print(translator('GAME PASS  🦘', lang))
                    obj.gp=True
                    obj.game_pass=False
                else:
                    print(translator('NO', lang))
                word=city
            elif word=='Replacement' or word=='Замена':
                if obj.replacement==True:
                    print(translator('REPLACEMENT  🦝', lang))
                    while True:
                        letter=city[-1].upper()
                        new_list=[i for i in cities_list if i.startswith(letter) and i not in cities_set]
                        if new_list==[]:
                            print(translator('There are no suitable cities', lang))
                        else:
                            city1=city
                            city=choice(new_list)
                            print(f'{city1} --> {city}')
                        obj.replacement=False
                        break
                else:
                    print(translator('NO', lang))
                word=city
            elif word in cities_set:
                print(translator('This word has already been used.', lang))
                word=city
            elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
                obj.points+=1
                cities_set.add(word)
                break
            else:
                print(translator('Error!!!', lang))
                obj.hearts-=1
                word=city
                break
        print(f'{translator('Points:', lang)} {obj.points}')
        if obj.points>=max_points:
            print(translator('You have received the maximum points', lang))
            print(translator('You are WINNER!!!', lang))
        if obj.hearts<=0:
            print(translator('You are eliminated from the game!!!', lang))
            if losers==[]:
                print(translator('You don\'t get anything because you took the last place.', lang))
                obj.points=0
            else:
                print(f'{translator('You received', lang)} {obj.points} {translator('points.', lang)}')
            obj.out=True
            losers.append(obj.name)
        print('-'*125)
        spisok2_result=(obj.points, obj.out, obj.hearts, word, cities_set, losers, have_winner)
    else:
        spisok2_result=(obj.points, obj.out, obj.hearts, word, cities_set, losers, have_winner)
    return spisok2_result