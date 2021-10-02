# Maximum Sum Cirbular Subarray
def solve(arr):
    arr += arr
    suma = 0
    ans = 0
    for i in arr:
        suma = max(i, suma + i)
        ans = max(ans, suma)
    return ans
    

arr = list(map(int, input("Enter the array: ").split()))
print(sum(arr))
print(solve(arr))