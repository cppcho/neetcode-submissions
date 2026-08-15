"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
mp = old -> new
q = ()

# without the neighbour linkages
while queue not empty
    get oldNode
        create newNode
    for each neighbors 
        if not seen yet
            enqueue neighbors
        if seen
            do linkage

return mp[root]
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        mp = {node.val: Node(node.val) }
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor.val not in mp:
                    mp[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                mp[curr.val].neighbors.append(mp[neighbor.val])


        return mp[node.val]
