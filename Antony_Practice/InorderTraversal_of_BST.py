nums = [1,2,3,4,5]
nums.append(6)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)
    
    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        
    return root

def inorder_traversal(root):
    # Left -> Root -> Right (Yields sorted order for BST)
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# --- Example Usage ---
if __name__ == "__main__":
    # Initialize an empty tree
    root = None
    
    # Insert a sequence of numbers
    elements = [50, 30, 20, 40, 70, 60, 80]
    
    for el in elements:
        root = insert(root, el)
        
    print("In-order traversal of the BST:")
    inorder_traversal(root) 
    # Expected Output: 20 30 40 50 60 70 80