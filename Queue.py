# this file holds the queue class that is used to create and manipulate the queue

import Node

class Queue:
    """
    This class is used to create and manipulate a queue
    """
    def __init__(self):
        self.queue_size = 0
        self.head = None
        self.tail = None

    def is_queue_empty(self):
        if self.queue_size == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        # create a new node with the value passed in 
        node = Node.Node(value)

        # if statement for adding the node into an empty queue
        if self.is_queue_empty():
            self.queue_size += 1
            self.head = node
            self.tail = node
            return
        
        # else statement is for adding the node onto the queue if it isn't empty
        else:
            self.queue_size += 1
            self.tail.set_node_next(node)
            self.tail = node
            return

    def dequeue(self):
        
        # determine if the queue is empty, if it is return None
        if self.is_queue_empty():
            return 0

        # else if the queue is not empty dequeue the node from the head
        else:
            self.queue_size -= 1
            temp_value = self.head.return_value()
            node = self.head
            self.head = node.return_next_node()
            node.set_node_next(None)
            del node
            return temp_value