# Move all zeros present in the array to the end
def solve(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[k] = arr[i]
            k += 1
    for i in range(k, len(arr)):
        arr[i] = 0
    return arr

arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))