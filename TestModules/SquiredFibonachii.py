import math
a = 0
b = 1
sum = 0

limit = int(input("Enter the Limit :: "))
for i in range(limit):
    sum = math.pow(a, 2) + math.pow(b, 2)
    print(sum)
    a = b
    b = sum

