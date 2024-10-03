def linear_search(arr, key):
    for index in range(len(arr)):
        # If the element is found, return its index
        if arr[index] == key:
            return index
    return -1

# Example usage:
arr = [10, 23, 45, 70, 11, 15]
key = 11

# Function call
result = linear_search(arr, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
