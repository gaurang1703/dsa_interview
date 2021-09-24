# Find equilibrium index of an array
def solve(arr):
    suma = sum(arr)
    ans = []
    so_far = 0
    for i in range(len(arr)):
        if abs(so_far) == abs(suma - arr[i] - so_far):
            ans.append(i)
        so_far += arr[i]
    return ans

arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))