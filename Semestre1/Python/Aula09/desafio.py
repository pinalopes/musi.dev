from random import*
num= randint(0,100)
resp=num
while resp==num:
    n=int(input('Digite um número: '))
    if n==num:
        print("Número digitado é o correto")
        break
    elif n<num:
        print("O número escolhido é maior")
    else:
        print("O número escolhido é menor")

