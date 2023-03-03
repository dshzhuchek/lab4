from random import randint
n=0
while n!=3:
    a=randint(0,11)
    b=randint(0,11)
    print(a,' + ', b,' = ' )
    i=int(input())
    if a+b==i:
        print('Правильно!')
    else:
        n+=1
        print('Ответ неверный')
if n==3:
    print('Игра закончена')