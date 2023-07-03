class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def createBST(self, root):
        print("Creating Binary Search Tree")
        print("Enter -1 to Stop")
        data = int(input("Enter Root Data: "))
        while data != -1:
            root = self.insertNode(root, data)
            data = int(input("Enter Next Data: "))
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

    def search(self, root, val):
        if root is None:
            return False
        if root.data == val:
            return True
        if root.data > val:
            return self.search(root.left, val)
        return self.search(root.right, val)

    def isComplete(self, root, idx, numNodes):
        if root is None:
            return True
        if idx >= numNodes:
            return False
        return self.isComplete(root.left, 2*idx+1, numNodes) and self.isComplete(root.right, 2*idx+2, numNodes)

    def insertNode(self, root, data):
        if root is None:
            return Node(data)
        if(root.data > data):
            root.left = self.insertNode(root.left, data)
        else:
            root.right = self.insertNode(root.right, data)
        return root

    def deleteNode(self, root, val):
        if root is None:
            return root
        if val < root.data:
            root.left = self.deleteNode(root.left, val)
        elif val > root.data:
            root.right = self.deleteNode(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.minValue(root.right)
            root.right = self.deleteNode(root.right, root.data)
        return root

    def balanceFactor(self, root, val):
        if root.data > val:
            return self.balanceFactor(root.left, val)
        if root.data < val:
            return self.balanceFactor(root.right, val)
        return abs(self.height(root.left)-self.height(root.right))

    def minValue(self, root):
        while root and root.left:
            root = root.left
        return root.data

    def maxValue(self, root):
        while root and root.right:
            root = root.right
        return root.data

    def countNone(self, root):
        if root is None:
            return 1
        return self.countNone(root.left)+self.countNone(root.right)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.root = tree.createBST(tree.root)

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

    val = int(input("Enter a Value to Search: "))
    if tree.search(tree.root, val):
        print(val, "is present in the Tree")
    else:
        print(val, "is not present in the Tree")

    if tree.isComplete(tree.root, 0, tree.countNodes(tree.root)):
        print("The Binary Search Tree is Complete.")
    else:
        print("The Binary Search Tree is not Complete.")


    val = int(input("Enter a Data to Insert in BST: "))
    tree.root = tree.insertNode(tree.root, val)
    print(val, "is Inserted in BST")


    val = int(input("Enter a Data to Delete from BST: "))
    if tree.search(tree.root, val):
        tree.root = tree.deleteNode(tree.root, val)
        print(val, "is Deleted from BST")
    else:
        print(val, "is not present in the tree")

    val = int(input("Enter a Value to get Balance Factor: "))
    if tree.search(tree.root, val):
        print("Balance Factor of", val, "is",tree.balanceFactor(tree.root, val))
    else:
        print(val, "is not present in the tree")

    print("Minimum Value in BST: ", tree.minValue(tree.root))
    print("Maximum Value in BST: ", tree.maxValue(tree.root))
    print("Number of None Pointers: ", tree.countNone(tree.root))
