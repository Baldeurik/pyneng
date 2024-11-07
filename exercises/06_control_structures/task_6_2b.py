# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def is_valid_ip(ip):
    ip_split = ip.split('.')
    if len(ip_split) != 4:
        return False
    for segment in ip_split:
        if not segment.isdigit() or not 0 <= int(segment) <= 255:
            return False
    return True

while True:
    ask_for_ip = input("Введите IP в формате: 10.0.1.1: ")
    
    if not is_valid_ip(ask_for_ip):
        print("Неправильный IP-адрес")
        continue  
    else:
        
        ip_split = [int(segment) for segment in ask_for_ip.split('.')]
        
        # Determine IP type
        if ask_for_ip == "255.255.255.255":
            print("local broadcast")
        elif ask_for_ip == "0.0.0.0":
            print("unassigned")
        elif 1 <= ip_split[0] <= 223:
            print("unicast")
        elif 224 <= ip_split[0] <= 239:
            print("multicast")
        else:
            print("unused")
        break
