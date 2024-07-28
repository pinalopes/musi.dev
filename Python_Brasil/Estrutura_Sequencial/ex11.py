#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo.
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
inteiro1=int(input('Digite um número inteiro: '))
inteiro2=int(input('Digite outro número inteiro: '))
real=float(input('Digite um número real: '))
r1=(inteiro1*2)*(inteiro2/2)
r2=(inteiro1*3)+real
r3=real**3
print(f'O primeiro resultado é: {r1}\nO segundo resultado é: {r2}\nO terceiro resultado é: {r3:.2f}')