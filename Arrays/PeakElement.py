## Problem Link : https://practice.geeksforgeeks.org/problems/peak-element/1
## An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
## Given an array arr[] of size N, Return the index of any one of its peak elements.
## Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 

def peakElement(self,arr, n):
  if n == 0:
      return 0        
  if n == 1:
      return 0           
  if n == 2:
      return 0 if arr[0] >= arr[1] else 1        
  i = 0
  while i < n:
      if i == 0:
          if arr[i] >= arr[i+1]:
              return i           
      elif i == n-1:
          if arr[n-1] >= arr[n-2]:
              return n-1              
      else:
          if arr[i-1] <= arr[i] and arr[i] >= arr[i+1]:
              return i                    
      i += 1

## Input:  N = 3, arr[] = {1,2,3}
## Possible Answer: 2
## Generated Output: 1
## Explanation: index 2 is 3. It is the peak element as it is greater than its neighbour 2. If 2 is returned then the generated output will be 1 else 0.
