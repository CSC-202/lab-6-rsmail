class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
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


def initialize() -> Queue:
    # raise NotImplementedError("Queue.initialize() not defined")
    return Queue()

def isEmpty(data: Queue) -> bool:
    # raise NotImplementedError("Queue.isEmpty() not defined")
    return data.first == None

def enqueue(data: Queue, value: int) -> Queue:
    # raise NotImplementedError("Queue.enqueue() not defined")
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

# stack = initialize()
# stack = enqueue(stack, 0)
# stack = enqueue(stack, 1)
# stack = enqueue(stack, 2)
# print(stack.toPythonList())

def dequeue(data: Queue) -> tuple[Node, Queue]:
    # raise NotImplementedError("Queue.dequeue() not defined")
    if isEmpty(data):
        return None, None
    else:
        front: Node = data.first
        data.first = front.next
        return front.value, data



# stack = initialize()
# stack = enqueue(stack, 0)
# stack = enqueue(stack, 1)
# stack = enqueue(stack, 2)
# print(dequeue(stack))

def peek(data: Queue) -> Node:
    # raise NotImplementedError("Queue.peek() not defined")
    if len(data) == 0:
        raise IndexError('Cannot peek an empty queue')

    def helper(curr: Node) -> Node:
        if curr is data.first:
            return curr.value

        return helper(curr.next)

    return helper(data.first)

# stack = initialize()
# stack = enqueue(stack, 0)
# stack = enqueue(stack, 1)
# stack = enqueue(stack, 2)
# print(peek(stack))

def clear(data: Queue) -> Queue:
    # raise NotImplementedError("Queue.clear() not defined")
    return Queue()