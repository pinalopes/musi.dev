#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area=int(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
litros=area/3
lata=int(litros/18)
if(litros%18!=0):
    lata+=1
print(f'Você tem que comprar {lata} latas')
print(f'O valor total é: {lata*80}')