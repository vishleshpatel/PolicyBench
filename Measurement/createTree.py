__author__ = 'vishlesh'

import ipaddress
from SDN_RuleSetGenerator.Measurement.BinaryTree import *
class CreateTree:

    def createTree(self, srcIP, dstIP):
       # assert srcIP == ipaddress.ip_network  ##check for the type of srcIP and dstIP
        #assert dstIP == ipaddress.ip_network
        #assert isinstance(srcIP,ipaddress.ip_network)
        #assert isinstance(dstIP,ipaddress.ip_network)

        key = 1
        n = rbnode(key,srcIP,dstIP)
        t = rbtree(n)

        while(1):
            side_flipcoin = random.randint(0,1)
            ## flip the coin and randomly choose to divide srcIP or dstIP
            if(side_flipcoin==0):
                if(srcIP._prefixlen == 32):
                    continue
                srcIP =list(srcIP.subnets()).pop(0)
            else:
                if(dstIP._prefixlen == 32):
                    continue
                dstIP=list(dstIP.subnets()).pop(0)
            key = key+1
            treeNode = rbnode(key,srcIP,dstIP)
            t.insert_node(treeNode)

srcIP = ipaddress.ip_network('10.0.0.0/24')
dstIP = ipaddress.ip_network('10.0.1.0/24')
c = CreateTree()
c.createTree(srcIP,dstIP)