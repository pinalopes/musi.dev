vc=float(input('Digite o valor da sua compra:'))
if vc<10:
    lucro=(vc+vc*7)/10
    print('%.2fO valor da venda é' % (lucro))
elif vc<=10 and vc <30:
    lucro=(vc+vc*5)/10
    print('O valor de venda é', lucro)
elif vc<=30 and  vc<50:
    lucro=(vc+vc*4)/10
    print('O valor do produto é', lucro)
else:
    lucro=(vc+vc*3)/10
    print('O valor do produto é', lucro)