def factrial(n):
    if n <= 2:
        return 1
    else:
        return factrial(n - 1) + factrial(n - 2)

number = int(input('请输入月份数：'))
result = factrial(number)
print(result)
