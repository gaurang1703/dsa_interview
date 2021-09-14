# Sort binary array in linear time
def solve(arr):
    ans = []
    for i in arr:
        if i == 0:
            ans = [0] + ans
        else:
            ans.append(1)
    return ans
    


arr = list(map(int, input("Please enter the array: ").split()))
print(solve(arr))