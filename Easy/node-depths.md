# Node Depths

Write a function that takes in a Binary Tree & return nodes'depths

Hint:
- As obvious as it may seem, to solve this question, you'll have to figure out how to compute the depth of any given node; once you know how to do that, you can compute all of the depths and add them up to the desired output.

- To compute the depth of a given node, you need information about its positions in the tree, pass this information down from the node's parent.

- The depth of any node in the tree is equal to the depth of its parent node + 1. By starting at the root node whose depth is 0, you can pass down to every node in the tree ts respective depth, and you can implement the algorimth that does this and that sums up all f the depths recursively or iteratively

```py
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node":root, "depth":0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepth += depth
        stack.append([{"node":node.left, "depth":depth + 1}])
        stack.append([{"node":node.right, "depth":depth + 1}])
    return sumOfDepths
```