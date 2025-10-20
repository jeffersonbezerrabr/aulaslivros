#6.21.3 - Diferença - Página 195

#Entre as operações disponíveis com conjuntos, temos a diferença 
# entre conjuntos, que utiliza o operador -

A = {0, 1, 2, 3, -1}
B = {2, 3}

print(A - B)

print("*-*" * 25)

A = {1, 2, 3, 6}
B = {2, 4, 5, 6}

print(A - B)
print(A.difference(B))

#O Resultado contém apenas os elementos de A 
# que não estão presentes em B.

#Elementos unicos de A