email=input('Digite seu e-mail: ')
partes=email.split('@')
if len(partes)==2:
    dominio=partes[1]
    print(f'O domínio do seu e-mail é: http://{dominio}')
else:
    print('e-mail inválido')