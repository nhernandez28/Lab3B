class Node(object):
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def AVL_set_child(self, parent, whichChild, child):
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

        self.AVL_update_height(parent)
        return True

    def AVL_replace_child(self, parent, currentChild, newChild):
        if parent.left == currentChild:
            return self.AVL_set_child(parent, "left", newChild)
        elif parent.right == currentChild:
            return self.AVL_set_child(parent, "right", newChild)
        return False

    def AVL_search(self, key, cur):
        if not cur:
            return 0
        if cur.key == key:
            return 1
        if key < cur.key:
            return self.AVL_search(key, cur.left)
        if key > cur.key:
            return self.AVL_search(key, cur.right)
        return 0

    def AVL_update_height(self, node):
        leftHeight = -1
        if node.left is not None:
            leftHeight = node.left.height
        rightHeight = -1
        if node.right is not None:
            rightHeight = node.right.height
        node.height = max(leftHeight, rightHeight) + 1

    def AVL_get_balance(self, node):
        leftHeight = -1
        if node.left is not None:
            leftHeight = node.left.height
        rightHeight = -1
        if node.right is not None:
            rightHeight = node.right.height
        return leftHeight - rightHeight

    def AVL_rebalance(self, node):
        self.AVL_update_height(node)
        if self.AVL_get_balance(node) == -2:
            if self.AVL_get_balance(node.right) == 1:
                # Double rotation case.
                self.avl_rotate_right(node.right)

            return self.avl_rotate_left(node)

        elif self.AVL_get_balance(node) == 2:
            if self.AVL_get_balance(node.left) == -1:
                # Double rotation case.
                self.avl_rotate_left(node.left)

            return self.avl_rotate_right(node)

        return node

    def AVL_insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
        else:
            self._AVL_insert(new_node)

    def _AVL_insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
            return
        cur = self.root
        while cur is not None:
            if node.key < cur.key:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        node = node.parent
        while node is not None:
            self.AVL_rebalance(node)
            node = node.parent

    def avl_rotate_right(self, node):
        leftRightChild = node.left.right
        if node.parent is not None:
            self.AVL_replace_child(node.parent, node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        self.AVL_set_child(node.left, "right", node)
        self.AVL_set_child(node, "left", leftRightChild)

    def avl_rotate_left(self, node):
        rightLeftChild = node.right.left
        if node.parent is not None:
            self.AVL_replace_child(node.parent, node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None

        self.AVL_set_child(node.right, "left", node)
        self.AVL_set_child(node, "right", rightLeftChild)

    def print_tree(self, node):
        if node is None:
            return
        print(node.key)
        self.print_tree(node.left)
        self.print_tree(node.right)
        return
