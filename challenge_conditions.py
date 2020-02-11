#Challenge 10/02/2020

#Sistema para uma universidade:
#O Sistema deve solicitar 
# -Nome
# -Idade
# -Nota de duas provas deste aluno.
# Mostrar como saída o nome dele apenas com as letras iniciais em maiúsculo, independente de como for digitado.
# Mensagem se foi aprovado ou reprovado
# Só será aprovado caso a média for 6 ou maior
# E idade seja maior ou igual a 18

name = input("Digite o nome: ")
year = int(input("Digite a idade: "))

n1 = int(input("Digite a nota da prova 1: "))
n2 = int(input("Digite a nota da prova 2: "))

media = ((n1+n2)/2)

name = name.title()

print(name)

if media >= 6 and year >= 18:
    print("Parabéns! Você foi aprovado!")
else:
    print("Você foi reprovado, sinto muito.")
