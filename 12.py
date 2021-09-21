# Find the index of 0 to be replaced to get the maximum length sequence of continuous ones
def solve(arr):
    left = 0
    ind = 0
    ans = 0
    z_count = 0
    if arr[left] == 0:
        z_count += 1 
    for i in range(1, len(arr)):
        if arr[i] == 0:
            z_count += 1
            while z_count == 2:
                if arr[left] == 0:
                    z_count -= 1
                left += 1
            cur = i - left + 1
            if cur > ans:
                cur = ans
                ind = i
    return ind
            

arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))

# { 0 0 1 0 1 1 1 0 1 1 }