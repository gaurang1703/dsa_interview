# Check if a subarray with 0 sum exists
arr = list(map(int, input("Enter the array: ").split()))
s = set()
suma = 0
for i in arr:
    suma += i
    if suma in s:
        print("Subarray with zero sum exists")
        break
    else:
        s.add(suma)
else:
    print("Subarray with zero sum does not exist")
