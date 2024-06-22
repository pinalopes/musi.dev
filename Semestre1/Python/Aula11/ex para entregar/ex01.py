num=[]
resp='s'
while resp=='s' or resp=='S':
    n=int(input('Digite um número: '))
    num.append(n)
    resp=input('Deseja continuar(S/N)? ')
soma=sum(num)
media=soma/len(num)
nmd=[numeros for numeros in num if numeros>media]
print('Soma:',soma)
print('Média:',media)
print('Números maiores que a média:',len(nmd))
