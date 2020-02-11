#Aula 10/02/2020

#If/Else

nota = int(input("Digite sua nota: "))

if nota == 10:
    print("Parabéns! Nota máxima!")
elif nota > 6 and nota < 10:
    print("Ok, sua nota foi",nota)
else:
    print("Se esforce mais.")