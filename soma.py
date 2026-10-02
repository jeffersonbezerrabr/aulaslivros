# Programa 8.20: Módulo soma (soma.py) que importa entrada

import entrada

L = []

for x in range(10):
    L.append(entrada.validar_inteiro(f"Digite o {x+1}º número: ", 0, 20))
    
print(f"Soma: {sum(L)}")