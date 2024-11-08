# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
file = "C:/Users/user/Documents/GitHub/pyneng/exercises/07_files/config_sw1.txt"

ignore = ["duplex", "alias", "configuration"]
#file = input("Введите название файла: ")
with open(file, 'r') as f:
    for line in f:
        printer = True
        for words in ignore:
            if words in line:
                printer = False
                break

        if '!' in line.strip('\n'):
            printer = False
        if printer:
            print(line.rstrip())