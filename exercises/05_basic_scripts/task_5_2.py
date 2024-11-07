# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Network: ")

print("Network:\n")
iplisted = ip.replace('.', ' ').replace('/', ' ').split()

print('{:<10}{:<10}{:<10}{:<10}'.format(iplisted[0], iplisted[1], iplisted[2], iplisted[3]))

tobin = '{:08b}  {:08b}  {:08b}  {:08b}'.format(int(iplisted[0]), int(iplisted[1]), int(iplisted[2]), int(iplisted[3]))

print(f"{tobin}\n\n")
print("Mask:\n/" '{:<10}'.format(iplisted[4]))


  

calculatemaskend = 32 - int(iplisted[4])

calculatemask = "1" * int(iplisted[4]) + "0" * calculatemaskend

binarymask = '{:08b}  {:08b}  {:08b}  {:08b}'.format(

   int(calculatemask[0:8], 2),
   int(calculatemask[8:16], 2),
   int(calculatemask[16:24], 2),
   int(calculatemask[24:32], 2))

decimalmask = '{:<10}{:<10}{:<10}{:<10}'.format(

  int(calculatemask[0:8], 2),
  int(calculatemask[8:16], 2),
  int(calculatemask[16:24], 2),
  int(calculatemask[24:32], 2)

)

print(decimalmask)

print(binarymask)