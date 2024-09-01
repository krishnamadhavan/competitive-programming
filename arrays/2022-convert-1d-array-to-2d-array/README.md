## 2022. Convert 1D array to 2D array

### Solution Explanation:

A straight-forward solution would be a brute-force technique where we keep one of the values as a constant and loop 
through to check if any other values (excluding the current one) will add up to be the target value. 

We can use a nested for loop to achieve this, but the time complexity in this scenario would be O(n^2) - in the order 
of n squared. Where n is the number of elements in the array. 

To reduce the complexity to O(n), we can consider a trade-off on space complexity from O(1) to O(n). In this case, we 
can use a hashmap which holds the value of every item we've seen so far in the array and the index of that item.
By using hashmaps, we can reduce the time taken to loop through the array and have also avoided using nested loops.
