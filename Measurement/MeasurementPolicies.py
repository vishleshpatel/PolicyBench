__author__ = 'vishlesh'

import random
import ipaddress
from SDN_RuleSetGenerator.Policy import *
from SDN_RuleSetGenerator.Measurement.createTree import *

class MeasurementPolicies():
    def __init__(self):
        self.listPolicies = []

    def generateMeasurementPolicies(self, subnetsList, resources):
        resourcesLeft = resources
        while(resourcesLeft>0):
            randomNo = random.randint(0,len(subnetsList)-1)
            sourceIP =  subnetsList[randomNo]
            subnetsList.pop(randomNo)
            randomNo = random.randint(0,len(subnetsList)-1)
            destIP =subnetsList[randomNo]
            subnetsList.pop(randomNo)
            c = CreateTree()
            tree = c.createTree(sourceIP,destIP)
            print(tree.height(),"height",
                  tree.rootNode.srcIP,"root node srcIP",
                  tree.rootNode.dstIP,"root node dstIP",
                  tree.elements_count,"total nodes in tree")
            while(1):
                noPolicy = random.randint(1,resourcesLeft)
                if(noPolicy<tree.elements_count):
                    print("no of Policy:",noPolicy,"total elements:",tree.elements_count,
                          "resources left",resourcesLeft)
                    break

            listNodes = self.randomPickNodes(noPolicy,tree)
            resourcesLeft = resourcesLeft - noPolicy
            self.addMeasurementPolicies(listNodes)
        return self.listPolicies

    def addMeasurementPolicies(self,listNodes):

        for each_node in listNodes:
            assert isinstance(each_node,Node)
            p=Policy()
            p.setDest(each_node.dstIP)
            a = Action(3)   # action type: count
            p.setAction(a)
            p.setSource(each_node.srcIP)
            self.listPolicies.append(p)


    def randomPickNodes(self, noNodes, tree):
        """
        :param noNodes: number of nodes to pick
        :param tree: binary tree
        :return:
        """
        list1 = tree.inorder_non_recursive()
        #print(len(list1),"list of all elements in tree")
        returnList = []
        while(noNodes>0):
            node = random.choice(list1)
            returnList.append(node)
            noNodes=noNodes-1
        return returnList


