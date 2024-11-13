"""

"""
def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort1(left) + middle  + quick_sort1(right)


arr1 = [5, 3, 8 , 4, 2]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(quick_sort1(arr2))
