__author__ = 'vishlesh'

from enum import Enum
import ipaddress

class test:
    ipnet = ipaddress.ip_network('10.0.0.0/29')

    def getlist(self,ipnet):
        list = []
        for addr in ipnet:
            list.append(addr)

        list.pop()
        list.pop(0)
        return list


class action(Enum):
    forward = 1
    drop =2

a= action(1)
list =str(a).split('.')
print( str(list[1]))
print(str(a).split('.'))

t =test()
list=t.getlist(ipaddress.IPv4Network('10.0.0.0/29'))
print(list)
print(len(list))