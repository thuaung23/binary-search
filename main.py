# The following programs implements a simple binary search algorithm recursively and iteratively
# Written by: Thu Aung
# Written on: Dec 5, 2020

"""
A binary search algorithm works only on a sorted array or list in descending or ascending order. 
"""

def binary_search_re(arr, target, start, end):
  
  # Pick midpoint of an array.
  midpoint = (start+end) // 2

  # Check if the array is in ascending order.
  if end >= start:
    # Check if target is at midpoint. 
    if target == arr[midpoint]:
      return midpoint
    
    # If target is less than midpoint, it is in the left side of midpoint. (midpoint - 1) becomes the end of the new array.
    if target < arr[midpoint]:
      return binary_search_re(arr, target, start, midpoint-1)

    # If the target is greater than target, it is in the right side and the start is (midpoint+1).
    else:
      return binary_search_re(arr, target, midpoint+1, end)
  else:
      return -1

# The same logic as recursive method applies here.
def binary_search_it(arr, target):
  start = 0
  end = len(arr) - 1
  midpoint = 0

  while end >= start:
    midpoint = (start+end) // 2

    if arr[midpoint] == target:
      return midpoint
    elif arr[midpoint] > target:
      end = midpoint - 1
    else:
      start = midpoint + 1
    
  return False


arr = [1,2,3,4,5,6,7,8,9,10]
result_re = binary_search_re(arr, 6, 0, len(arr)-1)
print("The number being searched recursively is at index: ", result_re)
result_it = binary_search_it(arr, 11)
print("The number being searched iteratively is at index: ", result_it)
