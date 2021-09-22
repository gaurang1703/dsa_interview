# Shuffle an array using Fisher-Yates shuffle algorithm
from random import randrange

def solve(arr):
    for i in range(len(arr) - 1):
        j = randrange(i, len(arr))
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = list(map(int, input("Please enter the array: ").split()))
print(solve(arr))