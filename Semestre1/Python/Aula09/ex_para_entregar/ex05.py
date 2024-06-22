m=0
f=0
contm=0
contf=0
resp='s'
while resp=='s' or resp=='S':
    s=int(input('Qual seu sexo (1=M/2=F)? '))
    alt=float(input("Qual a sua altura em centímetros? " ))
    if s==1:
        m=m+1
        contm=contm+alt
    elif s==2:
        f=f+1
        contf=contf+alt
    else:
        print('Número negado.')
        break
    resp=input("Deseja continuar(S/N)? ")

print('A altura média dos homens é',contm/m)
print('A altura média das mulheres é', contf/f)
