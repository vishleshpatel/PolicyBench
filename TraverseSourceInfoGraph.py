__author__ = 'vishlesh'

from SDN_RuleSetGenerator.TraverseDestInfoGraph import *
from SDN_RuleSetGenerator.Policy import *
import ipaddress


class SourceInfo:

    def __init__(self):
        self.policyPercentageCovered = 0
        self.hostPercentegeCovered=0
        self.endHostsSet= set([])
        self.policies=[]

    def getAllEndHosts(self,subnetsList):
        """
        Method getAllEndHosts:
        this method gives all endHosts list of the entire network consisting several subnets

        inputs: list of subnet address in the enterprise network
        output: all host addresses available in the enterprise network
        """
        EndHostsList = []
        for each_subnet_addr in subnetsList:
            list =self.getHosts(each_subnet_addr)
            for each_host in list:
                EndHostsList.append(each_host)

        print(len(EndHostsList),"total endhosts in enterprise")
        return set(EndHostsList)


    def getHosts(self,networkAddr):
        """
        Input: Subnet address
        Output: list of host addresses available in that particular subnet
        :rtype : list
        """
        list = []
        for addr in networkAddr:
            list.append(addr)

        list.pop()
        list.pop(0)
        return list


    def traverseSourceInfoGraph(self,sourceInfoGraph,list_PolicyUnits,subnetsList):
        """
        :param sourceInfoGraph: list of points in source Info graph = graph 2
        :param list_PolicyUnits: list of Policy Units generated from method traverseDestInfoGraph
        :param subnetsList: list of subnet address available in enterprise
        :return: Method sets source addresses in the policy unit
        """
        assert isinstance(list_PolicyUnits, list)
        totalPolicies = len(list_PolicyUnits)
        self.endHostsSet = self.getAllEndHosts(subnetsList)

        for (x,y) in sourceInfoGraph:
            totalNumEndHosts = len(self.endHostsSet)
            print(totalNumEndHosts,"lets check")
            numPolicyUnit = self.getNumber_policy(y,totalPolicies)
            numEndHostsToAssign= self.getNumber_endhost(x,totalNumEndHosts)
            endHostsPerPolicyUnit = int(numEndHostsToAssign/numPolicyUnit)
            print(numPolicyUnit,"no. of policy units", numEndHostsToAssign,"no. of end hosts",
                  endHostsPerPolicyUnit,"end hosts per policy unit")
            print((x,y))
            for i in range(0,numPolicyUnit,1):
                 if(i==numPolicyUnit-1): #last iteration
                    endHostsPerPolicyUnit = numEndHostsToAssign #assign remaining endHosts
                 sourceAddressesList =self.getRandomEndhosts(endHostsPerPolicyUnit)
                 self.setSource(list_PolicyUnits[i],sourceAddressesList)
                 numEndHostsToAssign = numEndHostsToAssign - endHostsPerPolicyUnit
                    #endHosts_toAssign = random.sample(endHosts,endHostsPerPolicyUnit)
                    #Remember: source are the intersection, dest are unions
                    #endHosts = self.substract(endHosts,endHosts_toAssign)


        return self.policies

    def getRandomEndhosts(self,endHostsPerPolicyUnit):
        # based on the random.sample method
        print("in getRandomEndhosts")
        print("set of",endHostsPerPolicyUnit,"should be created")
        print(len(self.endHostsSet),"total end hosts")
        randomEndhostsSet =set([])
        randomEndhosts = set(random.sample(self.endHostsSet,endHostsPerPolicyUnit))
        print("got the sample, sample size:",len(randomEndhosts), "random end hosts")
        self.endHostsSet = self.endHostsSet - randomEndhosts
        print(len(self.endHostsSet), "new substracted size of self.endHostsSet")
        return randomEndhosts


    def setSource(self,policyUnit,endHosts_toAssign):
       # assert isinstance(policyUnit,Policy)
        for each_endHost in endHosts_toAssign:
            p=Policy()

            p.setSource(each_endHost)
            p.setAction(policyUnit.getAction())
            p.setDestAccessPoints(policyUnit.getDestAccessPoints())
            self.policies.append(p)

    def substract(self,parentList,subList):
        assert isinstance(parentList, list)

        for each_element in subList:
            parentList.remove(each_element)
        return parentList

    def getNumber_policy(self,percentageY,totalPolicies):

        percentageX = percentageY - self.policyPercentageCovered
        number = int((percentageY/100)*totalPolicies)
        self.policyPercentageCovered =self.policyPercentageCovered + percentageY
        return number

    def getNumber_endhost(self,percentageX,numEndHosts):

        percentageY = percentageX - self.hostPercentegeCovered
        number = int((percentageX/100)*numEndHosts)
        self.hostPercentegeCovered =self.hostPercentegeCovered + percentageX
        return number