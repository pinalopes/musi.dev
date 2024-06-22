def pb(base,altura):
    area=base*altura/2
    return(area)

def inicio():
    print('Olá, tudo bem?')
    print('Hoje falaremos sobre parametros de um triângulo')
inicio()
base=int(input('Digite o valor da sua base: '))
altura=int(input('Digite o valor da sua altura: '))
print('O valor da área do seu triângulo é de:',pb(base,altura))