def binarysearch(arr,a,low,high):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == a:
            return mid
        elif arr[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
            return -1

        #Example usage
arr = [1,2,3,4,5,6,7,8]
a = 5
print("The array is",arr)
print("Element to be found is",a)



