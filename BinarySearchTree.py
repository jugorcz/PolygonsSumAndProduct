

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        print("put " + str(key) + ":" + str(val))
        duplicate = self.findDuplicate(self.root, key, val)
        if duplicate:
            print("Duplicate")
            return

        if self.root:
            self._put(key, val, self.root)  # _put is a helper function
        else:
            self.root = TreeNode(key, val)
        self.size += 1
        # self.display()

    def _put(self, key, val, currentNode):
        if key < currentNode.key or (key == currentNode.key and val < currentNode.value):
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):  # overloading of [] operator
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):  # overloading of [] operator
        return self.get(key)

    def __contains__(self, key):  # overloading of in operator
        if self._get(key, self.root):
            return True
        else:
            return False

    def getNode(self, currentNode, key, value):
        return self.findDuplicate(self.root, key, value)

    def delete(self, key, value):
        print("delete " + str(key))
        if self.size > 1:
            nodeToRemove = self.getNode(self.root, key, value)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                print('Error, key not in tree')
                return
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            print('Error, key not in tree')
            return
        # self.display()

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.value = succ.value
        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.value,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.value,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def display(self):
        self.displayBST(self.root, 0)
        print("")
        print("")

    def displayBST(self, root, x):
        if root:
            print(str(root.key) + ":" + str(root.value), end="")
            if root.hasRightChild():
                print(" -> ", end="")
                self.displayBST(root.rightChild, x + 1)
            if root.hasLeftChild():
                print("")  # new line
                i = x
                while i >= 0:
                    print("  |    ", end="")
                    i -= 1
                print("")
                i = x
                while i > 0:
                    print("  |    ", end="")
                    i -= 1
                self.displayBST(root.leftChild, x)

    def findTheSmallest(self, root):
        if root.hasLeftChild():
            return self.findTheSmallest(root.leftChild)
        else:
            return root

    def findDuplicate(self, currentNode, key, value):
        if currentNode is None:
            return None

        if currentNode.key == key and currentNode.value == value:
            return currentNode

        if currentNode.hasLeftChild():
            result = self.findDuplicate(currentNode.leftChild, key, value)
            if result:
                return result

        if currentNode.hasRightChild():
            result = self.findDuplicate(currentNode.rightChild, key, value)
            if result:
                return result

        return None