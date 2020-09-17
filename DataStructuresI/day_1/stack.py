# lets look at the idea of another data structure
# a Stack like a stack of plates or books
# LIFO (last in first out)

# we can push items on to the stack
# we can pop items off a stack
# and we can peek at the item at the top of the stack

# think of how you could utilise a linked list to form a stack
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop()

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
        # other option return len(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1


    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()