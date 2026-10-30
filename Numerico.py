#==========================================================================================#
#=====================================AULA 01==============================================#
#==========================================================================================#

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
print(float(Binary("0.001")))
print(float(Binary("0.00011100001010001111010111000010100011110101110000101001")))

#====================CONVERSÃO DECIMAL -> QUALQUER BASE====================
x=0.3457
binario = "" #variavel que armazena bits encontrados(0 e 1)
base = 2
casas = 50# quantidade de casas binarias a serem calculadas
for i in range(casas):
  x=x*base#multiplica a parte fracionaria por 2
  bit=int(x) ##pega a parte inteira do x (0 ou 1)##
  print(f"Passo {i+1}: valor multiplicado={x:.10f},bit={bit}")
  binario += str(bit)
  x = x - bit
print("\nResultado final em binário:")
print("0."+binario)

#0,3457 _10
#0,3457*2 = 0,6914 (0)
#0,6914*2 = 1,3828 => 0,3828 (1)
#0,3828*2 = 0,7656 (0)
#0,7656*2 = 1,5312 =>0,5312 (1)
#0,5312*2 = 1,0624 =>0,0624 (1)
#0,0624*2 = 0,1248 (0)

#010110

#====================HEXADECIMAL====================

x=0.3457
hex_frac=" "
base=16
casas = 100
hex_digits= "0 1 2 3 4 5 6 7 8 9 A B C D E F"
for i in range(casas):
  x=x*base
  inteiro = int(x)
  print(f"Passo{i+1}:Valor multiplicado ={x:.12f},digito={hex_digits[inteiro]}")
  hex_frac += hex_digits[inteiro]
  x=x-inteiro
print("\n Resultado final em hexadecimal:")
print("0."+hex_frac)

#0.  4  6  1 51 6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000