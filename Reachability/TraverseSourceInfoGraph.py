__author__ = 'vishlesh'

from SDN_RuleSetGenerator.Reachability.TraverseDestInfoGraph import *
from SDN_RuleSetGenerator.Policy import *


class SourceInfo:

    def __init__(self):
        self.policyPercentageCovered = 0
        self.hostPercentegeCovered=0
        self.endHostsSet= set([])
        self.policies=[]
        self.set_selectedSrcIPs = set([])

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
        totalPolicyUnits = len(list_PolicyUnits)
        self.endHostsSet = self.getAllEndHosts(subnetsList)

        for (x,y) in sourceInfoGraph:
            totalNumEndHosts = len(self.endHostsSet)
            #numPolicyUnit: number of policy units needs to fill up by sourceIPs in this iteration
            numPolicyUnit = self.getNumber_policy(y,totalPolicyUnits)   
            # numEndHostsToAssign = number of [end hosts = sources] needs to assign to bunch of policy units  
            numEndHostsToAssign= self.getNumber_endhost(x,totalNumEndHosts)
            # endHosts / sources per policy unit
            sourcesPerPolicyUnit = int(numEndHostsToAssign/numPolicyUnit)

            if(((x,y)==sourceInfoGraph[len(sourceInfoGraph)-1]) or numPolicyUnit>=len(list_PolicyUnits)):
                 numPolicyUnit=len(list_PolicyUnits)
                 sourcesPerPolicyUnit = int(len(self.endHostsSet)/numPolicyUnit)
                 for i in range(0,numPolicyUnit,1):
                      #last iteration
                     sourceAddressesList =self.getRandomEndhosts(sourcesPerPolicyUnit)
                     self.setSource(list_PolicyUnits[i],sourceAddressesList)
                    # update set of selected sourceIPs
                     self.set_selectedSrcIPs.update(sourceAddressesList)
                 return self.policies

            for i in range(0,numPolicyUnit,1):
                 if(i==numPolicyUnit-1): #last iteration
                    sourcesPerPolicyUnit = numEndHostsToAssign #assign remaining endHosts
                 sourceAddressesList =self.getRandomEndhosts(sourcesPerPolicyUnit)
                 self.setSource(list_PolicyUnits[i],sourceAddressesList)
                 # update set of selected sourceIPs
                 self.set_selectedSrcIPs.update(sourceAddressesList)
                 numEndHostsToAssign = numEndHostsToAssign - sourcesPerPolicyUnit

            for i in range(0,numPolicyUnit,1):
                list_PolicyUnits.pop(i)

        return self.policies

    def getRandomEndhosts(self,sourcesPerPolicyUnit):
        # based on the random.sample method
        randomEndhostsSet=set([])
        randomEndhosts = set(random.sample(self.endHostsSet,sourcesPerPolicyUnit))
        self.endHostsSet = self.endHostsSet - randomEndhosts
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
        percentageY = percentageY - self.policyPercentageCovered
        number=(percentageY/100)*totalPolicies
        number = int(number)
        if(number==0):
            number = 1
        self.policyPercentageCovered =self.policyPercentageCovered + percentageY
        return number

    def getNumber_endhost(self,percentageX,numEndHosts):

        percentageX= percentageX - self.hostPercentegeCovered
        number = int((percentageX/100)*numEndHosts)
        self.hostPercentegeCovered =self.hostPercentegeCovered + percentageX
        return number