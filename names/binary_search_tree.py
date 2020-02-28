from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # larger numbers right
        if value > self.value:
            # check if there's value there
            if self.right == None:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
        # smaller numbers left
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if equal, already in the tree
        else:
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #smaller numbers first
        if node.left:
            self.in_order_print(node.left)
        # then current value
        print(node.value)
        #then larger numbers
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len() > 0:
            t = q.dequeue()
            print(t.value)
            if t.left:
                q.enqueue(t.left)
            if t.right:
                q.enqueue(t.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.len() > 0:
            t = s.pop()
            print(t.value)
            if t.right:
                s.push(t.right)
            if t.left:
                s.push(t.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
