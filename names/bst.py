from collections import deque

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the incoming value is less than the current node's value 
        if value < self.value:
            # we know we need to go left 
            # how do we know when we need to recurse again, 
            # or when to stop? 
            if not self.left:
                # we can park our value here 
                self.left = BST(value)
            else:
                # we can't park here 
                # keep searching 
                self.left.insert(value)
        else:
            # we know we need to go right 
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BST
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BST
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # we'll keep going right until there are no more nodes on the right side 
        if not self.right:
            return self.value
        # otherwise, keep going right 
        return self.right.get_max()
    # Call the function `fn` on the value of each node
    # Do we expect a return from the for_each function? No 
    def for_each(self, fn):
        # call the fn on the value at this node 
        fn(self.value)

        # pass this function to the left child 
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child 
        if self.right:
            self.right.for_each(fn)
  # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            node = queue.popleft()

            print(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
            # create stack
        stack = []
        # add root to stack
        stack.append(self)
        while len(stack) > 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
