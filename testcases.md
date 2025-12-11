# Test Cases

## Test Case 1 (standard)
Frames = 3  
Reference String = 7 0 1 2 0 3 0 4 2 3 0 3  
Expected: FIFO=9, LRU=8, Optimal=7

## Test Case 2
Frames = 4  
Reference String = 1 2 3 4 1 2 5 1 2 3 4 5  
Expected: FIFO=10, LRU=8, Optimal=6

## Test Case 3 (sequential)
Frames = 3  
Reference String = 1 2 3 4 5 6 7  
Expected: FIFO=7, LRU=7, Optimal=7
