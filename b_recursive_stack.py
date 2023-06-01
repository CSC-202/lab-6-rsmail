class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    # raise NotImplementedError("Stack.initialize() not defined")
    return Stack()


def isEmpty(data: Stack) -> bool:
    # raise NotImplementedError("Stack.isEmpty() not defined")
    return data.first == None
        


def push(data: Stack, value: int) -> Stack:
    # raise NotImplementedError("Stack.push() not defined")
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
# stack = initialize()
# stack = push(stack, 0)
# stack = push(stack, 1)
# stack = push(stack, 2)
# stack = push(stack, 3)
 
# print(stack.toPythonList())



def pop(data: Stack) -> tuple[int, Stack]:
    top = data.first
    data.first = top.next
    return top.value, data
# stack = initialize()
# stack = push(stack, 0)
# stack = push(stack, 1)
# stack = push(stack, 2)
# stack = push(stack, 3)
# value = pop(stack)  
# print(value)



def peek(data: Stack) -> Node:
    # raise NotImplementedError("Stack.peek() not defined")
    return data.first.value

# stack = initialize()
# stack = push(stack, 0)
# stack = push(stack, 1)
# stack = push(stack, 2)
# stack = push(stack, 3)
# print(peek(stack))


def clear(data: Stack) -> Stack:
    # raise NotImplementedError("Stack.clear() not defined")
    data.first = None
    return data

# stack = initialize()
# stack = push(stack, 0)
# stack = push(stack, 1)
# stack = push(stack, 2)
# stack = push(stack, 3)
# clear(stack)
# print(stack.toPythonList())
