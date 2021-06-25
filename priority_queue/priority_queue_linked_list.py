"""
File: priority_queue_linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It controls the condition to break the input loop
EXIT = ''


class ListNode:
	def __init__(self, val, next_one):
		self.val = val
		self.next = next_one


def main():
	priority_queue = None
	while True:
		name = input(f'Name of patient ({EXIT} to quit): ')
		if name == EXIT:
			break
		priority = int(input('Priority: '))
		data = (name, priority)
		if priority_queue is None:
			priority_queue = ListNode(data, None)
		else:
			new_node = ListNode(data, None)
			if priority < priority_queue.val[1]:
				# Prepend new node at the beginning
				new_node.next = priority_queue
				priority_queue = new_node
			else:
				# Insert new node in between or append new node at last
				current = priority_queue
				while current.next is not None:
					if current.val[1] <= new_node.val[1] < current.next.val[1]:
						print('insert')
						new_node.next = current.next
						current.next = new_node
						break
					current = current.next
				if current.next is None:
					print('append')
					current.next = new_node
	traversal(priority_queue)


def traversal(linked_list: ListNode):
	# use is not because it's reference
	while linked_list is not None:
		print(linked_list.val)
		linked_list = linked_list.next


if __name__ == '__main__':
	main()
