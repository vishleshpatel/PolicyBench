__author__ = 'vishlesh'

import ipaddress
import random
from SDN_RuleSetGenerator.Measurement.BinaryTree import *
class CreateTree:

    def createTree(self, srcIP, dstIP):

        key = 1
        n = Node(key,srcIP,dstIP)
        t = AVLTree(n)
        srcVisitList =[]   # list of sourceIPs which are visited in next iteration
        srcAddList =[]     # list of sourceIPs whichs will be inserted in tree now in this iteration
        dstVisitList = []
        dstAddList = []

        while(1):
            side_flipcoin = random.randint(0,1)

            ## flip the coin and randomly choose to divide srcIP or dstIP
            if(srcIP._prefixlen==32 and dstIP._prefixlen==32):
                #print("tree completely created","key =",key)
                break
            else:
                if(side_flipcoin==0):
                    if(srcIP._prefixlen == 32):
                        continue

                    srcAddList.extend(list(srcIP.subnets()))
                    #print(srcAddList)
                    srcVisitList.extend(list(srcIP.subnets()))
                    key = key+1
                    srcIP = srcAddList.pop(0)
                    treeNode1 = Node(key,srcIP,dstIP)
                    t.insert_node(treeNode1)
                    key = key+1
                    srcIP = srcAddList.pop()
                    treeNode2 = Node(key,srcIP,dstIP)
                    t.insert_node(treeNode2)
                    srcIP = srcVisitList.pop(0)
                else:
                    if(dstIP._prefixlen == 32):
                        continue

                    dstAddList.extend(list(dstIP.subnets()))
                    dstVisitList.extend(list(dstIP.subnets()))
                    key = key+1
                    dstIP = dstAddList.pop(0)
                    treeNode1 = Node(key,srcIP,dstIP)
                    t.insert_node(treeNode1)
                    key = key+1
                    dstIP = dstAddList.pop()
                    treeNode2 = Node(key,srcIP,dstIP)
                    t.insert_node(treeNode2)
                    dstIP = dstVisitList.pop(0)
                    dstIP=list(dstIP.subnets()).pop(0)
        return t

"""
srcIP = ipaddress.ip_network('10.0.0.0/24')
dstIP = ipaddress.ip_network('10.0.0.0/24')
c = CreateTree()
tree = c.createTree(srcIP,dstIP)
print(tree.height())
print(tree.elements_count,"total count")
Node = tree.find(2)
print(Node.key,Node.srcIP,Node.dstIP)
"""