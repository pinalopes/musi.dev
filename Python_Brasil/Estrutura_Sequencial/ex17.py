#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem 
# compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
area=int(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
litros=area/6*1.1
lata=int(litros/18)
galao=int(litros/3.6)
if(litros%18!=0):
    lata+=1
if(galao%3.6!=0):
    galao+=1
    
mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print(f'Latas: {lata} Valor: {lata * 80}')
print(f'Galoes: {galao} Valor: {galao * 25}')
print(f'Latas: {mixLatas} e {mixGaloes} Valor:\n{mixLatas * 80}+{mixGaloes*25}')

