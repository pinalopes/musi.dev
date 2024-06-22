idades=[]
qtde_votantes=0
soma_n_votantes=0
qtde_n_votantes=0
for i in range (5):
    idade=int(input(f'Digite sua idade {i+1}:'))
    if idade>=16:
        qtde_votantes=qtde_votantes+1
    else:
        soma_n_votantes=soma_n_votantes+idade
        qtde_n_votantes=qtde_n_votantes+1
if qtde_n_votantes>0:
    media=soma_n_votantes/qtde_n_votantes
else:
    media=0

print(f'A quantidade de alunos que podem votar é: {qtde_votantes}')
print(f'A media de alunos que não podem votar é:{media:.2f}')

    