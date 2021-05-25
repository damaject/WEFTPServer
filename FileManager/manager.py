# Created by Maxim on 27.03.2021 23:31

import os
import shutil
from commands import COMMANDS

SETTING_FILE = 'settings.ldm'
ROOT_DIR = ''
USER_PATH = []

try:
    file = open(SETTING_FILE, 'r')
    ROOT_DIR = file.readline()
    file.close()
    if not os.path.isdir(ROOT_DIR):
        ROOT_DIR = ''
except IOError:
    pass


def get_args(name, params):
    if params == '':
        return []
    elif COMMANDS[name][1] <= 1:
        params = [params.replace('[', '').replace(']', '')]
    else:
        temp = ''
        in_brackets = False
        for s in params:
            if s == '[':
                in_brackets = True
            elif s == ']':
                in_brackets = False
            else:
                if s == ' ' and not in_brackets:
                    temp += '<LdSep>'
                else:
                    temp += s
        params = temp.split('<LdSep>')
    return params


def clear_path(path):
    for c in ['../', './', '/', '..\\', '.\\', '\\']:
        path = path.replace(c, '')
    return path


def get_user_path():
    path = ''
    for d in USER_PATH:
        path += '/' + d
    return path + '/'


def get_root_path():
    return ROOT_DIR + get_user_path()


