while True: #o True serve para ser um código infinito até a pessoa digitar 0
    altura=float(input('Digite sua altura em metros (ou 0 para sair): '))
    if altura==0:
        break
    sexo=input('Digite o sexo (M para masculino e F para feminino) ').upper()#serve para a entrada do usuário seja toda maiúscula
    if sexo=='M':
        pi=(72.7*altura)-58
    elif sexo=='F':
        p1=(62.1*altura)-44.7
    else:
        print('Sexo inválido. ')
        continue
    print(f'O seu peso ideal é: {pi:.2f} kg')
    