from translator import *
from subprocess import run
from platform import system
from json import load, dump
from colorama import Fore, Style
import sys
from time import sleep

colors={
    'White': Fore.WHITE,
    'Red': Fore.RED,
    'Light Red': Fore.LIGHTRED_EX,
    'Cyan': Fore.CYAN,
    'Light Cyan': Fore.LIGHTCYAN_EX,
    'Blue': Fore.BLUE,
    'Light Blue': Fore.LIGHTBLUE_EX,
    'Yellow': Fore.YELLOW,
    'Light Yellow': Fore.LIGHTYELLOW_EX,
    'Green': Fore.GREEN,
    'Magenta': Fore.MAGENTA
}

def delete_cursor():
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

def return_cursor():
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()

def func_loading(lang):
    delete_cursor()
    super_print('Loading...', lang)
    sleep(2)
    clear_screen()
    return_cursor()

def pyread(filename):
    match filename:
        case filename if filename.endswith('.txt'):
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read().strip()
        case filename if filename.endswith('.json'):
            with open(filename, 'r', encoding='utf-8') as file:
                return load(file)

def pywrite(filename, value):
    match filename:
        case filename if filename.endswith('.txt'):
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(value)
        case filename if filename.endswith('.json'):
            with open(filename, 'w', encoding='utf-8') as file:
                dump(value, file, indent=4, ensure_ascii=False)

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def super_print(text, lang, color='White', style_text=Style.NORMAL):
    if isinstance(text, list):
        lst=[colors[color]+style_text+translator(str(i), lang) for i in text]
        new_text=' '.join(lst)
    else:
        new_text=colors[color]+style_text+translator(text, lang)
    print(new_text)

def super_input(text, lang, color='White', style_text=Style.NORMAL):
    if isinstance(text, list):
        lst=[colors[color]+style_text+translator(str(i), lang) for i in text]
        new_text=' '.join(lst)
    else:
        new_text=colors[color]+style_text+translator(text, lang)
    result=input(new_text)
    return result

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
        name=super_input('Enter your name: ', lang)
        name=name.strip()
        if name=='':
            clear_screen()
            super_print('Error!!!', lang, 'Red')
        elif len(name)>16:
            clear_screen()
            super_print('The name must not exceed 16 characters!!!', lang, 'Red')
        else:
            data['name']=name
            pywrite('data.json', data)
            if name not in base['The Cities Game']:
                base['The Cities Game'][name]=[0, 0]
                base['Rock, Scissors, Paper'][name]=[0, 0]
                pywrite('base.json', base)
            return name

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word

def settings(data, base, name, lang):
    clear_screen()
    while True:
        super_print(['Name:', data['name']], lang)
        super_print(['Language:', data['language']], lang)
        change=super_input('Do you want to change parameters (Enter \"Name\" or \"Language\")?: ', lang)
        change=new_word(change, lang)
        match change:
            case 'Name':
                name=enter_name(data, base, lang)
                clear_screen()
            case 'Language':
                lang=enter_lang(data)
                clear_screen()
            case _:
                break
    clear_screen()
    return name, lang

def choose_mode(lang):
    super_print('Game      Rules      Highscores      Exit', lang, 'Cyan')
    mode=super_input('Choose a game mode: ', lang, 'Cyan')
    mode=new_word(mode, lang)
    clear_screen()
    return mode

def exit_to_mode(lang):
    end=super_input('Enter to exit mode: ', lang)
    clear_screen()

def exit_to_game(lang):
    clear_screen()
    exit_confirm=super_input('Do you want to exit (\"Yes\" or \"No\")?: ', lang)
    exit_confirm=new_word(exit_confirm, lang)
    return exit_confirm