#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c=float(input('Digite a temperatura em Celsius: '))
fah=c*9/5+32
print(f'A temperatura {c} em Celsius é {fah:.2f} em Fahrenheit')