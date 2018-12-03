import random
secret = random.randint(1,10)
temp = input('请输入您的数字：')
guess = int(temp)
while guess != secret:
    if guess > secret:
        temp = input('大了请重新输入:')
        guess = temp
    else:
        temp = input('小了请重新输入:')
        guess = temp
print('结束')
        
