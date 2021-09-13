# Find a pair with the given sum in an array
def solve(arr, target):
    req = set()
    for i in arr:
        diff = abs(target - i)
        if diff in req:
            return [diff, i]
        else:
            req.add(i)
    return False

arr = list(map(int, input("Enter the array: ").split()))
target =int(input("Enter the target: "))
ans = solve(arr, target)
if ans:
    print(f"Pair found: {ans[0], ans[1]}")
else:
    print("Pair not found")