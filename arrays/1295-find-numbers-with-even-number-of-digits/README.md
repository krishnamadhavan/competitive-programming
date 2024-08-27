## 1295. Find numbers with even number of digits

### Solution Explanation:

The idea here is to divide the number by 10 until the quotient of the division is 0. Say, for example, the number 6789, 
after dividing 4 times, the quotient becomes 0. So, with this process, we can runa while loop until the `num` 
becomes 0. 

We can use a counter to increment the value for every iteration. Then we can use the bitwise `AND` operator to 
determine whether the no. of digits is even or odd.
