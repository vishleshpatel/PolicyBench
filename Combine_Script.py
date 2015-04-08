__author__ = 'vishlesh'

from subnet import *
from  TraverseDestInfoGraph import *



s = Subnet()
subnetList = s.createSubnets(100000)

destinationGraph = [(50,60),(100,100)]
totalPolicies = 2

destinationInfoObj = DestInfo()
list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicies,subnetList)
print(len(list_PolicyUnits))
print(list_PolicyUnits)