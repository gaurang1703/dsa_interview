# Find the maximum product of two integers in an array
def solve(arr):
    tmp = sorted(arr)
    return max(tmp[0] * tmp[1], tmp[-1] * tmp[-2])

arr = list(map(int, input("Enter the array: ").split()))
print(f"The largest sum is: {solve(arr)}")

# This solution takes O(n.logn)
# But essentially we need the smallest, second smallest, largest and the second largest element, hence the problem can be solved in linear O(n) time
