from translator import *
from subprocess import run
from platform import system
from json import load, dump
from colorama import Fore, Style
from sys import stdout
from time import sleep

colors={
    'White': Fore.WHITE,
    'Red': Fore.RED,
    'Light Red': Fore.LIGHTRED_EX,
    'Cyan': Fore.CYAN,
    'Dark Grey': Fore.LIGHTBLACK_EX,
    'Blue': Fore.BLUE,
    'Light Blue': Fore.LIGHTBLUE_EX,
    'Yellow': Fore.LIGHTYELLOW_EX,
    'Green': Fore.GREEN,
    'Magenta': Fore.MAGENTA
}

def delete_cursor():
    stdout.write("\x1b[?25l")
    stdout.flush()

def return_cursor():
    stdout.write("\x1b[?25h")
    stdout.flush()

def func_loading(lang):
    delete_cursor()
    super_print('Loading...', lang, 'Dark Grey')
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
                words_list=pyread('russian_words.json')
                v=['А', 'Б', 'В', 'Г']
                questions=pyread('q2.json')
                break
            case 'English':
                lang='en'
                cities_list=pyread('cities.json')
                words_list=pyread('words.json')
                v=['A', 'B', 'C', 'D']
                questions=pyread('q1.json')
                break
            case _:
                clear_screen()
    data['language']=lang
    data['cities']=cities_list
    data['words']=words_list
    data['variants']=v
    data['questions']=questions
    pywrite('data.json', data)
    return lang

def enter_name(data, base, lang):
    clear_screen()
    while True:
        name=super_input('Enter your name: ', lang)
        name=name.strip().title()
        if name=='':
            clear_screen()
            super_print('Error!!!', lang, 'Red')
        elif name in game_system_words:
            clear_screen()
            super_print('Don\'t write a word that is in the game system.', lang, 'Red')
        elif name in base['Users']:
            clear_screen()
            super_print('This name is already in the game database. Choose another name.', lang, 'Red')
        elif len(name)>16:
            clear_screen()
            super_print('The name must not exceed 16 characters!!!', lang, 'Red')
        else:
            is_my_name=super_input('Check if you have entered your name correctly. If not, write \"No\". If yes, then simply press Enter: ', lang)
            if new_word(is_my_name, lang)=='No':
                clear_screen()
            else:
                data['name']=name
                pywrite('data.json', data)
                fill_base(name, base, lang)
                return name

def fill_base(name, base, lang):
    for i in base:
        if name not in base[i]:
            for i in base:
                if i=='Users':
                    password=super_input('Create your password: ', lang)
                    base[i][name]=password
                elif i=='Snakes and Ladders':
                    base[i][name]=0
                else:
                    base[i][name]=[0, 0]
            pywrite('base.json', base)

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
        u=', '.join(base['Users'])
        super_print(['Users:', u], lang)
        change=super_input('Do you want to change parameters?: ', lang)
        change=new_word(change, lang)
        match change:
            case 'Name':
                name=enter_name(data, base, lang)
                clear_screen()
            case 'Language':
                lang=enter_lang(data)
                clear_screen()
            case 'Users':
                clear_screen()
                change_profile=super_input('Enter the username of the user whose parameters you want to change: ', lang)
                change_profile=change_profile.strip().title()
                if change_profile in base['Users']:
                    for i in range(3):
                        password=super_input('Enter the password of player: ', lang)
                        if password==base['Users'][change_profile]:
                            super_print('What exactly do you want to do with the selected profile?', lang)
                            choose_change_parameter=super_input('Enter \"Change name\", \"Change password\" or \"Delete user\": ', lang)
                            clear_screen()
                            match new_word(choose_change_parameter, lang):
                                case 'Change Name':
                                    for i in base:
                                        base[i]['']=base[i][change_profile]
                                        base[i].pop(change_profile)
                                    pywrite('base.json', base)
                                    while True:
                                        new_name=super_input('Enter your new name: ', lang)
                                        new_name=new_name.strip().title()
                                        if new_name=='':
                                            clear_screen()
                                            super_print('Error!!!', lang, 'Red')
                                        elif new_name in game_system_words:
                                            clear_screen()
                                            super_print('Don\'t write a word that is in the game system.', lang, 'Red')
                                        elif new_name in base['Users']:
                                            clear_screen()
                                            super_print('This name is already in the game database. Choose another name.', lang, 'Red')
                                        elif len(new_name)>16:
                                            clear_screen()
                                            super_print('The name must not exceed 16 characters!!!', lang, 'Red')
                                        else:
                                            for i in base:
                                                base[i][new_name]=base[i]['']
                                                base[i].pop('')
                                            pywrite('base.json', base)
                                            if change_profile==data['name']:
                                                data['name']=new_name
                                                pywrite('data.json', data)
                                            super_print('The name change is complete!!!', lang, 'Green')
                                            break
                                case 'Change Password':
                                    password=super_input('Create your new password: ', lang)
                                    base['Users'][name]=password
                                    super_print('The password change is complete!!!', lang, 'Green')
                                    pywrite('base.json', base)
                                case 'Delete User':
                                    want_delete=super_input('Are you sure you want to delete the selected profile? All scores will be erased. (Enter \"Yes\" or \"No\"): ', lang)
                                    if new_word(want_delete, lang)=='Yes':
                                        super_print([f'{change_profile}', 'is deleted.'], lang)
                                        for i in base:
                                            base[i].pop(change_profile)
                                        pywrite('base.json', base)
                                        if change_profile==data['name']:
                                            for i in data:
                                                if i in ('name', 'language'):
                                                    data[i]=''
                                                else:
                                                    data[i]=[]
                                            pywrite('data.json', data)
                                case _:
                                    clear_screen()
                            break
                        else:
                            super_print('Incorrect password!!! Please try again.', lang, 'Light Red')
                    else:
                        super_print('You don\'t know the password of the selected user. Ask him/her for the password and try again later.', lang, 'Red')
                else:
                    super_print('This user is not in game base', lang)
                super_input('Enter to exit: ', lang)
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