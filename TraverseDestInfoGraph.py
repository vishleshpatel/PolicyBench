__author__ = 'vishlesh'

class DestInfo:
    def __init__(self):
        totalPercentageCovered =0
        totalSpannedDevices= 0

    def traverseDestInfoGraph(self,destInfoGraph,totalPolicies,subnetsList):

        totalAccessPoints =self.createAccesspoints(subnetsList)
        for (x,y) in destInfoGraph:
            numberPoliciesToCreate = self.getNumber(x,totalPolicies)
            spannedEndHosts = self.getSpannedDeviceNumber(y,totalAccessPoints)
            PolicyUnits = self.cretePolicyUnits(numberPoliciesToCreate,spannedEndHosts)

        return PolicyUnits

    def getNumber(self,percentageX,totalPolicies):

        percentageX = percentageX - self.totalPercentageCovered
        number = (percentageX/100)*totalPolicies
        self.totalpercentageCovered =self.totalpercentageCovered + percentageX
        return number

    def getSpannedDeviceNumber(self,percentageY,totalAccessPoints):
        number = (percentageY/100)*totalAccessPoints
        return number

    def createAccessPoints(self,subnetsList):
        #to be implemented


        AccessPoints = list([])
        return AccessPoints

    def createPolicyUnits(self,numberPolicies,destAccessPoints):
