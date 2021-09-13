# Print all subarrays with sum 0
def solve(arr):
    ans = []
    sums = {0: [-1]}
    suma = 0
    for i,n in enumerate(arr):
        suma += n
        if suma in sums:
            end = i
            for start in sums[suma]:
                tmp = arr[start+1:end+1]
                ans.append(tmp)
            sums[suma].append(i)
        else:
            sums[suma] = [i]
    return ans

arr = list(map(int, input("Please enter the array: ").split()))
print(solve(arr))