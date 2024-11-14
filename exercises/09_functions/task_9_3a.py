# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
            elif line.startswith('switchport mode access'):
                access[current_interface] = 1
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


config = get_int_vlan_map(config_filename='C:/Users/user/Documents/GitHub/pyneng/exercises/09_functions/config_sw2.txt')
print(config)