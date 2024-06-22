#ex08
compra= float(input('Digite o valor da compra:'))
if compra>=200:
   valor=(compra+compra*20)/105 
   juros=compra-valor
   print('%.2f É o valor da sua compra' %(juros))
else:
   print('O valor da sua compra é:', compra)