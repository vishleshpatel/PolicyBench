__author__ = 'vishlesh'

from subnet import *
from  TraverseDestInfoGraph import *

class script:


    def getlist(self,hosts):
        s =Subnet()
        return s.createSubnets(hosts)

s = script()
subnetList = s.getlist(100000)

destinationGraph = [(50,60),(100,100)]
totalPolicies = 2

destinationInfoObj = DestInfo()
list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicies,subnetList)
print(list_PolicyUnits)