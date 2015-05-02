__author__ = 'vishlesh'


from SDN_RuleSetGenerator.Action import *

class Policy:
    def __init__(self):

        self.destinationAccessPoints = None
        self.destination =None
        self.source = None
        self.action = None

    def setDestAccessPoints(self,listDestAP):
        self.destinationAccessPoints = listDestAP
    def getDestAccessPoints(self):
        return self.destinationAccessPoints

    def setDest(self,dest):
        self.destination = dest
    def getDest(self):
        return self.destination

    def setAction(self,action):
        self.action = action
    def getAction(self):
        return self.action

    def setSource(self,source):
        self.source = source
    def getSource(self):
        return self.source