#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
sexo=str(input('Digite seu gênero: M/F'))
alt=float(input('Digite sua altura: '))
if sexo=='m' or sexo=='M':
    h=72.7*alt-58
    print(f'Seu peso ideal é {h:.2f}')
elif sexo=='f' or sexo=='F':
    m=62.1*alt-44.7
    print(f'Seu peso ideal é {m:.2f}')
else:
    print('Letra errada.')