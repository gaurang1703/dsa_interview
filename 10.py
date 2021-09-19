# In-place merge two sorted arrays
def solve(x, y):
    start = 0
    while True:
        if y[0] > x[-1] or start >= len(x):
            print("New X: ", x)
            print("New Y: ", y)
            return 
        if x[start] > y[0]:
            x[start], y[0] = y[0], x[start]

            tmp = y[0]
            for i in range(1, len(y)):
                if y[i] < tmp:
                    y[i-1], y[i] = y[i], y[i-1]
        start += 1
    


x = list(map(int, input("Enter array X: ").split()))
y = list(map(int, input("Enter array Y: ").split()))
solve(x, y)