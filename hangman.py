from utils_hangman import *
from random import choice
from common_utils import *
from translator import *

def hangman(base, data):
    while True:
        name=data['name']
        lang=data['language']
        words_list=data['words']
    
        super_print('Hangman', lang, 'Cyan')
        match choose_mode(lang):
            case 'Game':
                start=super_input('Enter to start game: ', lang, 'Dark Grey')
                func_loading(lang)

                point=0 
                word=choice(words_list)
                word=word.lower()
                task='_ '*len(word)
                task1=task.split()

                lst=[]
                result={i: j for i, j in enumerate(word)}
                result1={}
                for i, j in result.items():
                    result1.setdefault(j, []).append(i)

                while True:
                    super_print(task, lang, 'Light Blue')
                    if '_' not in task1:
                        super_print(word, lang, 'Green')
                        super_print('You win!!!', lang, 'Green')
                        base['Hangman'][name][0]+=1
                        break    
                    w=super_input('Enter a letter: ', lang)
                    w=w.lower().strip()
                    if w=='':
                        super_print('You must enter the letter!!!', lang, 'Red')
                    else:
                        if w in word and w not in lst:
                            lst.append(w)
                            num=len(result1[w])
                            for n in range(num):
                                i=result1[w][n]
                                task1[i]=w
                            task=' '.join(task1)
                        elif len(w)>1:
                            super_print('You must enter only one letter!!!', lang, 'Red')
                        elif w in lst:
                            super_print('This letter is already in the hidden word.', lang, 'Red')
                        elif point==9:
                            draw(d[9])
                            super_print(['Game Over!!!', 4*' ', 'Regular word:', word], lang, 'Red')
                            base['Hangman'][name][1]+=1
                            break
                        else:
                            point=mistake_was_maden(d, point, lang)
                pywrite('base.json', base)
                exit_to_mode(lang)
        
            case 'Rules':
                if lang=='ru':
                    rules=pyread('ru_rules_hangman.txt')
                else:
                    rules=pyread('en_rules_hangman.txt')
                super_print(rules, lang)
                exit_to_mode(lang)
        
            case 'Highscores':
                draw_leaderboard(base, lang)
                exit_to_mode(lang)

            case 'Exit':
                break
            case _:
                clear_screen()