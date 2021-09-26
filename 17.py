# Find majority element
def solve(arr):
    di = {}
    n = len(arr)
    for i in arr:
        if i in di:
            di[i] += 1
            if di[i] > n / 2:
                return i
        else:
            di[i] = 1
    return -1

arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))
