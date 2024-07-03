lista=[]
print(
    """===CONVERSOR DE BASES==="""
)
n=int(input('Digite o número: '))
print(""""
[1]BINÁRIO
[2]HEXADECIMAL
[3]OCTAL
""")
opção=int(input('Digite o número da opção desejada: '))
if opção==1:
    while n>=2:
        resto=n%2
        divisao=n//2
        n=divisao
        lista.insert(0,resto)
        print(divisao,lista)
elif opção==2:
    numeros_decimais='0123456789ABCDEF'
    while n>0:
        resto=n%16
        divisao=n//16
        n=divisao
        lista.insert(0, numeros_decimais[resto])
        print(divisao,lista)
elif opção==3:
    while n >=8:
        resto=n%8
        divisao=n//8
        n=divisao
        lista.insert(0,resto)
        print(divisao,lista)
else:
    print('O número digitado não corresponde aos selecionados')