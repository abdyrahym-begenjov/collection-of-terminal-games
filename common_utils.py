from translator import *
from subprocess import run
from platform import system
from json import load, dump

def pyread(filename):
    try:
        match filename:
            case filename if filename.endswith('.txt'):
                with open(filename, 'r', encoding='utf-8') as file:
                    return file.read().strip()
            case filename if filename.endswith('.json'):
                with open(filename, 'r', encoding='utf-8') as file:
                    return load(file)
            case _:
                print('Error!!!')
    except FileNotFoundError:
        print('File is not found!!!')

def pywrite(filename, value):
    try:
        match filename:
            case filename if filename.endswith('.txt'):
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(value)
            case filename if filename.endswith('.json'):
                with open(filename, 'w', encoding='utf-8') as file:
                    dump(value, file, indent=4, ensure_ascii=False)
            case _:
                print('Error!!!')
    except FileNotFoundError:
        print('File is not found!!!')

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
            if name not in base['The Cities Game']:
                base['The Cities Game'][name]=[0, 0]
                pywrite('base.json', base)
            return name

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word