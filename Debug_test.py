__author__ = 'vishlesh'

from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.TraverseDestInfoGraph import *
from SDN_RuleSetGenerator.TraverseSourceInfoGraph import *
from SDN_RuleSetGenerator.Policy import *


s = Subnet()
subnetList = s.createSubnets(100000)
print(subnetList)
print("total no. of subnets created:",len(subnetList))

destinationGraph = [(60,50),(100,100)]
totalPolicies = 2

destinationInfoObj = DestInfo()
sourceInfoObj = SourceInfo()
list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicies,subnetList)
policies = []
sourceGraph = [(17,50),(100,100)]
policies=sourceInfoObj.traverseSourceInfoGraph(sourceGraph,list_PolicyUnits,subnetList)
print(len(list_PolicyUnits),"total policy units")
for each_policy in list_PolicyUnits:
    print(each_policy.getDestAccessPoints())
    print(each_policy.getAction())
print(len(policies),"total no. of end point reachability policies")
"""
for each_policy in policies:
    print(each_policy.getSource)
    print(each_policy.getDestAccessPoints(each_policy))
    print(each_policy.getAction(each_policy))
"""

