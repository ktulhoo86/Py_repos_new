# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
"""
from pprint import pprint
import textfsm


# def parser_output_to_dict(template, command_output):
#     with open(template) as tmpl:
#         parser = textfsm.TextFSM(tmpl)
#         header = parser.header
#         result = parser.ParseText(command_output)
#     return [dict(zip(header, line)) for line in result]


def parser_output_to_dict(template, command_output):
    with open(template) as tmpl:
        fsm = textfsm.TextFSM(tmpl)
        result = fsm.ParseTextToDicts(command_output)
    return result


if __name__ == "__main__":
    with open('output/sh_ip_int_br.txt') as show:
        output = show.read()
    rslt = parser_output_to_dict('templates/sh_ip_int_br.template', output)
    pprint(rslt, width=100)
