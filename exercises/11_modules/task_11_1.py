# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    lines = command_output.strip().split('\n')
    cdp_dict = {}

    # Извлекаем имя локального устройства из первой строки
    local_device = lines[0].split('>')[0]
    # Обрабатываем строки с информацией о соседях
    if local_device == "SW1":
        for line in lines[6:]:
            parts = line.split()
            local_int = parts[1] + parts[2]
            remote_device_id = parts[0]
            remote_port_id = parts[-2] + parts[-1]
            # Ключ: (локальное устройство, локальный интерфейс), значение: (удалённое устройство, удалённый интерфейс)
            cdp_dict[(local_device, local_int)] = (remote_device_id, remote_port_id)
    else:
        for line in lines[5:]:
            parts = line.split()
            local_int = parts[1] + parts[2]
            remote_device_id = parts[0]
            remote_port_id = parts[-2] + parts[-1]
                # Ключ: (локальное устройство, локальный интерфейс), значение: (удалённое устройство, удалённый интерфейс)
            cdp_dict[(local_device, local_int)] = (remote_device_id, remote_port_id)

    return cdp_dict


if __name__ == "__main__":
    with open("exercises/11_modules/sh_cdp_n_sw1.txt") as f:
        command_output = f.read()
        result = parse_cdp_neighbors(command_output)
        print(result)
