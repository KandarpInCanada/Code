class node:
    def __init__(self,number):
        self.data = number
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def _insert(self,root,number):
        if root is None:
            root = node(number)
        else:
            if number < root.data:
                root.left = self._insert(root.left,number)
            else:
                root.right = self._insert(root.right,number)
        return root
    
    def insert(self,number):
        self.root = self._insert(self.root,number)
    
    def inorder_traversal(self,root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.data)
            result += self.inorder_traversal(root.right)
        return result
    
    def preorder_traversal(self,root):
        result = []
        if root:
            result.append(root.data)
            result += self.preorder_traversal(root.left)
            result += self.preorder_traversal(root.right)
        return result
    
    def postorder_traversal(self,root):
        result = []
        if root:
            result += self.postorder_traversal(root.left)
            result += self.postorder_traversal(root.right)
            result.append(root.data)
        return result
    
    def _search(self,root,search_value):
        try:
            if search_value == root.data:
                print("found the data")
            else:
                if search_value < root.data:
                    self._search(root.left,search_value)
                else:
                    self._search(root.right,search_value)
        except:
            print("not found")

    def search(self,search_value):
        self._search(self.root,search_value)

    def max_height_of_tree(self,root):
        if root is None:
            return -1
        else:
            left_max_height = self.max_height_of_tree(root.left)
            right_max_height = self.max_height_of_tree(root.right)
            return max(left_max_height,right_max_height) + 1

t = Tree()
list1 = [223,3456,8,9,3,26,76,56,76,6]
for i in list1:
    t.insert(i)
print("-"*20)
print(t.inorder_traversal(t.root))
print("-"*20)
print(t.preorder_traversal(t.root))
print("-"*20)
print(t.postorder_traversal(t.root))
print("-"*20)
print(t.max_height_of_tree(t.root))
print("-"*20)
t.search(223)
