## 2022. Convert 1D array to 2D array

### Solution Explanation:

The idea here would be to generate a `m x n` matrix with all values set to `0` where `m` is the number of rows and `n` 
is the number of columns.

Now we can write a nested loop and fill in the matrix with all the values from the `original` array. We maintain an 
`index` variable to maintain the index of the `original` array. During each inner 
loop, we increment this value.
