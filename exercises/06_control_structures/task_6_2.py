# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ask_for_ip = input("Ввести IP-адрес в формате 10.0.1.1: ")

ip = ask_for_ip.split('.')


  
  

while True:
   if ip[0] >= '1' and ip[0] <= '223':
      print("unicast")
      break

   elif ip[0] >= '224' and ip[0] <= '239':
      print("multicast")
      break

   elif ask_for_ip == "255.255.255.255":
    print("local broadcast")
    break

   elif ask_for_ip == "0.0.0.0":
      print("unassigned")
      break
   else:
    print("unused")
    break