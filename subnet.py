__author__ = 'Vishlesh.Patel'


import ipaddress

import math
import random



class Subnet:
    ''''
    2 Methods in Class Subnet: createEqualSubnets, createSubnets

    1.  createEqualSubnets: creates all subnets having equal no. of hosts
        :argument1 hostsPerSubnets :  no. of hosts in 1 subnet-allowed values - 14,30,62,126,254 ==> 2^n - 2
        :argument2 totalHosts : total no. of end points in entire network
        :return list of subnets having equal no. of hosts in it

    2. createSubnets: creates subnets having unequal no. of hosts
        :argument  totalHosts : total no. of end points in entire network
        :return list of subnets having unequal no. of hosts in it
    '''''

    def createEqualSubnets(self, totalHosts, hostsPerSubnet):

        if(hostsPerSubnet != (14 or 30 or 62 or 126 or 254)):

            numberOfSubnets = int(totalHosts / hostsPerSubnet) +1
            subnetHostMask = (int(math.log2(hostsPerSubnet))+1)

            networkIP = ipaddress.IPv4Network('10.0.0.0/15')
            subnetsList = self.getList(networkIP,subnetHostMask)
            return list(subnetsList[0:numberOfSubnets])
        else:
            print("syntax: createEqualSubnets( totalHosts<262144, hostsPerSubnet = 14,30,62,126 or 254")

    # creates list of subnets
    # subnetHostMask : host mask of the subnet
    def getList(self,networkAddr, subnetHostMask):
        return list(networkAddr.subnets(prefixlen_diff=17-subnetHostMask))


    def createSubnets(self, totalHosts):
        if(totalHosts>262144):
            print("error: maximum total hosts allowed : 262144")
            return None

        networkIP = ipaddress.ip_network("10.0.0.0/15",strict=False)
        list = []   # list of subnets - list of different sizes
        subnetsList = []


        list.append( self.getList(networkIP,4))   #list of possible subnets , each subnet contains 14 end hosts
        list.append(self.getList(networkIP,5))    #subnets with 30 end hosts
        list.append(self.getList(networkIP,6))    #62
        list.append(self.getList(networkIP,7))  #126
        list.append(self.getList(networkIP,8))  #254

        combination = self.getRandomCombination(totalHosts)
        #print(combination)
        combination = sorted(combination.items())
        print("here is the combinations in a shorted manner:",combination)

        list_keys = []
        list_values = []
        for (x,y) in combination:
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
                    start = 0
                else:
                    start = int(next_start.pop())
                subnetsList.extend(list[1][start:start+list_values[i]])
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
                    start = 0
                else:
                    start = int(next_start.pop())
                subnetsList.extend(list[2][start:start+list_values[i]])
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
                    start = 0
                else:
                    start = int(next_start.pop())
                subnetsList.extend(list[3][int(start):int(start)+list_values[i]])
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
                    start = 0
                else:
                    start = int(next_start.pop())
                subnetsList.extend(list[4][int(start):int(start)+list_values[i]])

        return subnetsList

    # input: total no. of end hosts in network
    # output : random combination of subnets
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
                number = int(math.ceil(totalHost/sublist[0]))
                combinations=dict([(sublist[0],number)])
            elif(random1<0.5 and random2 >=0.5):
                number = int(math.ceil(totalHost/sublist[1]))
                combinations = dict([(sublist[1],number)])
            else:
                temp = totalHost - sublist[1]
                number = int(math.ceil(totalHost/sublist[0]))
                combinations = dict([ (sublist[0],1) , (sublist[1],number) ])

        else:       #(totalHost>62 and totalHost <=2046):

            for index in range(5,0,-1):
                max_possible = int(math.ceil(totalHost/list[index-1]))

                if index==1:
                    combinations[list[index-1]]  = max_possible
                elif(max_possible>=2):
                    probability = random.random()
                    if(probability>=0.5):  # if probability >= 0.5 , select that subnet
                        number = int(random.uniform(1,max_possible))
                        totalHost = totalHost -(number*list[index-1])
                        combinations[list[index-1]]=number

        return combinations

