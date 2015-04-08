__author__ = 'vishlesh'

from TraverseDestInfoGraph import *
import ipaddress

class SourceInfo:

    def __init__(self):
        self.policyPercentageCovered = 0
        self.hostPercentegeCovered=0
        self.setEndHosts =0

    def getAllEndHosts(self,subnetsList):
        EndHostsList = []

        for each_subnet_addr in subnetsList:
            EndHostsList.append(self.getHosts(each_subnet_addr))

        return EndHostsList

    def getHosts(self,networkAddr):
        """
        :rtype : list
        """
        list = []
        for addr in networkAddr:
            list.append(addr)

        list.pop()
        list.pop(0)
        return list


    def traverseSourceInfoGraph(self,sourceInfoGraph,list_PolicyUnits,subnetsList):
        assert isinstance(list_PolicyUnits, list)

        totalPolicies = len(list_PolicyUnits)
        endHosts = []
        endHosts = self.getAllEndHosts(subnetsList)
        totalNumEndHosts = len(endHosts)

        for (x,y) in sourceInfoGraph:
            numPolicyUnit = self.getNumber_policy(x,totalPolicies)
            numEndHostsToAssign= self.getNumber_endhost(y,totalNumEndHosts)
            endHostsPerPolicyUnit = int(numEndHostsToAssign/numPolicyUnit)

            for i in range(0,numPolicyUnit,1):
                if(i==numPolicyUnit-1): #last iteration
                    endHostsPerPolicyUnit = numEndHostsToAssign

                endHosts_toAssign = random.sample(endHosts,endHostsPerPolicyUnit)
            #Remember: source are the intersection, dest are unions
                endHosts = self.substract(endHosts,endHosts_toAssign)
                self.setSource(list_PolicyUnits[i],endHosts_toAssign)
                numEndHostsToAssign = numEndHostsToAssign - endHostsPerPolicyUnit

    def setSource(self,policy, endHosts_toAssign):
        assert isinstance(policy,policy)
        policy.setSource(endHosts_toAssign)

    def substract(self,parentList,subList):
        assert isinstance(parentList, list)

        for each_element in subList:
            parentList.remove(each_element)
        return parentList

    def getNumber_policy(self,percentageX,totalPolicies):

        percentageX = percentageX - self.policyPercentageCovered
        number = int((percentageX/100)*totalPolicies)
        self.totaPercentageCovered =self.percentageCovered + percentageX
        return number

    def getNumber_endhost(self,percentageY,numEndHosts):

        percentageY = percentageY - self.hostPercentegeCovered
        number = int((percentageY/100)*numEndHosts)
        self.hostPercentegeCovered =self.hostPercentegeCovered + percentageY
        return number