# Longest bitonic subarray problem
def solve(arr):
    upward = True
    start = 0
    end = 0
    ans = -1
    fin = [0,0]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            if upward:
                end += 1
            else:
                cur = (end - start) + 1
                if cur > ans:
                    fin[0] = start
                    fin[1] = end + 1
                    ans = cur
                start = i - 1
                end = i 
                upward = True
        else:
            if upward:
                upward = False
                end += 1
            else:
                end += 1
    return arr[fin[0]: fin[1]]

arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))