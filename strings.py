#Aula 05/02/2020
'''
upper()
lower()
len()
replace("str", 'str')
count('str')
find('str')
title()
'''

#upper() - Transforma em maiúscula.
strUP = 'guilherme de souza'
strUP = strUP.upper()
print("Upper:")
print(strUP)

#lower() - Transforma em minúscula.
strLOW = 'GUILHERME DE SOUZA'
strLOW = strLOW.lower()
print("Lower:")
print(strLOW)

#len() - Conta a quantidade de caracteres armazenados, incluindo espaços.
print("Len:")
print('Letras na variavel strUP:',len(strUP))

#replace() - Sobrescreve a primeira palavra com a segunda palavra definida.
strUP = strUP.replace('DE SOUZA', 'OLIVEIRA')
print("Replace:")
print(strUP)

#count() - Conta a quantidade de caracteres definido no código.
print("Count(Letra):")
print(strUP.count('E'))
print("Count(Espaço):")
print(strUP.count(' '))

#find() - Diz a posição da string procurada, começando da posição zero.
print("Find:")
print(strUP.find('E'))

#title() - Função para deixar todas as primeiras letras maiúsculas.
print("Title:")
strLOW = strLOW.title()
print(strLOW)