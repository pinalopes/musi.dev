idade=int(input('Qual a sua idade?'))
if idade<16:
    print('Você é não eleitor')
elif idade>=18 and idade<=65:
   print('Você é obrigado a votar')
else:
    print('Eleitor Facultativo')