vtc=float(input('Qual o valor total da compra?'))
qtdep=int(input('Quantas parcelas?'))
if qtdep==2:
    juros=(vtc+vtc*3)/100
    print('%.2f É o valor da sua conta com juros:' %(juros))
elif qtdep==4:
    juros=(vtc+vtc*7)/100
    print('%.2f É o valor da sua conta com juros' %(juros))
elif qtdep==6:
    juros=(vtc+vtc*9)/100
    print('%.2f É o valor da sua conta com juros' %(juros))
elif qtdep==8: 
    juros=(vtc+vtc*12)/100
    print('%.2f É o valor da sua compra com juros' %(juros))
else: 
    print('Quantidade de parcelas inválida')                                                              