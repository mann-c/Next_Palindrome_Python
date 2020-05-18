# this program will take in an integer number as an input and output the next highest palindrome
# if the number is a palindrome itself the program will return the entered number

import Stack
import Queue

# create the stack and queue that will be used to determine if the number is a palindrome 
stack = Stack.Stack()
queue = Queue.Queue()

def print_queue(integer):

	# loop through the integer and add all of the digits to the queue
	while not (integer/10 == 0 and integer%10 ==0):
		queue.enqueue(integer%10)
		integer = integer//10
	
	# create a loop to dequeue the entire queue and recreate the integer
	multiplier = 1
	return_value = 0
	while not queue.is_queue_empty():
		#print(f"Return Value: {return_value}")
		return_value += queue.dequeue()*multiplier
		multiplier *= 10

	# print out the integer dequeued from the queue
	print(f"The dequeued number is: {return_value}")

def print_stack(integer):

	# loop through the integer and add all of the digits to the stack
	while not (integer/10 == 0 and integer%10 ==0):
		stack.push(integer%10)
		integer = integer//10

	# create a loop to pop the entire stack and recreate the integer reversed
	multiplier = 1
	return_value = 0
	while not stack.is_stack_empty():
		return_value += stack.pop()*multiplier
		multiplier *= 10

	# print out the integer dequeued from the queue
	print(f"The popped number is: {return_value}")

def is_palindrome(integer):

	# enter the integer into both the stack and queue
	while not (integer/10 == 0 and integer%10 ==0):
		stack.push(integer%10)
		queue.enqueue(integer%10)
		integer = integer//10

	# loop through the numbers as they are dequeued and popped, if the numbers are all the 
	# same then the integer passed in is a palindrome, otherwise the number isn't a palindrome 
	# and false should be returned
	while not (queue.is_queue_empty() and stack.is_stack_empty()):
		if queue.dequeue() != stack.pop():
			while not (queue.is_queue_empty() and stack.is_stack_empty()):
				queue.dequeue()
				stack.pop()
			return False
	
	return True


# get the integer from the user
integer = int(input("Input a number, the next number that is a palindrome will be returned:\n"))

# print the integer passed in forwards and backwards
print_queue(integer)
print_stack(integer)

# loop to increment the integer until the next palindrome is reached 
while not is_palindrome(integer):
	integer += 1

print(f"The next integer that is a palindrome is: {integer}")