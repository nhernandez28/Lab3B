red = "red"
black = "black"
count = 0


class Node(object):
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.height = 0
        self.left = None
        self.right = None
        self.color = red


class RedBlackTree:
    def __init__(self, root=None, height=-1):
        self.root = root

    def RB_search(self, key, cur):
        if not cur:
            return 0
        if cur.key == key:
            return 1
        if key < cur.key:
            return self.RB_search(key, cur.left)
        if key > cur.key:
            return self.RB_search(key, cur.right)
        return 0

    def RB_set_child(self, parent, whichChild, child):
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        return True

    def RB_replace_child(self, parent, currentChild, newChild):
        if parent.left == currentChild:
            return self.RB_set_child(parent, "left", newChild)
        elif parent.right == currentChild:
            return self.RB_set_child(parent, "right", newChild)
        return False

    def RB_insert(self, key):
        node = Node(key)
        self._bst_insert(node)
        node.color = red
        self.RB_balance(node)

    def _bst_insert(self, node):
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

    def RB_get_grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def RB_get_uncle(self, node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left == node.parent:
            return grandparent.right
        else:
            return grandparent.left

    def RB_balance(self, node):
        if node.parent is None:
            node.color = black
            return

        if node.parent.color == black:
            return

        parent = node.parent
        grandparent = self.RB_get_grandparent(node)
        uncle = self.RB_get_uncle(node)

        if uncle is not None and uncle.color == red:
            parent.color = uncle.color = black
            grandparent.color = red
            self.RB_balance(grandparent)
            return

        if (node == parent.right and
                parent == grandparent.left):
            self.RB_rotate_left(parent)
            node = parent
            parent = node.parent

        elif (node == parent.left and
              parent == grandparent.right):
            self.RB_rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = black
        grandparent.color = red
        if node == parent.left:
            self.RB_rotate_right(grandparent)
        else:
            self.RB_rotate_left(grandparent)

    def RB_rotate_left(self, node):
        rightLeftChild = node.right.left
        if node.parent is not None:
            self.RB_replace_child(node.parent, node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None

        self.RB_set_child(node.right, "left", node)
        self.RB_set_child(node, "right", rightLeftChild)

    def RB_rotate_right(self, node):
        leftRightChild = node.left.right
        if node.parent is not None:
            self.RB_replace_child(node.parent, node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        self.RB_set_child(node.left, "right", node)
        self.RB_set_child(node, "left", leftRightChild)

    def RB_try_case_1(self, node):
        if node.is_red() or node.parent is None:
            return True
        else:
            return False

    def RB_try_case_2(self, node, sibling):
        if sibling.is_red():
            node.parent.color = red
            sibling.color = black
            if node is node.parent.right:
                self.RB_rotate_right(node.parent)
            else:
                self.RB_rotate_left(node.parent)
            return True
        return False

    def RB_try_case_3(self, node, sibling):
        if node.parent.is_black() and sibling.RB_are_both_children_black():
            sibling.color = red
            self.RB_prepare_for_removal(node.parent)
            return True
        return False

    def RB_try_case_4(self, node, sibling):
        if node.parent.is_red() and sibling.RB_are_both_children_black():
            node.parent.color = black
            sibling.color = red
            return True
        return False

    def RB_try_case_5(self, node, sibling):
        if self.RB_is_non_none_and_red(sibling.left) and self.RB_is_none_or_black(
                sibling.right) and node is node.parent.left:
            sibling.color = red
            sibling.left.color = black
            self.RB_rotate_right(sibling)
            return True
        return False

    def RB_try_case_6(self, node, sibling):
        if self.RB_is_none_or_black(sibling.left) and self.RB_is_non_none_and_red(
                sibling.right) and node is node.parent.right:
            sibling.color = red
            sibling.right.color = black
            self.RB_rotate_left(sibling)
            return True
        return False

    def print_tree(self, root):
        if root is None:
            return
        print(root.key, root.color)
        self.print_tree(root.left)
        self.print_tree(root.right)
        return
