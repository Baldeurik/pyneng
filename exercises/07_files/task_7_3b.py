# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = {}
with open("C:/Users/user/Downloads/CAM_table.txt", 'r') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0].isdigit(): # Проверка на то, что влан - число
            vlan_num = line_list[0]
            mac_address = line_list[1]
            ports = line_list[3]
# присвоение переменным значения в словаре
            if vlan_num not in result: # условие на случай, если влан повторяется
                result[vlan_num] = []
            result[vlan_num].append((mac_address, ports))
specific_vlan = input("Enter VLAN number: ")
output_lines = []
if specific_vlan in result:
    for mac_address, ports in result[specific_vlan]:
        output_lines.append(f"{specific_vlan:<8} {mac_address} {ports:>10}")
output_string = '\n'.join(output_lines)
print(output_string)