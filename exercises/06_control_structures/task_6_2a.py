# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ask_for_ip = input("Ввести IP-адрес в формате 10.0.1.1: ")
ip_split = ask_for_ip.split('.') # IP приводится к виду списка, '.' - разделитель

while True:
   if len(ip_split) != 4:
      print("Неправильный IP-адрес")
      break
   else:
      valid = True
      for num in ip_split:
         if not num.isdigit() or not 0 <= int(num) <= 255:
            valid = False
            print("Неправильный IP-адрес")
            break
      if valid == True:
         if ip_split[0] >= '1' and ip_split[0] <= '223':
            print("unicast")
            break
         elif ip_split[0] >= '224' and ip_split[0] <= '239':
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
      else:
         break