import json

def pyread(filename):
    try:
        match filename:
            case filename if filename.endswith('.txt'):
                with open(filename, 'r', encoding='utf-8') as file:
                    return file.read().strip()
            case filename if filename.endswith('.json'):
                with open(filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
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
                    json.dump(value, file, indent=4, ensure_ascii=False)
            case _:
                print('Error!!!')
    except FileNotFoundError:
        print('File is not found!!!')