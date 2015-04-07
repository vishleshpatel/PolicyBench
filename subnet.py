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
        list = []   # list of subnets - list of different sizes
        subnetsList = []


        list.append( self.getList(networkIP,4))   #list of all subnets , each subnet contains 14 end hosts
        list.append(self.getList(networkIP,5))     #32
        list.append(self.getList(networkIP,6))    #64
        list.append(self.getList(networkIP,7))  #128
        list.append(self.getList(networkIP,8))  #256

        combination = self.getRandomCombination(totalHosts)
        combination = sorted(combination.items(),reverse=1)
        combination = dict(combination)
        print(combination,"should be sorted")
        list_combination = combination.items()
        list_keys = []
        list_values = []
        for (x,y) in list_combination:
            list_keys.append(x)
            list_values.append(y)
        next_start = []
        #print(len(list_keys),"length of keys list")

        for i in range(0,len(list_keys),1):
            #print(i,list_keys[i],list_values[i],"in for loop")
            if(list_keys[i]==14):
                 subnetsList = list[0][0:list_values[i]]
                 if((i+1) < len(list_keys)):
                     if(list_keys[i+1] == 30):
                         #subnetsList = list[0][0:list_values[i]]
                         next_start.append( int(math.ceil(list_values[i]/2)))
                     elif(list_keys[i+1]==62):
                         #subnetsList = list[0][0:list_values[i]]
                         next_start.append(int(math.ceil(list_values[i]/4)))
                     elif(list_keys[i+1]==126):
                        # subnetsList = list[0][0:list_values[i]]
                         next_start.append(int(math.ceil(list_values[i]/8)))
                     else:
                         #subnetsList = list[0][0:list_values[i]]
                         next_start.append(int(math.ceil(list_values[i]/16)))

            elif(list_keys[i] ==30):
                if(i==0):
                    temp = 0
                else:
                    temp = int(next_start.pop())
                subnetsList.extend(list[1][temp:temp+list_values[i]])
                if((i+1) < len(list_keys)):
                    if(list_keys[i+1]==62):
                         if(i==1):
                            next_start.append( int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4)))
                         else:
                            next_start.append( int(math.ceil(list_values[i]/2)))
                    elif(list_keys[i+1]==126):
                        #subnetsList.extend(list[1][next_start[i],next_start[i]+list_values[i]])
                        if(i==1):  #14,30,126,...
                            next_start.append(int(math.ceil(list_values[i]/4)) + int(math.ceil(list_values[i-1]/8)))
                        else:   #30,126
                            next_start.append(int(math.ceil(list_values[i]/4)))
                    else:
                        #subnetsList.extend(list[1][next_start[i],next_start[i]+list_values[i]])
                        if(i==1):  #14,30,126,...
                            next_start.append(int(math.ceil(list_values[i]/8)) + int(math.ceil(list_values[i-1]/16)))
                        else:   #30,126
                            next_start.append(int(math.ceil(list_values[i]/8)))

            elif(list_keys[i] ==62):
                if(i==0):
                    temp = 0
                else:
                    temp = int(next_start.pop())
                subnetsList.extend(list[2][temp:temp+list_values[i]])
                if((i+1) < len(list_keys)):
                    if(list_keys[i+1]==126):
                        if(i==2):  #14,30,62,126,...
                            next_start.append(int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4))\
                                              + int(math.ceil(list_values[i-2]/8)))
                        elif(i==1):   #14,62,126 or 30,62,126
                            if(list_keys[i-1]==14): #14,62,126,...
                                next_start.append(int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/8)))
                            else:#30,62,126,...
                                next_start.append(int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4)))
                    else:
                        #subnetsList.extend(list[1][next_start[i],next_start[i]+list_values[i]])
                        if(i==1):  #14,30,126,...
                            next_start.append(int(math.ceil(list_values[i]/8)) + int(math.ceil(list_values[i-1]/16)))
                        else:   #30,126
                            next_start.append(int(math.ceil(list_values[i]/8)))

            elif(list_keys[i]==126):
                if(i==0):
                    temp = 0
                else:
                    temp = int(next_start.pop())
                subnetsList.extend(list[3][int(temp):int(temp)+list_values[i]])
                if((i+1) < len(list_keys)):
                    if(list_keys[i+1]==254):
                        if(i==3):  #14,30,62,126,256,...
                            next_start.append( int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4))\
                                          + int(math.ceil(list_values[i-2]/8)) +int(math.ceil(list_values[i-3]/16)))
                        elif(i==2):   #14,62,126,254 or 30,62,126,254 or 14,30,126,256
                            if(list_keys[i-2]==14 and list_keys[i-1]==62): #14,62,126,256,...
                                next_start.append( int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4))\
                                              + int(math.ceil(list_values[i-2]/16)))
                            elif(list_keys[i-2]==30 and list_keys[i-1]==62): #30,62,126,256,...
                                next_start.append( int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4)) \
                                              + int(math.ceil(list_values[i-2]/8)))
                            else:#14,30,126,...
                                next_start.append(int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/8))\
                                              +int(math.ceil(list_values[i-1]/16)))
                        elif(i==1):   #14,126,254 or 30,126,254 or 62,126,254
                            if(list_keys[i-1]==14): #14,126,256,...
                                next_start.append(int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/16)))

                            elif(list_keys[i-1]==30): #30,126,256,...
                               next_start.append( int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/8)))

                            else:#62,126,...
                                next_start.append( int(math.ceil(list_values[i]/2)) + int(math.ceil(list_values[i-1]/4)))

                        else:
                             next_start.append(int(math.ceil(list_values[i]/2)))

            else:
                if(i==0):
                    temp = 0
                else:
                    temp = int(next_start.pop())
                subnetsList.extend(list[4][int(temp):int(temp)+list_values[i]])

        return subnetsList

    def getRandomCombination(self,totalHost):
         # select every combinations randomly
        list = [14,30,62,126,254]
        combinations = dict([])

        if(totalHost<=14):
            combinations = dict([('14',1)])

        elif(totalHost>14 and totalHost<=30):
            combinations = dict([('14',2)])

        elif(totalHost>30 and totalHost <=62):
            sublist = list[0:2]
            while(1):
                random1 = random.random()
                random2 = random.random()
                if(random1 >= 0.5 or random2 >=0.5):
                    break;

            if(random1>=0.5 and random2<0.5):
                number = int(totalHost/sublist[0]) +1
                combinations=dict([(sublist[0],number)])
            elif(random1<0.5 and random2 >=0.5):
                number = int(totalHost/sublist[1]) +1
                combinations = dict([(sublist[1],number)])
            else:
                temp = totalHost - sublist[1]
                number = int(totalHost / sublist[0]) +1
                combinations = dict([ (sublist[0],1) , (sublist[1],number) ])

        else:       #(totalHost>62 and totalHost <=2046):

            for index in range(5,0,-1):
                max_possible = int(totalHost/list[index-1]) +1

                if index==1:
                    combinations[list[index-1]]  = max_possible
                elif(max_possible>=2):
                    probability = random.random()
                    if(probability>=0.5):  # if probability >= 0.5 , select that subnet
                        number = int(random.uniform(1,max_possible))
                        totalHost = totalHost -(number*list[index-1])
                        combinations[list[index-1]]=number

        return combinations













s = Subnet()
list = s.createSubnets(1006)

print(len(list))
print(list)