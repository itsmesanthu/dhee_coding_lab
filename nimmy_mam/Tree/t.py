class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def print_element(root):
    if root is None:
        return None
    print(root.val,end=" ")
    print_element(root.left)
    print_element(root.right)
root=TreeNode(1)
root
print_element(root)
