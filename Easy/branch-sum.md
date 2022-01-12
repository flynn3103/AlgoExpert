# Branch Sums

Write a function that takes in a Binary Tree and returns a list of branch sums ordered from leftmost branch sum to rightmost branch sum

Sample Input:
```py 
tree = 1
     /   \
    2     3
   / \   /  \
  4   5  6   7

Output: [7,8,10,11]
```
Hint:
- Try travesing the Binary Tree in DFS like fashion
- Pass a running sum of the values of every previously-visited node to each node that you're traversing.
- When recursively traverse the tree, if you reach the leaf node, add the relevant running sum that you've calculated to a list of sums(which you'll also have to pass to the recursive function)
- If you reach a node that isn't a leaf node, keep recursively traversing its children nodes, passing the correctly updated running sum to them

```py
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(root):
    sums = []
    runningSumBST(root,0,sums)
    return sums

def runningSumBST(node, runningSum, sums):
    if node is None:
        return 
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
    runningSumBST(node.left, newRunningSum, sums)
    runningSumBST(node.right, newRunnignSum, sums)
```