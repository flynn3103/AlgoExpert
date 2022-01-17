# Depth-first Search
Question: <br>
You're given a Node class that has `name` and an array of optional `children` nodes.When put together, node form an acyclic tree-like struture.
Implement the `depthFirstSearch` method on the Node class

Hint:

- DFS works by traversing a graph branch by branch. Before traversing sibling Nodes,its children nodes must be traversed
- Start at the root Node and call DFS method on all of its children Nodes. Then call DFS method on all children Nodes of each child node. Keep applying this logic until the entire graph has been traversed. Don't forget to add the current Node's name to the input array at every call DFS.


~~~python
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
	def depthFirstSearch(self, array):
		array.append(self.name)
		for child in children:
			child.depthFirstSearch(array)
		return array
~~~