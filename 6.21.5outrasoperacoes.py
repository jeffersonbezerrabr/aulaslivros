#6.21.5 - Outras operações - Página 196

#Você também pode fazer outras operações com conjuntos,
#como saber se um conjunto contém outro.

A = {x for x in range(0, 10, 2)}
print(A)
B = {2, 4}

#Podemos verificar se um conjunto contém o outro usando o maior(>):

print(A > B)
print(B > A)

print("*-*" * 25)

#Veja que, quando os conjuntos têm os mesmos elementos
#ou são iguais, o resultado do > é False:

print(A > A)
print(B > {2, 4})

print("*-*" * 25)

#Um conjunto é maior ou igual a outro  quando contém o outro:

print(A >= B)
print(B >= A)

print("*-*" * 25)

#E mesmo quando são iguais:

print(A >= A)
print(B >= {2, 4})

print("*-*" * 25)

#O inverso é valido para a operação com <(menor ou está contido):

print(A < B) #A está contido em B
print(B < A)
print (A <= B) #A está contido em B e não é igual a B
print(B <= A) #B está contido em A? (Todos os elementos de B são elementos de A)
print(A <= A)

print("*-*" * 25)

#Da mesma forma, == pode ser usado para verificar se os conjuntos têm
#os mesmos elementos e != para verificar se há elementos diferentes:

print(A == A)
print(A == B)
print(B == {2, 4})
print(A != A)
print(A != B)
print(B != {2, 4})

#E é claro, podemos testar se um conjunto é vazio:

if {}:
    print("Não vazio")
else:
    print("Vazio")

print("*-*" * 25)

E = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
F = [3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19]

print(set(E) | set(F))