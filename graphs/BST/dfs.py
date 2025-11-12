class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def dfs_recursive(node):
    if node is None:
        return
    print(node.value)
    dfs_recursive(node.left)
    dfs_recursive(node.right)

from collections import deque

def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)