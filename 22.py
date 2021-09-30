# Find the maximum difference between two array elements that satisfies the given constraints
def solve(arr):
    ans = -1
    big = -1
    big_ind = -1
    smol_ind = -1
    for i in range(len(arr) - 1, -1, -1):
        cur = arr[i]
        if cur > big:
            big = cur
            big_ind = i
        else:
            diff = big - cur
            if diff > ans:
                ans = diff
                smol_ind = i

    print(ans)
    return [arr[smol_ind], arr[big_ind]]


arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))
# 2 7 9 5 1 3 5