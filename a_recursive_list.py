class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> List:
    # raise NotImplementedError("List.initialize() not defined")
    return List()


def isEmpty(data: List) -> bool:
    # raise NotImplementedError("List.isEmpty() not defined")
    return data.first == None
     


def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(v: Node, index: int, value: int, i: int):
        if i == index:
            new_node = Node(value, v.next)
            v.next = new_node
        elif i > index:
            raise IndexError('index error')
        elif v.next is None and i + 1 == index:
            new_node = Node(value, None)
            v.next = new_node
        elif v.next is None:
            raise IndexError('index error')
        else:
            return helper(v.next, index, value, i + 1)

    if isEmpty(data):
        if index == 0:
            new_node = Node(value, None)
            data.first = new_node
            data.last = new_node
    elif index < 0 or index > len(data):
        raise IndexError('index error')
    elif index == 0:
        new_node = Node(value, data.first)
        data.first = new_node
        if data.last is None:
            data.last = new_node
    else:
        helper(data.first, index, value, 0)

    return data


# list = initialize()
# list = addAtIndex(list, 0, 0)
# list = addAtIndex(list, 0, 1)
# list = addAtIndex(list, 0, 2)
# list = addAtIndex(list, 0, 3)
# list = addAtIndex(list, 0, 100)
# print(list.toPythonList())  # Output: [100, 3, 2, 1, 0]


def addToFront(data: List, value: int) -> List:
    # raise NotImplementedError("List.addToFront() not defined")
    index = 0
    def helper(v: Node, index: int, value: int, i: int):
        if i == index:
            new_node = Node(value, v.next)
            v.next = new_node
        elif i > index:
            raise IndexError('index error')
        elif v.next is None and i + 1 == index:
            new_node = Node(value, None)
            v.next = new_node
        elif v.next is None:
            raise IndexError('index error')
        else:
            return helper(v.next, index, value, i + 1)
    if isEmpty(data):
        if index == 0:
            new_node = Node(value, None)
            data.first = new_node
            data.last = new_node
    elif index < 0 or index > len(data):
        raise IndexError('index error')
    elif index == 0:
        new_node = Node(value, data.first)
        data.first = new_node
        if data.last is None:
            data.last = new_node
    else:
        helper(data.first, index, value, 0)

    return data
# list1 = initialize()
# list1 = addAtIndex(list1, 0, 0)
# list1 = addAtIndex(list1, 1, 1)
# list1 = addToFront(list1, 1000)
# print(list1.toPythonList()) 

def addToBack(data: List, value: int) -> List:
    # raise NotImplementedError("List.addToBack() not defined")
    index = len(data)
    def helper(v: Node, index: int, value: int, i: int):
        if i == index:
            new_node = Node(value, v.next)
            v.next = new_node
        elif i > index:
            raise IndexError('index error')
        elif v.next is None and i + 1 == index:
            new_node = Node(value, None)
            v.next = new_node
        elif v.next is None:
            raise IndexError('index error')
        else:
            return helper(v.next, index, value, i + 1)
    if isEmpty(data):
        if index == 0:
            new_node = Node(value, None)
            data.first = new_node
            data.last = new_node
    elif index < 0 or index > len(data):
        raise IndexError('index error')
    elif index == 0:
        new_node = Node(value, data.first)
        data.first = new_node
        if data.last is None:
            data.last = new_node
    else:
        helper(data.first, index, value, 0)

    return data
# list2 = initialize()
# list2 = addAtIndex(list2, 0, 0)
# list2 = addAtIndex(list2, 1, 1)
# list2 = addToBack(list2, 1000)
# print(list2.toPythonList()) 

def getElementAtIndex(data: List, index: int) -> Node:
    # raise NotImplementedError("List.getElementAtIndex() not defined")
    def helper(v: Node, index: int, i: int):
        if i == index:
            return v.value
        elif i > index:
            raise IndexError('index error')
        elif v.next is None and i + 1 == index:
            raise IndexError('index error')
        elif v.next is None:
            raise IndexError('index error')
        else:
            return helper(v.next, index, i + 1)
    if isEmpty(data):
        raise IndexError('index error')
    elif index < 0 or index > len(data):
        raise IndexError('index error')
    else:
        return helper(data.first, index, 0)

# list2 = initialize()
# list2 = addAtIndex(list2, 0, 0)
# list2 = addAtIndex(list2, 1, 1)
# list2 = addToBack(list2, 1000)
# list2 = addToBack(list2, 1023)
# list2 = addToBack(list2, 10)
# list2 = addToBack(list2, 10)
# print(getElementAtIndex(list2, 3))


def clear(data: List) -> List:
    # raise NotImplementedError("List.clear() not defined")
    data.first = None
    return data


# list2 = initialize()
# list2 = addAtIndex(list2, 0, 0)
# list2 = addAtIndex(list2, 1, 1)
# list2 = addToBack(list2, 1000)
# list2 = addToBack(list2, 1023)
# list2 = addToBack(list2, 10)
# list2 = addToBack(list2, 10)
# clear(list2)

# print(list2.toPythonList())