# coding=utf-8
n = int(input("Input N: "))
a = 0
b = 1
sum = 0
for i in range(n):
    sum += a
    a, b = b, a+b
print("The sum of", n, "FIB is", sum, "!")
