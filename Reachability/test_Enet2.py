__author__ = 'vishlesh'


from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.Reachability.TraverseSourceInfoGraph import *

# usage enter No. of hosts in the network should be given to s.createSubnets(number of End host)
s = Subnet()
subnetList = s.createSubnets(50000)
print("subnets:",subnetList)
print("total no. of subnets created:",len(subnetList))

destinationGraph = [(1,13),(3,37),(5,50),(6,59),(7,65),(8,70),(10,75),(18,80),(19,88),(20,90),(21,94),(54,98),(75,100)]
totalPolicyUnits = 40

destinationInfoObj = DestInfo()
sourceInfoObj = SourceInfo()
list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicyUnits,subnetList)
print(len(list_PolicyUnits),"total policy units")
policies = []
sourceGraph = [(1,1),(1,2),(2,4),(2.3,10),(2.4,12),(2.5,15),(2.6,18),(2.7,20),(2.8,23),(2.9,26),
               (3,29),(3.1,32),(3.7,35),(4.5,38),(5,40),(6,42),(7,44),(8,46),(9,48),(10,50),(11,52),
               (12,54),(13,56),(14,58),(15,60),(17,63),(19,66),(20,70),(22,73),(24,76),(26,80),
               (28,82),(29,84),(30,87),(31,90),(33,92),(34,96),(100,100)]
policies=sourceInfoObj.traverseSourceInfoGraph(sourceGraph,list_PolicyUnits,subnetList)

for each_policy in list_PolicyUnits:
    print(each_policy.getDestAccessPoints())
    print(each_policy.getAction())

print(len(policies),"total no. of end point reachability policies")
"""
for each_policy in policies:
    print(each_policy.getSource())
    print(each_policy.getDestAccessPoints())
    print(each_policy.getAction())
"""