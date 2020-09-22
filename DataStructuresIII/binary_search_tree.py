"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    """
    The left subtree of a node contains only nodes with values lesser than the node's values
    The right subtree of a node contains only nodes with values greater or equal to than the node's values
    The left and right subtree each must also be a binary search tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
            # if there is no left child already there
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it then set it to the left
            # otherwise call insert on the left node
        # otherwise (the new nodes value is greater than or equal to the current nodes value)
            # if there is no right child already there
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it then set it to the right
            # otherwise call insert on the left node
        pass


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
            # return True
        # check if the target is less than the current nodes value
            # if there is no left child already there
                # return False
            # otherwise
                # return a call of contains on the left child passing in the target value
        # otherwise (the target is greater thanthe current nodes value)
            # if there is no right child already there
                # return False
            # otherwise
                # return a call of contains on the right child passing in the target value
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty tree
            # return None

        # recursive approach (use more memory)
        # check if there is no node to the right
            # return the nodes value
        # return a call to get max on the right child
        # -------------------------------------------
        # iterative approach (more lines of code)
        # doubly linked list max function

        # initialize max value

        #  get reference to the current node

        # lopp while there is still a current node
            # if the current value is greater than the max value, update the max value
            # move on to the next right node

        # return max value
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call back function
        # call the function - passing the current node's value

        # if there is a node to the left
            # call the function on the left value

        # if there is a node to the right
            # call the function on the right node
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft() 