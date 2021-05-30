# -*- coding: utf-8 -*-
"""
Задание 20.4

Создайте шаблон templates/add_vlan_to_switch.txt, который будет использоваться
при необходимости добавить VLAN на коммутатор.

В шаблоне должны поддерживаться возможности:
* добавления VLAN и имени VLAN
* добавления VLAN как access, на указанном интерфейсе
* добавления VLAN в список разрешенных, на указанные транки

Шаблон надо создавать вручную, скопировав части конфига в соответствующий шаблон.

Если VLAN необходимо добавить как access, надо настроить и режим интерфейса
и добавить его в VLAN:
interface Gi0/1
 switchport mode access
 switchport access vlan 5

Для транков, необходимо только добавить VLAN в список разрешенных:
interface Gi0/10
 switchport trunk allowed vlan add 5

Имена переменных надо выбрать на основании примера данных,
в файле data_files/add_vlan_to_switch.yaml.


Проверьте шаблон templates/add_vlan_to_switch.txt на данных
в файле data_files/add_vlan_to_switch.yaml, с помощью функции generate_config
из задания 20.1.
Не копируйте код функции generate_config.

"""
import yaml
from task_20_1 import generate_config







if __name__ == "__main__":
    data_file = "data_files/add_vlan_to_switch.yaml"
    template_file = "templates/add_vlan_to_switch.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))


'''
vlan {{ vlan_id }}
 name {{ name }}
{%if access %}
{% for int_accesss in access%}
interface {{int_accesss}}
 switchport mode access
 switchport access vlan {{vlan_id}}
{%endfor%}
{%endif%}
{%if trunk%}
{%for int_trunk in trunk%}
interface {{int_trunk}}
 switchport trunk allowed vlan add {{vlan_id}}
{%endfor%}
{%endif%}
'''



"""
vlan {{ vlan_id }}
 name {{ name }}
{% for int in access %}
interface {{ int }}
 switchport mode access
 switchport access vlan {{ vlan_id }}
{% endfor %}
{% for int in trunk %}
interface {{ int }}
 switchport trunk allowed vlan add {{ vlan_id }}
{% endfor %}
"""
