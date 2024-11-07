# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('C:/Users/user/Downloads/ospf.txt', 'r') as f:

    for line in f:
        line_list = line.strip()
        line_list = line_list.split()
        prefix = line_list[1]
        ad_metric = line_list[2][1:-1]
        next_hop = line_list[4][:-1]
        last_update = line_list[5][:-1]
        outbound_interface = line_list[6]
        print(f"Prefix                {prefix}")
        print(f"AD/Metric             {ad_metric}")
        print(f"Next-Hop              {next_hop}")
        print(f"Last update           {last_update}")
        print(f"Outbound Interface     {outbound_interface}\n")