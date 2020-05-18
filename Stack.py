# this file holds the stack class that will be used to manipulate the stack

import Node

class Stack:
    """
    This class is used to create the stack structure, it has methods to manipulate the stack
    """
    def __init__(self):
        self.stack_size = 0
        self.top = None

    def is_stack_empty(self):
        if self.stack_size == 0:
            return True
        else:
            return False

    def push(self, value):
        node = Node.Node(value)
        
        if self.is_stack_empty():
            self.top = node
            self.stack_size += 1
            return
        else:
            node.set_node_next(self.top)  
            self.top = node
            self.stack_size += 1
            return

    def pop(self):
        if self.is_stack_empty():
            return 0
        else:
            temp_value = self.top.return_value()
            self.stack_size -= 1
            self.top = self.top.return_next_node()
            return temp_value