__author__ = 'vishlesh'


from SDN_RuleSetGenerator.Action import *

class Policy:
    def __init__(self):

        destinationAccessPoints = None
        source = None
        action = None

    def setDestAccessPoints(self,listDestAP):
        self.destinationAccessPoints = listDestAP
    def getDestAccessPoints(self):
        return self.destinationAccessPoints

    def setAction(self,action):
        self.action = action
    def getAction(self):
        return self.action

    def setSource(self,source):
        self.source = source
    def getSource(self):
        return self.source