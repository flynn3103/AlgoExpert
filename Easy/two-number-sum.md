# Two Number Sum

## Understand the problem
Given an array of integers, no number in this array is repeated, and an integer representing the target sum, implement a function that find whether there's a pair of numbers in the array that adds up to the target sum. Return the pair in an array. If such pair does not exist, return an empty array.

Input:
```py
array = [3, 5, -4, 8, 11, 1,-1, 6]
targetSum = 10
```
Output: 
```
[-1, 11] // the number could be in reverse order
```

## Approach 1
Iterate through every number in the array. At each number, traverse through the rest of the array, if adding any number in the rest of the array to the number yields the target sum, return the pair.

```py
def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        firstNum = array[i]
        for j in range(len(array)):
            secondNum = array[i+1]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

```



### Time & Complexity Approach 1

>O(n^2) time | O(1) space, where n is the length of the input array.

## Approach 2
- I can solve the problem by looping through each integer in the array and find if there is another integer in the rest of array that is equals to target_sum - current_integer. 
- But that means I have to use a nested for loop, the outer for loop traverses the array and the inner for loop traverses the rest of the array to find the complement. 
- Instead of the nested for loop, I can keep track of the complement of each integer (target sum - integer) in a hash table, which provides a constant-time lookup on average. In the hash table, the key is the complement and the value is the integer. At each iteration, look up the integer in the hash table, if it is already in the hash table, then the pair is found, return the pair, otherwise, calculate the complement and add the key/value pair into the hash table. If I get out of the for loop without returning the pair, return an empty array.

```py
def twoNumberSum(array, targetSum):
    hashTable = {}
    for num in array:
        diff = targetSum - num
        if diff in hashTable:
            return [diff, num]
        else:
            hashTable[num] = True
    return []
```



### Time & Complexity Approach 2

>O(n) time | O(n) space, where n is the length of the input array.

## Approach 3
Use two pointers approach. 
- First sort the array in ascending order. 
- Then initialize two pointers, one pointing to the first element in the sorted array, and the other pointing to the last element in the sorted array. 
- Sum up the values that the two pointers point to. 
- If their sum is smaller than the targetSum, shift the left pointer to right by one, because the array is sorted in ascending order, if I move the right pointer to left, the new sum is even smaller than the current sum, which is already smaller than the targetSum. 
- If their sum is greater than the targetSum, shift the right pointer to left by one. Keep moving the pointers until I get the sum as targetSum or the pointers get equal to each other, which means the pointers are pointing to the same number.

```py
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
```



### Time & Complexity Approach 3

>O(n) time | O(n) space, where n is the length of the input array.