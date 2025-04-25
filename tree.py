class Node:
    def _init_(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(node):
     if node:
        return node.height
     else:
        return 0

def get_balance(node):
     if node:
        return height(node.left) - height(node.right)
     else :
        return 0

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    if balance > 1:
        if key < node.left.key:
            return right_rotate(node)
        else:
            node.left = left_rotate(node.left)
            return right_rotate(node)
    if balance < -1:
        if key > node.right.key:
            return left_rotate(node)
        else:
            node.right = right_rotate(node.right)
            return left_rotate(node)

    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

if __name__ == "__main__":
    root = None
    keys = [20, 4, 15, 70, 50, 100, 80]
    for key in keys:
        root = insert(root, key)

    print("In-order traversal of the AVL tree:")
    inorder(root)
    print()