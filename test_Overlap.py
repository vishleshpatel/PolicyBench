__author__ = 'vishlesh'

from SDN_RuleSetGenerator.Measurement.MeasurementPolicies import *
from SDN_RuleSetGenerator.Policy import *
from SDN_RuleSetGenerator.Reachability.TraverseSourceInfoGraph import *
from SDN_RuleSetGenerator.Reachability.TraverseDestInfoGraph import *
import ipaddress

class Overlap():
    def __init__(self):
       self.match_count = 0

    def testOverlapInPolicies(self,listReachablityPolicies,listMeasurementPolicies):
        assert isinstance(listMeasurementPolicies,list)
        assert isinstance(listReachablityPolicies,list)

        for each_measure_policy in listMeasurementPolicies:
            for each_forward_policy in listReachablityPolicies:
                match = False
                assert isinstance(each_measure_policy,Policy)
                assert isinstance(each_forward_policy,Policy)
                subnetIPaddr = each_measure_policy.getSource()
                endHost = each_forward_policy.getSource()
                listDestAddr_fwd = list(each_forward_policy.getDest())
                destIPaddr_measure = each_measure_policy.getDest()
                if self.isSourceMatch(endHost,subnetIPaddr)==True:
                    for each_addr in listDestAddr_fwd:
                        if self.isDestMatch(each_addr,destIPaddr_measure):
                            match =True
                            self.match_count =self.match_count+1
                            break
                if(match==True):
                   break

        return self.match_count

    def isSourceMatch(self,endHost,subnetIPaddr):

        for each_addr in subnetIPaddr:
            if each_addr==endHost:
                return True
        return False

    def isDestMatch(self,subnetAddrBig,subnetAddrSmall):

        set1 =([])
        prefix = subnetAddrBig._prefixlen
        subnetList = []
        while(prefix<=31):
            prefix = prefix+1
            subnetList = subnetAddrBig.subnets(new_prefix=prefix)
        set1 = set(subnetList)

        if subnetAddrSmall in set1:
            return True
        else:
            return False