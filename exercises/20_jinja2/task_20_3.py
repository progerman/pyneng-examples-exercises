# -*- coding: utf-8 -*-
"""
Задание 20.3

Создайте шаблон templates/ospf.txt на основе конфигурации OSPF в файле cisco_ospf.txt.
Пример конфигурации дан, чтобы показать синтаксис.

Шаблон надо создавать вручную, скопировав части конфига в соответствующий шаблон.

Какие значения должны быть переменными:
* номер процесса. Имя переменной - process
* router-id. Имя переменной - router_id
* reference-bandwidth. Имя переменной - ref_bw
* интерфейсы, на которых нужно включить OSPF. Имя переменной - ospf_intf.
  На месте этой переменной ожидается список словарей с такими ключами:
  * name - имя интерфейса, вида Fa0/1, Vlan10, Gi0/0
  * ip - IP-адрес интерфейса, вида 10.0.1.1
  * area - номер зоны
  * passive - является ли интерфейс пассивным. Допустимые значения: True или False

Для всех интерфейсов в списке ospf_intf, надо сгенерировать строки:
 network x.x.x.x 0.0.0.0 area x

Если интерфейс пассивный, для него должна быть добавлена строка:
 passive-interface x

Для интерфейсов, которые не являются пассивными, в режиме конфигурации интерфейса,
надо добавить строку:
 ip ospf hello-interval 1


Все команды должны быть в соответствующих режимах.

Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf.yml,
с помощью функции generate_config из задания 20.1.
Не копируйте код функции generate_config.

В результате должна получиться конфигурация такого вида
(команды в режиме router ospf не обязательно должны быть в таком порядке,
главное чтобы они были в нужном режиме):
router ospf 10
 router-id 10.0.0.1
 auto-cost reference-bandwidth 20000
 network 10.255.0.1 0.0.0.0 area 0
 network 10.255.1.1 0.0.0.0 area 0
 network 10.255.2.1 0.0.0.0 area 0
 network 10.0.10.1 0.0.0.0 area 2
 network 10.0.20.1 0.0.0.0 area 2
 passive-interface Fa0/0.10
 passive-interface Fa0/0.20
interface Fa0/1
 ip ospf hello-interval 1
interface Fa0/1.100
 ip ospf hello-interval 1
interface Fa0/1.200
 ip ospf hello-interval 1
"""


from task_20_1 import generate_config
import yaml


if __name__ == "__main__":
    data_file = "data_files/ospf.yml"
    template_file = "templates/ospf.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))

'''
router ospf {{process}}
 router-id {{router_id}}
 auto-cost reference-bandwidth {{ref_bw}}
 {% for ospf_list in ospf_intf %}
 {% set ip = ospf_list.ip %}
 {% set area = ospf_list.area %}
 network {{ip}} 0.0.0.0 area {{area}}
 {% endfor %}
 {% for ospf_list in ospf_intf %}
 {% if ospf_list.passive %}
 {% set int = ospf_list.name %}
 passive-interface {{int}}
 {% endif %}
 {% endfor %}
 {% for ospf_list in ospf_intf %}
 {%if ospf_list.passive == false %}
 {% set int = ospf_list.name %}
interface {{int}}
 ip ospf hello-interval 1
 {%endif%}
 {%endfor%}
'''







