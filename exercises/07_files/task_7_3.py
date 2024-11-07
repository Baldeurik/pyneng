# -*- coding: utf-8 -*-
"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = {}
file = "C:/Users/user/Documents/GitHub/pyneng/exercises/07_files/CAM_table.txt"
with open(file, 'r') as f:
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
output_lines = []
for vlan_num, mac_ports in result.items():
    for mac_address, ports in mac_ports:
        output_lines.append(f"{vlan_num:<8} {mac_address:} {ports:>10}")
output_string = '\n'.join(output_lines)
print(output_string)