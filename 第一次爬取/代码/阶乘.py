def func(n):
  if n == 1:
    return 1
  else:
    return n * func(n-1)
number = int(input("输入一个整数"))
print(func(number))