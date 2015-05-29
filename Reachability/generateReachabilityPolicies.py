__author__ = 'vishlesh'

#!/usr/bin/env python3
import sys
sys.path.append('/home/vishlesh/SDN_RuleSetGenerator')

from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.Reachability.TraverseSourceInfoGraph import *

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hosts","-nh", default = "1000", help="No. of hosts you want in your network" )
    parser.add_argument("--policyType","-t",default = "light",
                        help = "To create policy light network, argument: 'light' " + '\n' +
                               "To create policy heavy network, argument: 'heavy' ")

    args = parser.parse_args()

    print("hosts:",args.hosts)
    print("policy type:",args.policyType)
    file_reachablityPolicies = open('ReachabilityPolicies.txt','w').close()
    file_reachablityPolicies = open('ReachabilityPolicies.txt','w')

    s = Subnet()
    subnetList = s.createSubnets(int(args.hosts))
    print("total no. of subnets created in the network:",len(subnetList))
    totalPolicyUnits = 0
    if args.policyType == "light":
        destinationGraph = [(60,50),(100,100)]
        sourceGraph = [(17,50),(100,100)]
        totalPolicyUnits = 2
    else:
        destinationGraph = [(1,13),(3,37),(5,50),(6,59),(7,65),(8,70),(10,75),(18,80),(19,88),(20,90),(21,94),(54,98),(75,100)]
        sourceGraph = [(1,1),(1,2),(2,4),(2.3,10),(2.4,12),(2.5,15),(2.6,18),(2.7,20),(2.8,23),(2.9,26),
               (3,29),(3.1,32),(3.7,35),(4.5,38),(5,40),(6,42),(7,44),(8,46),(9,48),(10,50),(11,52),
               (12,54),(13,56),(14,58),(15,60),(17,63),(19,66),(20,70),(22,73),(24,76),(26,80),
               (28,82),(29,84),(30,87),(31,90),(33,92),(34,96),(100,100)]
        totalPolicyUnits =40

    destinationInfoObj = DestInfo()
    sourceInfoObj = SourceInfo()
    list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicyUnits,subnetList)
    print("total policy units: ",len(list_PolicyUnits))
    fwd_policies = []
    fwd_policies=sourceInfoObj.traverseSourceInfoGraph(sourceGraph,list_PolicyUnits,subnetList)
    print("total no. of end point reachability policies: ",len(fwd_policies))
    print("set of destinations: ",destinationInfoObj.set_selectedDestIPs)

    for each_forward_policy in fwd_policies:
          string= str(each_forward_policy.getSource()) + str(', '+str(each_forward_policy.getDest())) \
                                             + str(', '+str(each_forward_policy.getAction())+'\n')
          print(string)
          file_reachablityPolicies.write(string) ##writing into file


if __name__ == '__main__':
    main()
