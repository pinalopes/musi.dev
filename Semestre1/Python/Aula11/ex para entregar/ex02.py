valores=[]
par=[]
impar=[]
resp='s'
while resp=='s' or resp=='S':
    n=int(input('Digite um número inteiro (ou "s" para finalizar): '))
    valores.append(n)
    resp=input('Deseja continuar?(S/N)')
for n in valores:
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
print('Valores',valores)
print('Valores par',par)
print('Valores ímpar',impar)