def ld_command(name, params):
    global ROOT_DIR
    name = name.lower()

    if name == '' or name == 'end':
        return False

    if name in COMMANDS:
        params = get_args(name, params)
        if not (COMMANDS[name][0] <= len(params) <= COMMANDS[name][1]):
            print('! LdCommand «' + name + '» params error, use «hep ' + name + '» to learn')
            return True
    else:
        print('! LdCommand «' + name + '» not found, use «hep» to learn LdCommands')
        return True

    if name == 'hep':
        if len(params) == 0:
            i = 1
            print('LdFileManager\nNote: Use brackets «[» and «]» for param\nwith space on multiparams commands')
            print('LdCommands (* - optional param):')
            for key in COMMANDS:
                print(f'{i}. {key} - {COMMANDS[key][2]}')
                i += 1
        else:
            print(f'LdFileManager LdCommand «{params[0]}»:')
            if params[0] in COMMANDS:
                print(COMMANDS[params[0]][2])
            else:
                print(f'! LdCommand «{params[0]}» not found')
        return True
    elif name == 'setrot':
        new_path = params[0]
        if not os.path.isdir(new_path):
            print('! Path is not dir')
        else:
            ROOT_DIR = new_path
            file = open(SETTING_FILE, 'w')
            file.write(ROOT_DIR)
            file.close()
            print('Root dir changed')
        return True
    elif name == 'getrot':
        print(f'Root dir is «{ROOT_DIR}»')
        return True

    if ROOT_DIR == '':
        print(f'! LdCommand «{name}» need root dir')
        return True

    if name == 'ind':
        in_dir = clear_path(params[0])
        path = get_root_path() + in_dir
        if os.path.exists(path) and os.path.isdir(path):
            USER_PATH.append(in_dir)
        else:
            print('Directory not exists')
    elif name == 'out':
        if len(USER_PATH) > 0:
            USER_PATH.pop()
        else:
            print('You in root dir!')
    elif name == 'lis':
        i = 1
        for f in os.listdir(get_root_path()):
            print(f'{i}. {f}')
            i += 1
    elif name == 'credir':
        path = get_root_path() + clear_path(params[0])
        try:
            os.mkdir(path)
        except OSError:
            print('! Directory not created')
        else:
            print('Directory created')
    elif name == 'crefil':
        path = get_root_path() + clear_path(params[0])
        if os.path.exists(path):
            print('File already exists')
        else:
            try:
                open(path, 'w').close()
            except OSError:
                print('! File not created')
            else:
                print('File created')
    elif name == 'rendir':
        old_path = get_root_path() + clear_path(params[0])
        new_path = get_root_path() + clear_path(params[1])
        if os.path.exists(old_path) and os.path.isdir(new_path):
            try:
                os.rename(old_path, new_path)
            except OSError:
                print('! Directory not renamed')
            else:
                print('Directory renamed')
        else:
            print('Directory not exists')
    elif name == 'renfil':
        old_path = get_root_path() + clear_path(params[0])
        new_path = get_root_path() + clear_path(params[1])
        if os.path.exists(old_path) and os.path.isfile(new_path):
            try:
                os.rename(old_path, new_path)
            except OSError:
                print('! File not renamed')
            else:
                print('File renamed')
        else:
            print('File not exists')
    elif name == 'deldir':
        path = get_root_path() + clear_path(params[0])
        if os.path.exists(path) and os.path.isdir(path):
            try:
                os.rmdir(path)
            except OSError:
                print('! Directory not deleted')
            else:
                print('Directory deleted')
        else:
            print('Directory not exists')
    elif name == 'delfil':
        path = get_root_path() + clear_path(params[0])
        if os.path.exists(path) and os.path.isfile(path):
            try:
                os.remove(path)
            except OSError:
                print('! File not deleted')
            else:
                print('File deleted')
        else:
            print('File not exists')
    elif name == 'copfil':
        path_old = get_root_path() + params[0]
        path_new = get_root_path() + params[1]
        if os.path.exists(path_old) and os.path.isfile(path_old):
            try:
                shutil.copy(path_old, path_new)
            except IOError:
                print('! File not copied')
            else:
                print('File copied')
        else:
            print('File not exists')
    elif name == 'movfil':
        path_old = get_root_path() + params[0]
        path_new = get_root_path() + params[1]
        if os.path.exists(path_old) and os.path.isfile(path_old):
            try:
                shutil.move(path_old, path_new)
            except IOError:
                print('! File not moved')
            else:
                print('File moved')
        else:
            print('File not exists')
    elif name == 'redfil':
        path = get_root_path() + clear_path(params[0])
        max_lines = -1
        if len(params) > 1:
            try:
                max_lines = int(params[1])
            except ValueError:
                print('! LdCommand «' + name + '» second param not is number')
                return True
            if max_lines < 0:
                max_lines = 0
        if os.path.exists(path) and os.path.isfile(path):
            try:
                fil = open(path, 'r', encoding='utf-8')
                i = 1
                for line in fil.readlines():
                    if max_lines != -1 and i > max_lines:
                        break
                    print(f'{i}. {line}', end='')
                    i += 1
                fil.close()
            except BaseException:
                print('! File not read')
        else:
            print('File not exists')
    elif name == 'wrifil':
        path = get_root_path() + clear_path(params[0])
        append = 1
        if len(params) > 1:
            try:
                append = int(params[1])
            except ValueError:
                print('! LdCommand «' + name + '» second param not is number')
                return True
            if append != 0 and append != 1:
                print('! LdCommand «' + name + '» second param must be 0 or 1')
                return True
        if os.path.exists(path) and os.path.isfile(path):
            try:
                fil = open(path, ['w', 'a'][append], encoding='utf-8')
                text = ''
                if append == 1:
                    text += '\n'
                print('Writing to file... to end use «wriend»')
                while True:
                    line = input()
                    if line == 'wriend':
                        break
                    else:
                        text += line + '\n'
                fil.write(text)
                fil.close()
            except BaseException:
                print('! Error open/write file')
        else:
            print('File not exists')
    elif name == 'wriend':
        print('! LdCommand «' + name + '» use in «wrifil» to ends writing to file')

    return True


print('LdFileManager is started...')
if ROOT_DIR == '':
    print('Warning! Root dir not set!')
else:
    print(f'Root dir is «{ROOT_DIR}»')
print('Use «hep» to learn LdCommands')

while True:
    print(get_user_path() + '> ', end='')
    text = input().split(' ', 1)
    if not ld_command(text[0], text[1] if len(text) == 2 else ''):
        break

print('LdFileManager is finished...')
