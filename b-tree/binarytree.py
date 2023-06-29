class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def createTree(self):
        v = int(input())
        if v == -1:
            return None
        root = Node(val)
        print("Enter left child", root.data, end=": ")
        root.left = self.createTree()
        print("Enter right child", root.data, end=": ")
        root.right = self.createTree()
        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=' ')

    def countNodes(self, root):
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def height(self, root):
        if root is None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    def countLeaf(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countLeaf(root.left) + self.countLeaf(root.right)

    def countInternal(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        return self.countInternal(root.left) + self.countInternal(root.right) + 1

    def search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        return self.search(root.left, data) or self.search(root.right, data)


print("Enter -1 for None")
print("Enter Root Data: ", end='')
tree = BinaryTree()
tree.root = tree.createTree()

print("Displaying Tree Using Inorder")
tree.inorder(tree.root)
print("\nDisplaying Tree Using Preorder")
tree.preorder(tree.root)
print("\nDisplaying Tree Using Postorder")
tree.postorder(tree.root)

print("\nNumber of Nodes:", tree.countNodes(tree.root))
print("Height of Binary Tree:", tree.height(tree.root))
print("Number of Leaf Nodes:", tree.countLeaf(tree.root))
print("Number of Internal Nodes:", tree.countInternal(tree.root))

v = int(input("Enter a Data to Search : "))
if tree.search(tree.root, val):
    print(v, "is present in the Binary Tree")
else:
    print(v, "is not present in the Binary Tree")


#            19
#          /   \
#         71    62
#       /    \
#     58     33
#           /
#          69
