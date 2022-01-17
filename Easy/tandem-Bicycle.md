# Tandem Bicycle
- Given 2 list: `redShirtSpeed`, `blueShirtSpeed`, each rider is represented by a single positive integer, which is the speed that they pedal a tandem bicycle at. `tandemSpeed = max(speedA, speedB)`
- Both list have the same length
- Your goal is to pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bicycle
- Write a function that returns the maximum possible total speed or min possible total speed of all of the tandem bicycles being ridden based on an input parameter, `fastest`. If `fastest = True`, your function should return the maximum possible total speed, otherwise minimum total speed.
- Total Speed is defined as the sum of the speeds of all the tandem bicycles being ridden.
```
Input

redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = True

Output:
32
```
## Hint:
- The brute-force approach to solve this problem is to generate every possible set of pairs of riders and to determine the total speed that each of these sets generates.
- Try to looking at the input arrays in sorted order
- When generating the maximum total speed, you want to pair the slowest red shirt rider with fastest blue rider
- When generating the minimum total speed, you want to pair the fastest red-shirt riders with the fastest blue-shirt rider to eliminate a large speed by pairing it with a another larger speed.
