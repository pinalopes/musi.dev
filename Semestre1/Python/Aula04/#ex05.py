#ex05
import math

num=float(input('Digite um número qualquer:'))
if num>0:
    r=math.sqrt(num)
    print('A raíz quadrada do número digitado é:', r)
else:
    print('Não é possível calcular raíz quadrada de número negativo')