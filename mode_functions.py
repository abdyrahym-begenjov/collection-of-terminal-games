from random import choice
from translator import *
from utils import *
from play import *
from propython import pywrite

def mode_infinity(name, cities_list, base, lang):
    start=input(translator('Enter to start game: ', lang))
    print(translator('Loading...', lang))
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
            print(translator('You are ABSOLUTE CHAMPION!!!', lang))
            print(f'{translator('You received', lang)} {points} {translator('points.', lang)}')
            print(star(points, lang))
            break
        if hearts!=0:
            print(f'{number}) {word}')
            word=input(f'{translator('You have', lang)} {hearts} {translator('❤️ . Enter the word: ', lang)}')
            word=word.title().strip()
        if hearts<=0:
            print(translator('Game Over!!!', lang))
            print(f'{translator('You received', lang)} {points} {translator('points.', lang)}')
            print(star(points, lang))
            break    
        elif word=='':
            print(translator('You must enter the word!!!', lang))
            word=city
        elif word in cities_set:
            print(translator('This word has already been used.', lang))
            word=city
        elif word[0]==city[-1].upper() and word in cities_list and word not in cities_set:
            number+=1
            points+=1
            cities_set.add(word)
        else:
            print(translator('Error!!!', lang))
            hearts-=1
            word=city
            
    if base[name][0]<points:
        print(translator('You\'ve broken a new highscore!!!', lang))
        base[name][0]=points
        pywrite('base.json', base)

def mode_party(name, cities_list, base, lang):
    p=[translator('Player 2', lang), translator('Player 3', lang), translator('Player 4', lang)]
    lst1=[name]
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
    max_points=choose_parameter(lang)
    clear_screen()
    for _ in range(game_count-1):
        lst1.append(game(p, lst1, base, lang))
                
    result1, new_lst=selection_of_order(lst1, game_count, lang, Player)
    for n, i in enumerate(result1, 1):
        print(f'{n}) {i.name}')
                
    start=input(translator('Enter to start game: ', lang))
    print(translator('Loading...', lang))
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
                print(f'[{winner.name}]')
                print(translator('Since you didn\'t use any abilities, you get double points', lang))
                winner.points*=2
                print('-'*125)
            if game_count==2:
                print(f'1) {spisok1[0]} - {translator('WINNER', lang)}  😎🏆. {translator('Points:', lang)} {winner.points}')
                print(f'2) {spisok1[1]} - {translator('LOSER', lang)}  😫. {translator('Points:', lang)} {spisok2[1]}')
                break
            elif game_count==3:
                print(f'1) {spisok1[0]} - {translator('WINNER', lang)}  😎🏆. {translator('Points:', lang)} {winner.points}')
                print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)}  😀. {translator('Points:', lang)} {spisok2[1]}')
                print(f'3) {spisok1[2]} - {translator('LOSER', lang)}  😫. {translator('Points:', lang)} {spisok2[2]}')
                break
            elif game_count==4:
                print(f'1) {spisok1[0]} - {translator('WINNER', lang)}  😎🏆. {translator('Points:', lang)} {winner.points}')
                print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)}  😀. {translator('Points:', lang)} {spisok2[1]}')
                print(f'3) {spisok1[2]} - {translator('BRONZE MEDALIST', lang)}  😐. {translator('Points:', lang)} {spisok2[2]}')
                print(f'4) {spisok1[3]} - {translator('LOSER', lang)}  😫. {translator('Points:', lang)} {spisok2[3]}')
                break
    for player in result1:
        base[player.name][1]+=int(player.points)
    pywrite('base.json', base)