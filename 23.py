# Maximum sum subarray problem
def solve(arr):
    suma = 0
    ans = 0
    for i in arr:
        suma = max(i, suma + i)
        ans = max(suma, ans)
    return ans


arr = list(map(int, input("Enter the array: ").split()))
solve(arr)
# -2 1 -3 4 -1 2 1 -5 4