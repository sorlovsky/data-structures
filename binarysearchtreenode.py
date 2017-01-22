# 2010 September 18 by Joshua R. Davis

from binarytreenode import BinaryTreeNode

class BinarySearchTreeNode(BinaryTreeNode):
	"""A nonempty binary search tree with put(), get(), and delete() operations. The keys must be distinct ints. Warning: It is possible to use the underlying BinaryTree methods such as setLeftChild(), but this is not advisable, because they do nothing to enforce the BST condition."""

	def __init__(self, key, value=None):
		"""Creates a new binary search tree node with the given key and value and no children."""
		BinaryTreeNode.__init__(self, value)
		self.key = key

	def setKey(self, key):
		"""Stores the given key in the node."""
		self.key = key

	def getKey(self):
		"""Returns the key stored in the node."""
		return self.key

	def put(self, key, value):
		"""Puts the key-value pair into the tree. If the key is already in the tree, then changes its value. Returns 0 if key was already in tree, 1 if it was not. That is, the return value is the net change in the number of nodes in the tree."""
		if key < self.key:
			# Put the key in the left side of the tree.
			if self.getLeftChild() == None:
				# Create a new node of whatever class this node is (useful for subclasses).
				self.setLeftChild(self.__class__(key, value))
				return 1
			else:
				return self.getLeftChild().put(key, value)
		elif key > self.key:
			# Put the key in the right side of the tree.
			if self.getRightChild() == None:
				self.setRightChild(self.__class__(key, value))
				return 1
			else:
				return self.getRightChild().put(key, value)
		else:
			# The key is right here; store the new value.
			self.setValue(value)
			return 0

	def get(self, key):
		"""Returns the value associated to the given key, or None if the key is not present."""
		if key < self.key:
			# Search the left side of the tree.
			if self.getLeftChild() == None:
				return None
			else:
				return self.getLeftChild().get(key)
		elif key > self.key:
			# Search the right side of the tree.
			if self.getRightChild() == None:
				return None
			else:
				return self.getRightChild().get(key)
		else:
			# The key must be right here.
			return self.getValue()

	def getLeastKey(self):
		"""Returns the least key in the tree."""
		left = self.getLeftChild()
		if left == None:
			return self.key
		else:
			return left.getLeastKey()

	def getNextKey(self, key):
		"""If the given key is greater than or equal to all keys in the gree, then returns None. Otherwise, returns the least key in the tree that is greater than the given key."""
		if key < self.key:
			# Try to get the next key out of the left subtree.
			left = self.getLeftChild()
			if left == None:
				return self.key
			else:
				next = left.getNextKey(key)
				if next == None:
					return self.key
				else:
					return next
		else:
			# Try to get the key out of the right subtree.
			right = self.getRightChild()
			if right == None:
				return None
			else:
				return right.getNextKey(key)

	def delete(self, key):
		"""Deletes the key-value pair associated to the given key from the tree. Returns a pair (root, change) where root is the new root of the tree and change is 0 or 1 indicating how many nodes were deleted. If the key is not in the tree, then does nothing. The key is in the tree if and only if change == 1. If one deletes the last key in the tree, then root == None."""
		if key < self.key:
			if self.getLeftChild() == None:
				# The key was not found.
				return (self, 0)
			else:
				# The key may be in the left subtree.
				(root, change) = self.getLeftChild().delete(key)
				self.setLeftChild(root)
				return (self, change)
		elif key > self.key:
			if self.getRightChild() == None:
				# The key was not found.
				return (self, 0)
			else:
				# The key may be in the right subtree.
				(root, change) = self.getRightChild().delete(key)
				self.setRightChild(root)
				return (self, change)
		else:
			# The key must equal the key stored here.
			if self.getLeftChild() == None:
				if self.getRightChild() == None:
					# There are no children.
					return (None, 1)
				else:
					# There is a right child but no left child.
					return (self.getRightChild(), 1)
			else:
				right = self.getRightChild()
				if right == None:
					# There is a left child but no right child.
					return (self.getLeftChild(), 1)
				else:
					# There are two children; replace self's key-value pair with the next greatest key-value pair.
					value = self.getValue()
					leastKey = right.getLeastKey()
					leastKeyValue = right.get(leastKey)
					(root, change) = right.delete(leastKey)
					self.setRightChild(root)
					self.setKey(leastKey)
					self.setValue(leastKeyValue)
					return (self, 1)

	def __str__(self):
		"""Returns a string to describe the tree. Key-value pairs are indicated with colons as in a dictionary's string, but there are also nested braces to show off the tree structure."""
		# Get the string for the root key and value.
		string = str(self.key) + ':' + str(self.getValue())
		# Get the string for the left subtree.
		if self.getLeftChild() == None:
			string = string + ', {}'
		else:
			string = string + ', ' + str(self.getLeftChild())
		# Get the string for the right subtree.
		if self.getRightChild() == None:
			string = string + ', {}'
		else:
			string = string + ', ' + str(self.getRightChild())
		return '{' + string + '}'

if __name__ == "__main__":
	myTree = BinarySearchTreeNode(13, "jan")
	print myTree
	myTree.put(17, "jane")
	print myTree
	myTree.put(23, "juan")
	print myTree
	myTree.put(14, "john")
	print myTree
	myTree.put(20, "ian")
	print myTree
	myTree.put(28, "joan")
	print myTree
	myTree.put(19, "johann")
	print myTree
	myTree = myTree.delete(17)[0]
	print myTree
	print "The height is", str(myTree.getHeight())
	key = myTree.getLeastKey()
	print "Here are the keys in order:"
	while key != None:
		print key
		key = myTree.getNextKey(key)
