#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme 
# e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
fah=float(input('Digite a temperatura em Fahrenheit: '))
C=5*((fah-32)/9)
print(f'A temperatura {fah} em Fahrenheit é {C:.2f} em Celsius')#novo jeito de colocar os números após a vírgula