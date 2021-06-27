# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""



class IPAddress:
    
    def __init__(self,ip_addr):
        self.ip,self.mask = self._separete_ip_mask(ip_addr)
        ip = self.ip
        mask = self.mask
        self._check_ip(ip)
        self._check_mask(mask)
    
    def __str__(self):
        return f"IP address {self.ip}/{self.mask}"
        
    def __repr__(self):
         return f"IPAddress('{self.ip}/{self.mask}')"
    
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
    print(str(ip))
    list_test = []
    list_test.append(ip)
    print(list_test)
    
    
    
    
    
