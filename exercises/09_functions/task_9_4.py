# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def convert_config_to_dict(config_filename):
    conf_dict = {}
    current_command = None
    current_subcommands = []
    with open(config_filename, 'r') as file:
        for line in file:
            if ignore_command(line, ignore):
                continue
            if line.startswith('!'):
                continue
            if not line.startswith(' '):
                if current_command:
                    '''
                    Задавать эту переменную нужно было для того, чтобы хранить в неё информацию. 
                    В этом условии проверяется, начинается ли строка с пробела, если нет, записывается в переменную current_command и задает формат в котором она будет обрабатываться

                    Вне этого условия продолжается обработка строк, который начинаются с пробела.
                    '''
                    conf_dict[current_command] = current_subcommands
                
                current_command = ' '.join(line.split()[:5]) 
                current_subcommands = [] 

            else:
                line = line.strip() 
                if line:
                    current_subcommands.append(line)

        if current_command:
            conf_dict[current_command] = current_subcommands if current_subcommands else []

    return conf_dict

dic = convert_config_to_dict('C:/Users/user/Documents/GitHub/pyneng/exercises/09_functions/config_sw1.txt')
print(dic)