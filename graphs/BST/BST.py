#Object-oriented implementation of Binary Search Tree(BST) with inserting and searching succesor, searching
# "k" element smallest element


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.subtree_size = 0

    def __str__(self):
        return f"Node({self.value})"

class BST:
    def __init__(self):
        self.root = None

    def insert(self,node):
        if not self.root:
            self.root = node
        else:
            self.insert_recur(self.root,node)

    def insert_recur(self,current,node):
        if current.value >= node.value:
            if current.left is None:
                current.left = node
                node.parent = current
            else:
                self.insert_recur(current.left,node)
        else:
            if current.right is None:
                current.right = node
                node.parent = current
            else:
                self.insert_recur(current.right,node)

    def inorder_traversal(self,node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def successor(self,node):
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            while node.parent is not None and node.parent.left != node:
                node = node.parent
            return node.parent



tree = BST()
tree.insert(Node(10))
tree.insert(Node(30))
a = Node(9)
tree.insert(a)
tree.insert(Node(2))
tree.insert(Node(7))
tree.insert(Node(11))
tree.insert(Node(15))
print(tree.successor(a))
tree.inorder_traversal(tree.root)



