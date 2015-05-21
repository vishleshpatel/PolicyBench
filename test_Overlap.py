__author__ = 'vishlesh'

from SDN_RuleSetGenerator.Measurement.MeasurementPolicies import *
from SDN_RuleSetGenerator.Policy import *
from SDN_RuleSetGenerator.Reachability.TraverseSourceInfoGraph import *
from SDN_RuleSetGenerator.Reachability.TraverseDestInfoGraph import *
import ipaddress

class Overlap():
    def __init__(self):
       self.list_match_count = []


    def getOverlappedPolicies(self,listReachablityPolicies,listMeasurementPolicies):

        file_measurementPolicies = open('matchedMeasurementPolicies.txt','w').close()
        file_measurementPolicies = open('matchedMeasurementPolicies.txt','w')
        file_reachablityPolicies = open('matchedReachabilityPolicies.txt','w').close()
        file_reachablityPolicies = open('matchedReachabilityPolicies.txt','w')

        assert isinstance(listMeasurementPolicies,list)
        assert isinstance(listReachablityPolicies,list)
        iteration = -1
        for each_measure_policy in listMeasurementPolicies:
            iteration =iteration+1
            print(iteration,"length of list of match counts: ",len(self.list_match_count))
            match = False
            for each_forward_policy in listReachablityPolicies:
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
                            string= str(each_measure_policy.getSource()) + str(', '+str(each_measure_policy.getDest())) \
                                             + str(', '+str(each_measure_policy.getAction())+'\n')
                            print(string)
                            file_measurementPolicies.write(string)

                            string= str(each_forward_policy.getSource()) + str(', '+str(each_forward_policy.getDest())) \
                                             + str(', '+str(each_forward_policy.getAction())+'\n')
                            print(string)
                            file_reachablityPolicies.write(string)
                            if len(self.list_match_count)==iteration:
                                self.list_match_count.append(1)
                            else:
                                count = self.list_match_count[iteration]
                                count=count+1
                                #self.list_match_count.insert(iteration,self.list_match_count[iteration]+1)
                                self.list_match_count[iteration]=count
                            break
            if(match==False):
                self.list_match_count.append(0)
            print("previous count:" ,self.list_match_count[iteration])
        return self.list_match_count

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