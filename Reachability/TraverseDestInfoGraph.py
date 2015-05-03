__author__ = 'vishlesh'

import random
import math
from SDN_RuleSetGenerator.Policy import *
from SDN_RuleSetGenerator.Action import *

class DestInfo:
    def __init__(self):
        self.percentageCovered =0
        # save selected destination IPs for policy overlap
        self.set_selectedDestIPs =set([])


    def traverseDestInfoGraph(self,destInfoGraph,totalPolicyUnits,subnetsList):
        """
        Method: traverseDestInfoGraph

        Inputs:
        :arg1 destInfoGraph - list of points in DestInfo graph
        :arg2 totalPolicyUnits - total no. of policy units
        :arg3 subnetsList - list of subnets in the network
        subnetsList can be obtained by createSubnets and createEqualSubnets methods

        :returns list_PolicyUnits : list of policy units

        AP = Access Point
        access points are routers
        """

        allocatedPolicyUnits=0
        accessPoints=self.createAccessPoints(subnetsList)
        totalAccessPoints = len(accessPoints)
        list_PolicyUnits = []
        for (x,y) in destInfoGraph:
            numPolicyUnitsToCreate = self.getNumber_policy(y,totalPolicyUnits)
            if((x,y)==destInfoGraph[len(destInfoGraph)-1]):
                numPolicyUnitsToCreate=totalPolicyUnits - allocatedPolicyUnits
            number_spannedAPs = self.getSpannedDeviceNumber(x,totalAccessPoints)
            if numPolicyUnitsToCreate==0:
                continue
            list_PolicyUnits.extend(self.createPolicyUnits(numPolicyUnitsToCreate,number_spannedAPs,accessPoints))
            allocatedPolicyUnits = allocatedPolicyUnits + numPolicyUnitsToCreate
        return list_PolicyUnits

    def getNumber_policy(self,percentageX,totalPolicyUnits):

        percentageX = percentageX - self.percentageCovered
        number =(percentageX/100)*totalPolicyUnits
        if(number<1):
            return 0
        else:
            number = int(number)
        self.percentageCovered =self.percentageCovered + percentageX
        return number


    def createPolicyUnits(self,numPolicyUnits,number_spannedAPs,accessPoints):

        policyUnits = []
        # from DestGraph, we can just set Destinations and actions for Policy Units
        for index in range(0,numPolicyUnits,1):
            accessPoints_Policy = random.sample(accessPoints,number_spannedAPs)
            p = Policy()
            p.setDestAccessPoints(accessPoints_Policy)
            self.set_selectedDestIPs.update(accessPoints_Policy)
            a = Action(1)   # action type: forward
            p.setAction(a)
            policyUnits.append(p)
        return policyUnits

    def getSpannedDeviceNumber(self,percentageY,totalAccessPoints):
        number = int(math.ceil((percentageY/100)*totalAccessPoints))
        return number

    def createAccessPoints(self,subnetsList):

        totalSubnets = len(subnetsList)
        totalAccessPoints = random.randint(15,20)
        subnetsPerAP = int(math.ceil(totalSubnets/totalAccessPoints))

        accessPoints = []
        start = 0
        for index in range(0,totalAccessPoints,1):
            accessPoints.append(subnetsList[start:start+subnetsPerAP])
            start = start + subnetsPerAP
        return accessPoints

