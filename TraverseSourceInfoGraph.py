__author__ = 'vishlesh'

from SDN_RuleSetGenerator.TraverseDestInfoGraph import *
from SDN_RuleSetGenerator.Policy import *
import ipaddress

class SourceInfo:

    def __init__(self):
        self.policyPercentageCovered = 0
        self.hostPercentegeCovered=0
        self.setEndHosts =0
        self.endHostsList = []
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
            EndHostsList.append(self.getHosts(each_subnet_addr))

        return EndHostsList


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
        self.endHostsList = self.getAllEndHosts(subnetsList)
        totalNumEndHosts = len(self.endHostsList)

        for (x,y) in sourceInfoGraph:
            numPolicyUnit = self.getNumber_policy(y,totalPolicies)
            numEndHostsToAssign= self.getNumber_endhost(x,totalNumEndHosts)
            endHostsPerPolicyUnit = int(numEndHostsToAssign/numPolicyUnit)
            print((x,y))
            for i in range(0,numPolicyUnit,1):
                 if(i==numPolicyUnit-1): #last iteration
                    endHostsPerPolicyUnit = numEndHostsToAssign #assign remaining endHosts
                 endHostsList_Source =self.getRandomEndhosts(endHostsPerPolicyUnit)
                 self.setSource(list_PolicyUnits[i],endHostsList_Source)
                 numEndHostsToAssign = numEndHostsToAssign - endHostsPerPolicyUnit
                    #endHosts_toAssign = random.sample(endHosts,endHostsPerPolicyUnit)
                    #Remember: source are the intersection, dest are unions
                    #endHosts = self.substract(endHosts,endHosts_toAssign)


        return self.policies

    def getRandomEndhosts(self,endHostsPerPolicyUnit):

        randomEndhosts =[]
        for i in range(0,endHostsPerPolicyUnit,1):
            number = len(self.endHostsList)
            if(number==1):
                endHost=self.endHostsList[0]
                randomEndhosts.append(endHost)
                self.endHostsList.remove(endHost)
                return randomEndhosts
            else:
                num = random.randint(1,number-1)
                endHost = self.endHostsList[num]
                randomEndhosts.append(endHost)
                self.endHostsList.remove(endHost)
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