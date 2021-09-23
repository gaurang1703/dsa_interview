# Rearrange an array with alternate high and low elements
def solve(arr):
    for i in range(1, len(arr), 2):
        if arr[i-1] > arr[i]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if i + 1 < len(arr) and arr[i+1] > arr[i]:
            arr[i+1], arr[i] = arr[i], arr[i + 1]
    return arr


arr = list(map(int, input("Please enter the array: ").split()))
print(solve(arr))
