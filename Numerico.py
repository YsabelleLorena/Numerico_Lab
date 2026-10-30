#Os prints ultilizados nesses condigos são nescessario apenas se não estiver ultilizando o colab

#Propriedade = soma de parcelas iguais

s=0
x_i=0.11
for i in range(30000):
    s=s+x_i
print(s)

#Ao calcular no papel obtemos resultados difentes,pois o computador ultiliza a representação binária para armazenar números float
#e o número 0,11 não possui representação binária assim ele é armazenado com a aproximação 3300.0000000006285

#====================DECIMAL -> BINARIO====================

print(bin(327))

#Pra retirar o prefixo 0b usamos o replace
print(bin(327).replace("0b","x="))
#101000111

#====================BINARIO -> DECIMAL====================
#Interprete o número na base binária 2
print(int("101000111",2))
#327

#====================NUMEROS FRACIONARIOS====================
import numpy as np
#!pip instal binary-fractions
from binary_fractions import Binary
# 
#No powershell é nescessario instalar:python -m pip install numpy binary-fractions

print(Binary(0.11))
#0b0.00011100001010001111010111000010100011110101110000101001

#====================TRUNCAR====================
#retira 0b
print(str(Binary(0.125)).replace("0b","x="))

#x=0.001

#====================BINARIO FRACIONARIO -> DECIMAL====================