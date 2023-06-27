# ZyLab 6.22
# Benjamin Ojode
# 1663352

# Getting inputs for linear equation coefficients
a = int(input())
b = int(input())
c = int(input())
a_2 = int(input())
b_2 = int(input())
c_2 = int(input())

# variable to limit output to a single value
i = 'no'

# Brute force of the equations
for x in range(-10, 10):
    for y in range(-10, 10):
        if (a * x + b * y == c) and (a_2 * x + b_2 * y == c_2):
            i = 'yes'
            print(x, y)

if i == 'no':
    print('No solution')
