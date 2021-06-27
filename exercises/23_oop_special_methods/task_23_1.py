# -*- coding: utf-8 -*-

"""
Задание 23.1

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""


class IPAddress:
    
    def __init__(self,ip_addr):
        self.ip,self.mask = self._separete_ip_mask(ip_addr)
        ip = self.ip
        mask = self.mask
        self._check_ip(ip)
        self._check_mask(mask)
    
    def _separete_ip_mask(self, ip_addr):
        ip = ip_addr.split('/')[0]
        mask = ip_addr.split('/')[1]
        return ip, int(mask)   
        
    def _check_ip(self , ip):
        ip_addr = self.ip 
        ip_addr2 = []
        b =0
        '------проверка длинны сообщения ------'
        if 7 <= len(ip_addr) <= 15:
            check_len_input=True
        else:
            raise ValueError(' Incorrect IPv4 address')
        '-------Проверка цифр и точек----------------------'
        for point in list(ip_addr):
            if point.isdigit() == True:
                ip_addr2.append(point)
            elif point == '.': 
                b=b+1
                ip_addr2.append(point)
            else: 
                raise ValueError(' Incorrect IPv4 address')
        '-----Проверка на точку в конце в начале и количество точек не равное 4м-----'
        if ip_addr2[0] == '.' or ip_addr2[-1] == '.' or b != 3 : 
            raise ValueError(' Incorrect IPv4 address')
        for line in ip_addr.split('.'):
            if  line.isdigit() and int(line) > 255:
                raise ValueError(' Incorrect IPv4 address') 
        return True
        
    def _check_mask(self, mask):
        if 8 < mask > 32:
            raise ValueError(' ValueError: Incorrect mask') 
        return True
            
        
if __name__ == '__main__':
    ip = IPAddress('10.30.1.100/24')
    print(ip.ip)
    print(ip.mask)
    
    
    
    
    
    
    
