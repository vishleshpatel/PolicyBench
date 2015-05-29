__author__ = 'vishlesh'

from enum import Enum
import ipaddress
import random
import sys
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hosts","-nh", default = "1000", help="No. of hosts you want in your network" )
    parser.add_argument("--policyType","-t",default = "light",  help = "To create policy light network or policy heavy network")
    parser.add_argument("--policies", "-p" ,default="4000",  help = "no. of policy you want to create")

    args = parser.parse_args()

    print(args)
    list1 = []
    list1=list(args)
    print(list1)
if __name__ == '__main__':
    main()

def compareIP(srcIp1,srcIp2):
   list1=srcIp1.subnets()
   if(srcIp2==list1.pop(0)):
       print("ip2 is less")

list1=[1,2,3,4]
string = str(list1)
print(string,"dsfsd")
str = "10.0.10.200/31, 10.0.9.192/32, Action.count"

(srcip,dstip) = str.split(", ",1)
dstip,temp = dstip.split(", ",1)
list1 = []
list1.append
list1.append((srcip,dstip))
print(list1[0],"here")

srcIp = ipaddress.ip_network('10.0.0.0/24')
srcIp1 = ipaddress.ip_address('10.0.0.1')
for each_addr in srcIp:
    if each_addr==srcIp1:
        print(each_addr,"match")
i = srcIp._prefixlen
#print(i,"dsf")

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