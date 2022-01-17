# Class Photos
- All these students are wearing Blue and Red Shirt. You are responsible for arranging the student in 2 rows with condition:
	- Red Shirt must be in the same row.
	- Blue Shirt are same row
	- Each student in the back row must be strictly tailer than student directly in front of them in front row.

```
Input:
redShirtHeights = [5,8,1,3,4]
blueShirtHeights = [6,9,2,4,5]

Output:
True
```

Hint:
- Sort 2 Array with reverse == True
- Pick which color is the first row, which one is in the back row
- 
~~~python
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	shirtColorFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	for idx in range(len(redShirtHeights)):
		red = redShirtHeights[idx]
		blue = blueShirtHeights[idx]
		if shirtColorFirstRow == "RED":
			if red >=blue :
				return False
		else:
			if blue >= red:
				return False

    return True
~~~