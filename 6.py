# Find maximum length subarray having given sum
def solve(arr, target):
    di = {0:[-1]}
    suma = 0
    max_length = -1
    ans_start = -1
    for n,i in enumerate(arr):
        suma += i
        if suma - target in di:
            for ind in di[suma - target]:
                tmp = n - ind
                if tmp > max_length:
                    max_length = tmp
                    ans_start = ind
        if suma in di:
            di[suma].append(n)
        else:
            di[suma] = [n]
    return arr[ans_start+1: ans_start + max_length+1]

arr = list(map(int, input("Enter the array: ").split()))
target = int(input("Enter the target: "))
print(solve(arr, target))