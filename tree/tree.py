"""
File: tree.py
Name: 
-------------------------
This file shows the basic concepts for binary trees.
After constructing a tree, we will do 3 traversal examples:
Pre-order
In-order 
Post-order
"""


class Tree:
	def __init__(self, left, value, right):
		self.value = value
		self.right = right
		self.left = left


def main():
	l1 = Tree(None, 12, None)
	l2 = Tree(None, 30, None)

	leaf1 = Tree(None, 2, None)
	leaf2 = Tree(None, 6, None)
	leaf3 = Tree(l1, 18, l2)
	leaf4 = Tree(None, 40, None)
	node1 = Tree(leaf1, 4, leaf2)
	node2 = Tree(leaf3, 19, leaf4)
	root = Tree(node1, 17, node2)

	# traversal(root)
	print('-------------------')
	print('pre_order: ', end='')
	pre_order(root)
	print('\n-----------------')
	print('in_order: ', end=' ')
	in_order(root)
	print('\n------------------')
	print('post_order: ', end='')
	post_order(root)
	print('\n-----------------')
	print('bfs: ', end='')
	bfs(root)


def traversal(cur: Tree):
	if cur.left is None and cur.right is None:
		print(cur.value)
	else:
		print(cur.value)
		# left
		traversal(cur.left)
		# right
		traversal(cur.right)


def pre_order(root: Tree):
	if root is None:
		return
	else:
		print(root.value, end=',')
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root is None:
		return
	else:
		in_order(root.left)
		print(root.value, end=',')
		in_order(root.right)


def post_order(root):
	if root is None:
		return
	else:
		post_order(root.left)
		post_order(root.right)
		print(root.value, end=',')


def bfs(root: Tree):
	queue = [root]
	while len(queue) != 0:
		node = queue.pop(0)
		print(node.value, end=',')
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)


if __name__ == '__main__':
	main()
