# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    with open (config_filename, 'r') as file:
        current_interface = None
        is_access = False
        is_trunk = False

        for line in file:
            line = line.strip()
            if line.startswith('interface Fast'):
                current_interface = line.split()[-1]
                is_access = False
                is_trunk = False
            elif line.startswith('switchport access vlan'):
                vlan = int(line.split()[-1])
                access[current_interface] = vlan
                is_access = True
            elif line.startswith('switchport trunk allowed vlan'):
                vlans = line.split()[-1]
                trunk[current_interface] = [int(v) for v in vlans.split(',')]
                is_trunk = True

            if current_interface and (is_access or is_trunk):
                if is_access and current_interface not in access:
                    access[current_interface] = access[current_interface]
                if is_trunk and current_interface not in trunk:
                    trunk[current_interface] = trunk[current_interface]
    return access, trunk


config = get_int_vlan_map(config_filename='C:/Users/user/Documents/GitHub/pyneng/exercises/09_functions/config_sw1.txt')
print(config)