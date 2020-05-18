# this file holds the node class that will be used to build the stack and queue

class Node: 
    """
    This class is used to create the node objects for the stack and queue structure
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def return_next_node(self):
        return self.next_node

    def return_value(self):
        return self.value

    def set_node_next(self, node):
        self.next_node = node