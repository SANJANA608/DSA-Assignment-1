#Bubble sort
arr = [5,4,6,9,10]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
print("sorted Arrays",arr)


#Quick sort
import random
def Quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]

    return Quicksort(left) + middle + Quicksort(right)

arr = [5,4,6,9,10]
print("Before sorting:",arr)
print("After sorting:",Quicksort(arr))


#Insertion sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be positioned
        j = i - 1     # Index of the last sorted element

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)


#Selection sort
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
print("unsorted array:", arr)
selection_sort(arr)
print("Sorted array:", arr)


#Merge sort
def mergesort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[ :middle]
        right = arr[middle: ]

        mergesort(left)
        mergesort(right)

        lp = 0
        rp = 0
        fp = 0

        while(lp < len(left) and rp < len(right)):
            if left[lp] < right[rp]:
                arr[fp] = left[lp]
            else:
                arr[fp] = right[rp]
                rp += 1
                fp += 1
        while lp < len(left):
                arr[fp] = left[lp]
                fp += 1
                lp += 1
        while rp < len(right):
                arr[fp] = right[rp]
                fp += 1
                rp += 1



arr = [4,2]
print("Before merge sort",arr)
mergesort(arr)
print("after merge sort",arr)
