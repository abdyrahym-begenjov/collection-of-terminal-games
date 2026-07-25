from translator import *
        
def draw_leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=list(base['Rock, Scissors, Paper'].items())
    base.sort(key=lambda x: x[1][0]-x[1][1], reverse=True)
    base=dict(base)

    lst=['VICTORIES', 'DEFEATS', 'OVERALL RESULT']
    lst=[f'{translator(i, lang):<16}|' for i in lst]
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
        c=j[0]-j[1]
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}| {b:<16}| {c:<16}|'
        print(line2)
        print(line)