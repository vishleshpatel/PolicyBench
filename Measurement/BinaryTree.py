import ipaddress

class Node():
    def __init__(self, key,srcIP,dstIP):

        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = 0
        self.srcIP =srcIP
        self.dstIP=dstIP

    def __str__(self):
        return str(self.key) + "(" + str(self.height) + ")"

    def is_leaf(self):
        return (self.height == 0)

    def max_children_height(self):
        if self.leftChild and self.rightChild:
            return max(self.leftChild.height, self.rightChild.height)
        elif self.leftChild and not self.rightChild:
            return self.leftChild.height
        elif not self.leftChild and  self.rightChild:
            return self.rightChild.height
        else:
            return -1

    def balance (self):
        return (self.leftChild.height if self.leftChild else -1) - (self.rightChild.height if self.rightChild else -1)



class AVLTree():
    def __init__(self, node):
        assert isinstance(node,Node)
        self.rootNode = node
        self.elements_count = 0
        self.rebalance_count = 0


    def height(self):
        if self.rootNode:
            return self.rootNode.height
        else:
            return 0

    def rebalance(self, node_to_rebalance):
        self.rebalance_count += 1
        A = node_to_rebalance
        F = A.parent #allowed to be NULL
        if node_to_rebalance.balance() == -2:
            if node_to_rebalance.rightChild.balance() <= 0:
                """Rebalance, case RRC """
                B = A.rightChild
                C = B.rightChild
                assert (not A is None and not B is None and not C is None)
                A.rightChild = B.leftChild
                if A.rightChild:
                    A.rightChild.parent = A
                B.leftChild = A
                A.parent = B
                if F is None:
                   self.rootNode = B
                   self.rootNode.parent = None
                else:
                   if F.rightChild == A:
                       F.rightChild = B
                   else:
                       F.leftChild = B
                   B.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B.parent)
            else:
                """Rebalance, case RLC """
                B = A.rightChild
                C = B.leftChild
                assert (not A is None and not B is None and not C is None)
                B.leftChild = C.rightChild
                if B.leftChild:
                    B.leftChild.parent = B
                A.rightChild = C.leftChild
                if A.rightChild:
                    A.rightChild.parent = A
                C.rightChild = B
                B.parent = C
                C.leftChild = A
                A.parent = C
                if F is None:
                    self.rootNode = C
                    self.rootNode.parent = None
                else:
                    if F.rightChild == A:
                        F.rightChild = C
                    else:
                        F.leftChild = C
                    C.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B)
        else:
            assert(node_to_rebalance.balance() == +2)
            if node_to_rebalance.leftChild.balance() >= 0:
                B = A.leftChild
                C = B.leftChild
                """Rebalance, case LLC """
                assert (not A is None and not B is None and not C is None)
                A.leftChild = B.rightChild
                if (A.leftChild):
                    A.leftChild.parent = A
                B.rightChild = A
                A.parent = B
                if F is None:
                    self.rootNode = B
                    self.rootNode.parent = None
                else:
                    if F.rightChild == A:
                        F.rightChild = B
                    else:
                        F.leftChild = B
                    B.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B.parent)
            else:
                B = A.leftChild
                C = B.rightChild
                """Rebalance, case LRC """
                assert (not A is None and not B is None and not C is None)
                A.leftChild = C.rightChild
                if A.leftChild:
                    A.leftChild.parent = A
                B.rightChild = C.leftChild
                if B.rightChild:
                    B.rightChild.parent = B
                C.leftChild = B
                B.parent = C
                C.rightChild = A
                A.parent = C
                if F is None:
                   self.rootNode = C
                   self.rootNode.parent = None
                else:
                   if (F.rightChild == A):
                       F.rightChild = C
                   else:
                       F.leftChild = C
                   C.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B)


    def recompute_heights (self, start_from_node):
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.rightChild or node.leftChild) else 0)
            changed = node.height != old_height
            node = node.parent

    def add_as_child (self, parent_node, child_node):
        node_to_rebalance = None
        if child_node.key < parent_node.key:
            if not parent_node.leftChild:
                parent_node.leftChild = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break #we need the one that is furthest from the root
                        node = node.parent
            else:
                self.add_as_child(parent_node.leftChild, child_node)
        else:
            if not parent_node.rightChild:
                parent_node.rightChild = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break #we need the one that is furthest from the root
                        node = node.parent
            else:
                self.add_as_child(parent_node.rightChild, child_node)

        if node_to_rebalance:
            self.rebalance (node_to_rebalance)

    def insert_node(self, node):
        assert isinstance(node,Node)
        if not self.rootNode:
            self.rootNode =node
        else:
            if not self.find(node.key):
                self.elements_count += 1
                self.add_as_child (self.rootNode, node)

    def inorder_non_recursive(self):
        node = self.rootNode
        retlst = []
        while node.leftChild:
            node = node.leftChild
        while (node):

            retlst += [node]

            if (node.rightChild):
                node = node.rightChild
                while node.leftChild:
                    node = node.leftChild
            else:
                while ((node.parent)  and (node == node.parent.rightChild)):
                    node = node.parent
                node = node.parent
        return retlst

    def find(self, key):
        return self.find_in_subtree (self.rootNode, key )

    def find_in_subtree (self,  node, key):
        if node is None:
            return None  # key not found
        if key < node.key:
            return self.find_in_subtree(node.leftChild, key)
        elif key > node.key:
            return self.find_in_subtree(node.rightChild, key)
        else:  # key is equal to node key
            return node

"""
rootnode = Node(1,ipaddress.ip_network('10.0.0.0/24'),ipaddress.ip_network('10.0.0.0/24'))
tree = AVLTree(rootnode)
node1 = Node(2,None,None)
tree.insert_node(node1)
node2 = Node(3,None,None)
tree.insert_node(node2)
node3 = Node(4,None,None)
tree.insert_node(node3)
print(tree.height())
print(tree.find(2).dstIP)
print(tree.rootNode.key,"feffs")

list2=tree.inorder_non_recursive()
for each_node in list2:
    print(each_node.key)
print(len(list2))
"""