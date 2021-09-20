# Merge two arrays by satisfying given constraints
def solve(x, y):
    # move non empty elements of x to the begining 
    j = 0
    for i in range(len(x)):
        if x[i]:
            x[j] = x[i]
            j += 1
    x_pos = len(x) - len(y) - 1
    y_pos = len(y) - 1
    k = len(x) - 1
    while x_pos > -1 and y_pos > -1:
        if x[x_pos] >= y[y_pos]:
            x[k] = x[x_pos]
            x_pos -= 1
            k -= 1
        else:
            x[k] = y[y_pos]
            y_pos -= 1
            k -= 1

    while y_pos > -1:
        x[k] = y[y_pos]
        k -= 1
        y_pos -= 1
    return x


x = list(map(int, input("Enter first array: ").split()))
y = list(map(int, input("Enter second array: ").split()))
print(solve(x, y))

# 0 2 0 3 0 5 6 0 0
# 1 8 9 10 15