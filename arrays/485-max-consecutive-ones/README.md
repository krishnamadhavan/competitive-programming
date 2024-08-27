## 485. Max Consecutive Ones

### Solution Explanation:

- We declare two variables `counter` to hold the current window of consecutive ones and `max_ones` to hold the largest 
number of all consecutive ones' windows. The default values of both these variables are set to `0`.

- We iterate over the binary array, and check if the value is `1`. If yes, we increment the value of `counter` by 1. 
Additionally, we compare the current value of `counter` and `max_ones`.

- Since the problem statement is to return the max consecutive ones, we update the value of `max_ones` to the maximum 
value of `counter` vs `max_ones`.

- While iterating, if the value of `num` is 0, it means that the consecutive ones window has ended. Hence, we reset the 
value of `counter` to 0.

