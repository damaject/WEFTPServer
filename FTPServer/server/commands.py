# Created by Maxim on 28.03.2021 17:11

COMMANDS = {
    'hep': [0, 1, 'Show info about all commands [*command]'],
    'setrot': [1, 1, 'Set root dir [path]'],
    'getrot': [0, 0, 'Show root dir []'],
    'end': [0, 0, 'Exit from LdFileManager []'],
    'ind': [1, 1, 'Go in dir [name]'],
    'out': [0, 0, 'Out from dir []'],
    'lis': [0, 0, 'Show list files in directory []'],
    'credir': [1, 1, 'Create directory [name]'],
    'crefil': [1, 1, 'Create file [name]'],
    'rendir': [2, 2, 'Rename directory [oldname] [newname]'],
    'renfil': [2, 2, 'Rename file [oldname] [newname]'],
    'deldir': [1, 1, 'Delete directory [name]'],
    'delfil': [1, 1, 'Delete file [name]'],
    'copfil': [2, 2, 'Copy file [name] [newpath]'],
    'movfil': [2, 2, 'Move file [name] [newpath]'],
    'redfil': [1, 2, 'Read file [name] [*maxlines]'],
    'cftftp': [2, 2, 'Copy file to FTP [name] [data]'],
    'cffftp': [1, 1, 'Copy file from FTP [name]']
}
