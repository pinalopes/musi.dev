contP=0
acumuladorp=0
contN=0
acumuladorn=0
resp='s'
while resp=='s' or resp=="S":
    n=int(input("Digite um número: "))
    if n>=0:
        contP=contP+1
        if n<acumuladorp:
            acumuladorp=acumuladorp+n
    else:
        contN=contN+1
        if n<acumuladorn:
            acumuladorn=acumuladorn+n
    resp=input("Deseja continuar (S/N)?")
    
print("O número de valores positivos é de:",contP,'e o número de negativos é de:',contN)
print("O menor número positivo é: ",acumuladorp,'O menor número negativo é:',acumuladorn)
