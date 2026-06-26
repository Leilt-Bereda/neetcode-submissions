class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None
class LRUCache:
# sentinel nodes: makes operations of accessing the least used and most used in constant operations
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = ListNode(0, 0) # to access the lru
        self.right = ListNode(0, 0) # to access the mru
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node):
        prev_node = node.prev
        nxt_node = node.next
        prev_node.next = nxt_node
        nxt_node.prev = prev_node
    # always adds the node right before self.right
    def insert(self, node):
        prev_node = self.right.prev
        nxt_node = self.right
        prev_node.next = node
        nxt_node.prev = node
        node.next, node.prev = nxt_node, prev_node
    def get(self, key: int) -> int:
    # Check if the key exists in the HashMap
    # If it doesn't, return -1
    # If it does, move that node to the front (most recently used):
        # Remove it from its current position, otherwise we would have the same node in two places
        # Insert it at the front
    # Return the value
        if key in self.cache:
            node = self.cache[key] # get the node that you want to access
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # check if the key already exists in the cache
        if key in self.cache:
            # remove old one
            self.remove(self.cache[key])
         # insert new node at the front
        # update the hashmap 
        new_node = ListNode(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
