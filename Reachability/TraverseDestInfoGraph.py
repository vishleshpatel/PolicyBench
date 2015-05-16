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

            ### if statement for corner(last) case
            if((x,y)==destInfoGraph[len(destInfoGraph)-1]):
                numPolicyUnitsToCreate=totalPolicyUnits - allocatedPolicyUnits

            ### num_spannedAPs = spanned routers/access points per policy units
            num_spannedAPs = self.getSpannedDeviceNumber(x,totalAccessPoints)
            if numPolicyUnitsToCreate==0:
                continue

            list_PolicyUnits.extend(self.createPolicyUnits(numPolicyUnitsToCreate,num_spannedAPs,accessPoints))
            allocatedPolicyUnits = allocatedPolicyUnits + numPolicyUnitsToCreate
        return list_PolicyUnits

    def getNumber_policy(self,percentageY,totalPolicyUnits):

        percentageY = percentageY - self.percentageCovered
        number =(percentageY/100)*totalPolicyUnits
        if(number<1):
            return 0
        else:
            number = int(number)
        self.percentageCovered =self.percentageCovered + percentageY
        return number


    def createPolicyUnits(self,numPolicyUnits,num_spannedAPs,accessPoints):

        policyUnits = []
        # from DestGraph, we can just set Destinations and actions for Policy Units
        for index in range(0,numPolicyUnits,1):
            #### accessPointsInCurrentPolicyUnit = accessPoints spanned in the current policy units
            accessPointsInCurrentPolicyUnit=random.sample(accessPoints,num_spannedAPs)
            list_subnetAddr = []
            # get all subnets
            for each_router in accessPointsInCurrentPolicyUnit:
                list_subnetAddr.extend(each_router)
            p = Policy()
            p.setDest(list_subnetAddr)
            a = Action(1)   # action type: forward
            p.setAction(a)
            policyUnits.append(p)

            ### Update set_selectedDestIPs
            subSet_destIPs = set([])
            ### add each subnet address in  accessPointsInCurrentPolicyUnit,
            ### add that subnet address into set_selectedDestIps
            self.set_selectedDestIPs.update(set(list_subnetAddr))
            #subSet_destIPs = list(sublist_destIPs)
            #self.set_selectedDestIPs.update(subSet_destIPs)

        return policyUnits

    def getSpannedDeviceNumber(self,percentageX,totalAccessPoints):
        number = int(math.ceil((percentageX/100)*totalAccessPoints))
        return number

    def createAccessPoints(self,subnetsList):
        """

        :param subnetsList:
        :return:

         #make a group of 15-20 subnets and assign that group of subnets to one router / access point
         #From paper: we say a policy unit "spans" a router if any of the end points that
         #are part of the policy unit are connected directly to that router
        """

        totalSubnets = len(subnetsList)
        totalAccessPoints = random.randint(15,20)

        subnetsPerAP = int(math.ceil(totalSubnets/totalAccessPoints))

        accessPoints = []
        start = 0
        for index in range(0,totalAccessPoints,1):
            accessPoints.append(subnetsList[start:start+subnetsPerAP])
            start = start + subnetsPerAP
        return accessPoints

