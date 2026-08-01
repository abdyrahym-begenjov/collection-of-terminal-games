from translator import *
from common_utils import *
        
def draw_leaderboard(base, lang):
    super_print('LEADERBOARD:', lang)
    base=list(base['Rock, Scissors, Paper'].items())
    base.sort(key=lambda x: x[1][0]-x[1][1], reverse=True)
    max_value=base[0][1][0]-base[0][1][1]
    min_value=base[-1][1][0]-base[-1][1][1]
    base=dict(base)

    lst=['Victories', 'Defeats', 'Overall Result']
    lst=[translator(i, lang) for i in lst]
    lst=[f'{i.upper().strip():<16}|' for i in lst]
    lst=' '.join(lst)
    line1=f'|{translator('NAME |', lang):>18} {lst:<16}'
    line=(Style.BRIGHT+'-')*len(line1)
    super_print(line, lang, 'Cyan')
    super_print(line1, lang, 'Cyan', Style.BRIGHT)
    super_print(line, lang, 'Cyan')

    for i, j in base.items():
        name=i
        a=str(j[0])
        b=str(j[1])
        c=j[0]-j[1]
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}| {b:<16}| {c:<16}|'
        if c==max_value:
            super_print(line2, lang, 'Green')
            super_print(line, lang, 'Green')
        elif c==min_value:
            super_print(line2, lang, 'Red')
            super_print(line, lang, 'Red')
        else:
            super_print(line2, lang, 'Yellow')
            super_print(line, lang, 'Yellow')