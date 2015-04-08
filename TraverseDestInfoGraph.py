__author__ = 'vishlesh'

import random
import math
from enum import Enum

class DestInfo:
    def __init__(self):
        self.percentageCovered =0

    """
    AP = Access Point
    access points are routers
    """


    def traverseDestInfoGraph(self,destInfoGraph,totalPolicies,subnetsList):

        accessPoints=self.createAccessPoints(subnetsList)
        totalAccessPoints = len(accessPoints)
        list_PolicyUnits = []
        for (x,y) in destInfoGraph:
            numberPoliciesToCreate = self.getNumber_policy(x,totalPolicies)
            number_spannedAPs = self.getSpannedDeviceNumber(y,totalAccessPoints)
            list_PolicyUnits.extend( self.createPolicyUnits(numberPoliciesToCreate,number_spannedAPs,accessPoints))

        return list_PolicyUnits

    def createPolicyUnits(self,numberPolicies,number_spannedAPs,accessPoints):
        policyUnits = []

        for index in range(0,numberPolicies,1):
            accessPoints_Policy = random.sample(accessPoints,number_spannedAPs)
            p = policy()
            p.setDestAccessPoints(accessPoints_Policy)
            a = action(1)
            p.setAction(a)
            policyUnits.append(p)

        return policyUnits

    def getNumber_policy(self,percentageX,totalPolicies):

        percentageX = percentageX - self.percentageCovered
        number = int((percentageX/100)*totalPolicies)
        self.totaPercentageCovered =self.percentageCovered + percentageX
        return number

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



class policy:
    def __init__(self):
        destinationAccessPoints = None
        source = None
        action = None

    def setDestAccessPoints(self,listDestAP):
        self.destinationAccessPoints = listDestAP

    def setAction(self,action):
        self.action = action

    def setSource(self,source):
        self.source = source


class action(Enum):
    forward = 1
    drop =2