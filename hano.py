def hano(n, a, b, c):
    '''
    汉诺塔的递归实现
    n：代表几个盘子
    a：代表第一个盘子
    b：代表第二个盘子
    c：代表第三个盘子
    '''
    if n == 1:
        print(a, '-->', c)
        # return None
    if n == 2:
        print(a, '-->', b)
        print(a, '-->', c)
        print(b, '-->', c)
        # return None
    # 第一步，把A上n-1个盘子借助C挪到B上
    hano(n - 1, a, c, b)
    print(a, '-->', c)
    # 吧n-1个盘子借助A挪到C上
    hano(n - 1, b, a, c)


# if 语句若不加return结果不一样  ！！！
a = "A"
b = "B"
c = "C"

n = 2
hano(n, a, b, c)


