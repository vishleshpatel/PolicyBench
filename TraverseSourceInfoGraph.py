__author__ = 'vishlesh'

import ipaddress

class SourceInfo:

    def __init__(self):
        totalPolicyPercentageCovered = 0

    def getAllEndHosts(self,subnetsList):
        EndHostsList = []

        for each_subnet_addr in subnetsList:
            EndHostsList.append(self.getHosts(each_subnet_addr))

        return EndHostsList

    def getHosts(self,networkAddr):
        list = []
        for addr in networkAddr:
            list.append(addr)

        list.pop()
        list.pop(0)
        return list


    def traverseSourceInfoGraph(self,sourceInfoGraph,totalPolicies,subnetsList):
        EndHosts = []
        EndHosts = self.getAllEndHosts(subnetsList)

        for (x,y) in sourceInfoGraph:
