# Longest Increasing Subsequence problem
def solve(arr):
    rdm = [1] * len(arr)
    j = 1
    while j < len(arr):
        i = 0
        while i != j:
            if arr[j] > arr[i]:
                rdm[j] = max(rdm[j], rdm[i] + 1)
            i += 1
        # print(f"at {arr[j]} rdm is {rdm}")
        j += 1
    return max(rdm)
    


# arr = list(map(int, input("Enter the array: ").split()))
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(solve(arr))