class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next # The next node in the list


class LinkedList:
    def __init__(self):
        self.head = None # points to teh first node in the list
        self.head = None # points to the last node in the list
        self.length = 0
    
    def __str__(self):
        pass

    # append / add --> add_to_tail
    def add_to_tail(self, value):
        # check if there's a tail
        # If there is not tail (empty list)
        if not self.tail: # could also check length, check if tail == None
            # a. Create a new node
            new_tail = Node(value, None)
            # b. Set self.head and self.tail to new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail(general case):
        else:
            # a. Create a new node with the value you want to add = None
            new_tail = Node(value, None)
            # b. Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # c. Set self.tail to new node
            self.tail = new_tail
        self.length +=1

    def remove_head(self):
        # If not head(empty list):
        if not self.head # if self.head is None
            # a. Return None
            return None
        # List with one element:
        if self.head == self.tail
            # a. Set self.head to current_head.next(which is also None)
            current_head = self.head
            self.head = None
            # Decrement length by 1
            self.length -= 1
            # b. Set self.tail to None
            return current_head.value
        # If head(general case):
        else:
            # a. Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            # Decrement length by 1
            self.length -= 1
            # b. Return current_head.value
            return current_head.value

    def remove_tail(self):
        