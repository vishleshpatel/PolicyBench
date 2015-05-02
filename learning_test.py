__author__ = 'vishlesh'

from enum import Enum
import ipaddress
import random

srcIp = ipaddress.ip_network('10.0.0.0/24')
if srcIp._prefixlen == 31:
    print(srcIp.netmask,"ds")
list1 = list(srcIp.subnets())
srcIp1 = list1.pop(0)
srcIp2=list1.pop()
print(srcIp,"ip")
print(srcIp1,"ip1")
print(srcIp2,"ip2")
if srcIp2>=srcIp:
    print("dnsd")
else:
    print("loda")

list= [1,2,3,4,5,6,7]
print(list)
list.pop()
print(list)
print(random.sample(list,3))
