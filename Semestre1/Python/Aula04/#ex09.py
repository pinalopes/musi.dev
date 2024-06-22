#ex09
agua=float(input('Digite o valor da sua conta de água:'))
luz=float(input('Digite o valor da sua conta de luz:'))
energia=float(input('Digite o valor da sua conta de energia:'))
salario=float(input('Digite o seu salário:'))
conta=agua+luz+energia
if salario<conta:
    print('Salário insuficiente!')
else:
    resto=salario-conta
    print('O saldo restante é:', resto)