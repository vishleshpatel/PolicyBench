__author__ = 'vishlesh'

from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.Measurement.MeasurementPolicies import *
from SDN_RuleSetGenerator.Policy import *
s = Subnet()
subnetList = s.createSubnets(50000)
m = MeasurementPolicies()
listPolicies = []
listPolicies = m.generateMeasurementPolicies(subnetList,set(subnetList),40)
for each_policy in listPolicies:
    assert isinstance(each_policy,Policy)
    print("source:",each_policy.getSource(),"destination:",each_policy.getDest(),"action:",each_policy.getAction())
print(len(listPolicies),"finally finished")