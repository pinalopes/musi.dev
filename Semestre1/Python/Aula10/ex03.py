cont=0
idade=0
qtde40=0
sl40=0
p2=0
while True:
    i=int(input('Digite a sua idade (ou negativa para sair) '))
    if i<=0:
        break
    salario=float(input("Digite seu salário: "))
    cont=cont+1
    idade=idade+i
    if i>=40:
        qtde40=qtde40+1
        sl40=sl40+salario
    if salario<2000:
        p2=p2+1
if cont>0:
    mi=idade/cont
    ms=sl40/qtde40 if qtde40>0 else 0
    print('A média de idade do grupo é de:',mi)
    print('A média de salário das pessoas com mais de 40 anos é de:',ms)
    print('A quantidade de pessoas recebendo menos de 2000 é:',p2)
else:
    print('Nenhum dado informado')

