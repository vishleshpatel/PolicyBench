__author__ = 'vishlesh'
#!/usr/bin/env python3
import sys
sys.path.append('/home/vishlesh/SDN_RuleSetGenerator')
from SDN_RuleSetGenerator.Measurement.MeasurementPolicies import *
from SDN_RuleSetGenerator.Reachability import *
from SDN_RuleSetGenerator.subnet import *
from SDN_RuleSetGenerator.Policy import *
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--hosts","-nh", default = "1000", help="No. of hosts you want in your network" )
    parser.add_argument("--measurePolicies", "-c", default= "40",
                        help="enter no. of measurement policies to create")

    args = parser.parse_args()
    print("hosts:",args.hosts)
    print("Number of measurement policies: ", args.measurePolicies)

    file_measurementPolicies = open('MeasurementPolicies.txt','w').close()
    file_measurementPolicies = open('MeasurementPolicies.txt','w')

    s = Subnet()
    subnetList = s.createSubnets(int(args.hosts))
    m = MeasurementPolicies()
    listPolicies = []
    listPolicies = m.generateMeasurementPolicies(subnetList,set(subnetList),int(args.measurePolicies))
    for each_measure_policy in listPolicies:
        assert isinstance(each_measure_policy,Policy)
        string= str(each_measure_policy.getSource()) + str(', '+str(each_measure_policy.getDest())) \
                                             + str(', '+str(each_measure_policy.getAction())+'\n')
        print(string)
        file_measurementPolicies.write(string)  ## writing into file

    print("total no. of measurement policies",len(listPolicies))


if __name__ == '__main__':
    main()
