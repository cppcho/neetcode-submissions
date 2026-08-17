class Node:
    def __init__(self, key: int, value: int, prev: Node = None, next: Node = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.last = Node(0, 0)
        self.head.next = self.last
        self.last.prev = self.head

    def append_node(self, node: Node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    def remove_last(self):
        removing = self.last.prev
        if removing == self.head:
            raise Exception("empty list")
        
        removing.prev.next = self.last
        self.last.prev = removing.prev
        removing.prev = removing.next = None
        return removing

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.linkedList = LinkedList()

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            node = self.cache[key]
            res = node.value
            self.linkedList.remove_node(node)
            self.linkedList.append_node(node)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.linkedList.remove_node(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

        self.linkedList.append_node(node)

        while len(self.cache) > self.capacity:
            removed = self.linkedList.remove_last()
            del self.cache[removed.key]

        