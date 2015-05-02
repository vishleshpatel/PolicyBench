__author__ = 'vishlesh'

from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.Measurement.MeasurementPolicies import *
from SDN_RuleSetGenerator.Policy import *
s = Subnet()
subnetList = s.createSubnets(50000)
m = MeasurementPolicies()
listPolicies = []
listPolicies = m.generateMeasurementPolicies(subnetList,40)
for each_policy in listPolicies:
    assert isinstance(each_policy,Policy)
    print(each_policy.getSource(),"source",each_policy.getDest(),"destination",each_policy.getAction(),"action")
print(len(listPolicies),"finally finished")