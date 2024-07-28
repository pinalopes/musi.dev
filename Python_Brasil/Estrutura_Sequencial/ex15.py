#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
hs=float(input('Digite o valor que você ganha por hora: '))
horam=int(input('Digite quntas horas você trabalha no mês: '))
salariob=hs*horam
ir=salariob*0.11
inss=salariob*0.08
sindicato=salariob*0.05
salarioliq=salariob-ir-inss-sindicato
print(f'Salário Bruto: R${salariob}\nIR: R${ir}\nINSS: R${inss}\nSindicato: R${sindicato}\nSalário Líquido: R${salarioliq}')