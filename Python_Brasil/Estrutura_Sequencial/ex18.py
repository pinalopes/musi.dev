#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
import datetime
arq=float(input('Digite o tamanho do arquivo: ')) 
inter=float(input('Digite a velocidade da internet: '))
tpmin=int(arq/inter)
print(f'O tempo aproximado de download é de {tpmin} minutos')