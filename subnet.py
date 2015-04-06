__author__ = 'Vishlesh.Patel'

import ipaddress
import math
import random
class Subnet:

    ''''
    totalHosts : total no. of end points in entire network

    sizeOfSubnets : total no. of hosts in 1 subnet
    allowed subnet size - 14,30,64,128,256,512,1024,2048 ==> 2^n - 2
    '''''


    def createEqualSubnets(self, totalHosts, hostsPerSubnet):

        numberOfSubnets = int(totalHosts / hostsPerSubnet) +1
        subnetHostMask = (int(math.log2(hostsPerSubnet))+1)

        networkIP = ipaddress.IPv4Network('10.0.0.0/15')
        subnetsList = self.getList(networkIP,subnetHostMask)

        return list(subnetsList[0:numberOfSubnets])

    def getList(self,networkAddr, subnetHostMask):
        return list(networkAddr.subnets(prefixlen_diff=17-subnetHostMask))


    def createSubnets(self, totalHosts):

        networkIP = ipaddress.IPv4Network('10.0.0.0/15')
        subnetsList = []
        subnetsList[0] = self.getList(networkIP,4)  #list of all subnets , each subnet contains 14 end hosts
        subnetsList[1] = self.getList(networkIP,5)    #32
        subnetsList[2] = self.getList(networkIP,6)    #64
        subnetsList[3] = self.getList(networkIP,7)
        subnetsList[4] = self.getList(networkIP,8)  #256
        subnetsList[5] = self.getList(networkIP,9)  #512
        subnetsList[6] = self.getList(networkIP,10)  #1024
        subnetsList[7] = self.getList(networkIP,11)  #2048


    # def getRandomCombination(self,totalHost):
         # to be implemented




s = Subnet()
list = s.createEqualSubnets(255,30)
print(len(list))
print(list)