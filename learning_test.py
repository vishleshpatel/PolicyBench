__author__ = 'vishlesh'

from enum import Enum
import ipaddress
import random

def compareIP(srcIp1,srcIp2):
   list1=srcIp1.subnets()
   if(srcIp2==list1.pop(0)):
       print("ip2 is less")


srcIp = ipaddress.ip_network('10.0.0.0/24')
srcIp1 = ipaddress.ip_address('10.0.0.1')
for each_addr in srcIp:
    if each_addr==srcIp1:
        print(each_addr,"match")
i = srcIp._prefixlen
print(i,"dsf")

"""
srcIp2 =ipaddress.ip_network('10.0.0.64/26')
srcIp3=ipaddress.ip_network('10.0.0.0/31')
if(srcIp.network_address==srcIp3.network_address):
    print(srcIp.network_address,"dsd")
if(srcIp.network_address<srcIp2.network_address):
    print("dfsd")


compareIP(srcIp,srcIp3)




list= [1,2,3,4,5,6,7]
print(list)
list.pop()
print(list)
print(random.sample(list,3))
"""