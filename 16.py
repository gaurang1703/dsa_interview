# Find the largest subarray formed by consecutive integers

def solve(arr):
    di = {}
    left = 0
    ans = -1
    fin = [0, 0]
    for i in range(len(arr)):
        if arr[i] in di:
            cur = i - left 
            for j in range(0, cur):
                if j not in di or not di[j]:
                    break
            else:
                if cur > ans:
                    fin[0] = left
                    fin[1] = i
            while di[arr[i]]:
                di[arr[left]] -= 1
                left += 1
        di[arr[i]] = 1
    return arr[fin[0]: fin[1]]


arr = list(map(int, input("Enter the array: ").split()))
print(solve(arr))