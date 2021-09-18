# Find the largest subarray having an equal number of 0s and 1s
def solve(arr):
    suma = 0
    seen = {0: [-1]}
    ans = float('-inf')
    ans_start = -1
    ans_end = -1
    for n,i in enumerate(arr):
        if i == 0:
            suma -= 1
        else:
            suma += 1
        if suma in seen:
            for ind in seen[suma]:
                cur = n - ind
                if cur > ans:
                    ans = cur
                    ans_start = ind
                    ans_end = n
            seen[suma].append(n)
        else:
            seen[suma] = [n]
        
    return arr[ans_start+1: ans_end+1] if ans_start != -1 else "Does not exist"

arr = list(map(int, input("Enter the array: ").split()))
print(f"Largest subarray is: {solve(arr)}")
