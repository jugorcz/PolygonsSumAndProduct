class Node:
    def __init__(self, key, value, next=None):
        self.key = key  # line
        self.value = value  # pos y = f(x) -> (x,y)
        self.next = next


class LinkedList:
    def __init__(self, linesDictionary):
        self.start = None
        self.size = 0
        self.dictionary = linesDictionary

    def put(self, key, value):
        # print("put " + str(key) + ":" + str(value))
        if self.start:
            self._put(key, value)
        else:
            self.start = Node(key, value)
        self.size += 1
        # self.display()

    def calculateNewValue(self, x, function):
        a = function[0]
        b = function[1]
        y = a * x + b
        y = round(y, 4)
        return (x, y)

    # 1 left > right, 0 equal, -1 left < right
    # node: line -> (x,y)
    # dictionary: line -> function(a,b)
    def compareNodes(self, leftNode, rightNode):
        function1 = self.dictionary[leftNode.key]
        function2 = self.dictionary[rightNode.key]
        if function1 == function2:
            if leftNode.key[1][1] > rightNode.key[1][1]:
                return 1
            else:
                return -1

        leftX = leftNode.value[0]
        rightX = rightNode.value[0]
        if leftX != rightX:
            # print("change base")
            if rightX > leftX:
                function = self.dictionary[leftNode.key]
                leftNode.value = self.calculateNewValue(rightX, function)
            else:
                function = self.dictionary[rightNode.key]
                rightNode.value = self.calculateNewValue(leftX, function)

        leftY = leftNode.value[1]
        rightY = rightNode.value[1]
        if leftY > rightY:
            return 1
        elif rightY > leftY:
            return -1
        else:
            function = self.dictionary[leftNode.key]
            leftNode.value = self.calculateNewValue(leftNode.value[0]+0.5, function)
            return self.compareNodes(leftNode, rightNode)

    def _put(self, key, value):
        # new node goes to the beginning of list
        nodeToInsert = Node(key, value)
        currentNode = self.start
        if self.compareNodes(nodeToInsert, currentNode) == 1:
            self.start = nodeToInsert
            self.start.next = currentNode
            return

        # new node goes inside the list
        beforeCurrentNode = self.start
        currentNode = self.start.next
        while currentNode is not None:
            if self.compareNodes(nodeToInsert, currentNode) == 1:
                beforeCurrentNode.next = nodeToInsert
                nodeToInsert.next = currentNode
                return
            beforeCurrentNode = currentNode
            currentNode = currentNode.next

        # end of list
        beforeCurrentNode.next = nodeToInsert

    # key -> line
    def get(self, key):
        if self.start:
            result = self._get(key)
            if result:
                return result.value
        return None

    def _get(self, key):
        currentNode = self.start
        while currentNode:
            if currentNode.key == key:
                return currentNode
            currentNode = currentNode.next

    def delete(self, key):
        #print("delete " + str(key))
        if self.start:
            if self._delete(key):
                self.size -= 1
            else:
                print("No node to delete with key: " + str(key))

        # self.display()

    def _delete(self, key):
        # delete from beginning
        if self.start.key == key:
            self.start = self.start.next
            return True

        # delete from the middle
        beforeCurrentNode = self.start
        currentNode = self.start.next
        while currentNode:
            if currentNode.key == key:
                beforeCurrentNode.next = currentNode.next
                return True
            beforeCurrentNode = currentNode
            currentNode = currentNode.next
        return False

    def display(self):
        currentNode = self.start
        while currentNode is not None:
            print(str(currentNode.key[0]) + "-" + str(currentNode.key[1]) + " -> ", end="")
            currentNode = currentNode.next
        print("None")

    def getLeftNaighbour(self, key):
        if self.start.key == key:
            return None
        beforeCurrentNode = self.start
        currentNode = self.start.next
        while currentNode:
            if currentNode.key == key:
                return beforeCurrentNode.key
            beforeCurrentNode = currentNode
            currentNode = currentNode.next
        return None

    def getRightNaighbour(self, key):
        currentNode = self.start
        afterCurrentNode = self.start.next
        while afterCurrentNode:
            if currentNode.key == key:
                return afterCurrentNode.key
            currentNode = afterCurrentNode
            afterCurrentNode = afterCurrentNode.next
        return None

    def swapPlaces(self, key1, key2):
        #print("swap " + str(key1[0]) + " with " + str(key2[0]))
        # swap beginning
        if self.get(key1) is None or self.get(key2) is None:
            return

        node1 = self._get(key1)
        node2 = self._get(key2)
        if self.compareNodes(node1, node2) == 0:
            function = self.dictionary[node1.key]
            node1.value = self.calculateNewValue(node1.value[0]+1, function)

        if self.compareNodes(node1, node2) == 1:
            if node1.next == node2:
                return
        else:
            if node2.next == node1:
                return

        curr = self.start
        after = curr.next
        if (curr.key == key1 and after.key == key2) or (curr.key == key2 and after.key == key1):
            curr.next = after.next
            after.next = curr
            self.start = after
        else:
            before = curr
            curr = after
            after = after.next
            while after:
                if (curr.key == key1 and after.key == key2) or (curr.key == key2 and after.key == key1):
                    curr.next = after.next
                    after.next = curr
                    before.next = after
                    break
                before = curr
                curr = after
                after = after.next

        # self.display()

    def generatePairs(self):
        if self.size < 2:
            return None, None
        currentNode = self.start
        afterCurrentNode = currentNode.next
        while afterCurrentNode:
            yield currentNode.key, afterCurrentNode.key
            currentNode = afterCurrentNode
            afterCurrentNode = afterCurrentNode.next