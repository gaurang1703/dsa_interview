# Find the duplicate element in a limited range array
def solve(arr):
    val = 0
    for i in arr:
        val = val ^ i
    for i in range(1, len(arr)):
        val = val ^ i
    return val

arr = list(map(int, input("Please enter the array: ").split()))
print(f"The duplicate element is: {solve(arr)}")

# This can also be solved as: actual_sum - expected_sum
# Since the array contains elements between 1 and n-1