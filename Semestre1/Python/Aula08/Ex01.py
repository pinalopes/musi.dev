pes=float(input('Qual o seu peso?'))
alt=float(input('Qual a sua altura?'))
imc= pes/(alt*alt)
if imc<20:
    #a formula %.2f e a %(imc) serve para formatar a saída, de forma que so mostre duas casas depois da vírgula
    print('%.2fAbaixo do peso' %(imc))
elif imc <25:
    print(imc,'Peso normal')
elif imc<30:
    print(imc,'Sobrepeso')
elif imc<40:
    print(imc,'Obeso')
else:
    print(imc,'Obeso mórbido')