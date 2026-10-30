#Os prints ultilizados nesses condigos são nescessario apenas se não estiver ultilizando o colab

#Propriedade = soma de parcelas iguais
"""
s=0
x_i=0.11
for i in range(30000):
    s=s+x_i
print(s)

#Ao calcular no papel obtemos resultados difentes,pois o computador ultiliza a representação binária para armazenar números float
#e o número 0,11 não possui representação binária assim ele é armazenado com a aproximação 3300.0000000006285

#DECIMAL -> BINARIO

print(bin(327))

#Pra retirar o prefixo 0b usamos o replace
print(bin(327).replace("0b","x="))
#101000111

#BINARIO -> DECIMAL
#Interprete o número na base binária 2
print(int("101000111",2))
#327
"""