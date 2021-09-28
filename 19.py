# Replace every array element with the product of every other element without using a division operator
def solve(arr):
    left = [1, None, None, None, None]
    right = [None, None, None, None, 1]

    for i in range(1, len(arr)):
        left[i] = left[i-1] * arr[i-1]
    for j in range(len(arr) - 2, -1, -1):
        right[j] = right[j + 1] * arr[j+1]

    for i in range(len(arr)):
        arr[i] = left[i] * right[i]
    return arr



arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))
