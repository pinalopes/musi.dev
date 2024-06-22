def calculaimc(a,kg):
    imc=kg/(a*a)
    return(imc)
kg=float(input('Digite o seu peso em kg: '))
a=float(input('Digite sua altura em m: '))
print('O seu imc é:',calculaimc(a,kg),'Kg/m')