class tree:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def preorder(self):
        print(self.root, end=" ")
        self.left and self.left.preorder()
        self.right and self.right.preorder()
    def inorder(self):
        self.left and self.left.inorder()
        print(self.root, end=" ")
        self.right and self.right.inorder()
    def postorder(self):
        self.left and self.left.postorder()
        self.right and self.right.postorder()   
        print(self.root, end=" ") 



root = tree(1)
root.left = tree(2)
root.left.left = tree(4)
root.left.right = tree(5)
root.right = tree(3)
root.right.left = tree(6)
root.right.right = tree(7)
root.preorder()
print("------")
root.postorder()
print("------")
root.inorder()