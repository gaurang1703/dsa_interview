# Maximum sum subarray problem
def solve(arr):
    ans = 0
    start = 0
    end = 0
    suma = 0
    beg = 0
    for i in range(len(arr)):
        suma += arr[i]
        if arr[i] > suma:
            suma = arr[i]
            beg = i
        if suma > ans:
            ans = suma
            start = beg
            end = i
    print(f"length = {ans}, subarray = {arr[start: end + 1]}")


arr = list(map(int, input("Enter the array: ").split()))
solve(arr)
# -2 1 -3 4 -1 2 1 -5 4