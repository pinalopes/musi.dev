#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
valor_hora=float(input('Digite o valor que você ganha por hora: '))
hora_mes=int(input('Digite a quantidade de horas trabalhadas no mês '))
salario=valor_hora*hora_mes
print(f'O seu salário mensal é de {salario}')