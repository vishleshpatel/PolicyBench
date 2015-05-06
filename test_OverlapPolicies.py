__author__ = 'vishlesh'

from SDN_RuleSetGenerator.Measurement.MeasurementPolicies import *
from SDN_RuleSetGenerator.Reachability import *
from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.Reachability.TraverseSourceInfoGraph import *
from SDN_RuleSetGenerator.test_Overlap import *

# usage enter No. of hosts in the network should be given to s.createSubnets(number of End host)
s = Subnet()
subnetList = s.createSubnets(50000)
print(subnetList)
print("total no. of subnets created:",len(subnetList))

destinationGraph = [(60,50),(100,100)]
totalPolicies = 2

destinationInfoObj = DestInfo()
sourceInfoObj = SourceInfo()
list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicies,subnetList)
print(len(list_PolicyUnits),"total policy units")
policies = []
sourceGraph = [(17,50),(100,100)]

fwd_policies=sourceInfoObj.traverseSourceInfoGraph(sourceGraph,list_PolicyUnits,subnetList)

"""
for each_policy in list_PolicyUnits:
    print(each_policy.getDestAccessPoints())
    print(each_policy.getAction())
"""
print(len(fwd_policies),"total no. of end point reachability policies")


#print("set of sources: ", sourceInfoObj.set_selectedSrcIPs)
#print("total no. of selected sources:", len(sourceInfoObj.set_selectedSrcIPs))
#print(sourceInfoObj.set_selectedSrcIPs.pop())

#print("total no. of selected destination IPs",len(destinationInfoObj.set_selectedDestIPs))
print("set of destinations: ",destinationInfoObj.set_selectedDestIPs)

print("measurement policy part")
m = MeasurementPolicies()
listMeasurePolicies = []
listMeasurePolicies = m.generateMeasurementPolicies(subnetList,destinationInfoObj.set_selectedDestIPs,40)
for each_policy in listMeasurePolicies:
    assert isinstance(each_policy,Policy)
    print(each_policy.getSource(),"source",each_policy.getDest(),"destination",each_policy.getAction(),"action")
print(len(listMeasurePolicies),"finally finished")

o = Overlap()
list_match_count = o.testOverlapInPolicies(fwd_policies,listMeasurePolicies)
print(list_match_count,"list of match count")
print(len(list_match_count))
count = 0
for each_element in list_match_count:
    count=count+1
print(count,"total count")
