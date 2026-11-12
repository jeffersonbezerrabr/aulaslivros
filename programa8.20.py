# Módulos

# Programa 8.20 - Módulo sona que importa o programa8.19 - Página 251

import programa8_19

L = []

for x in range(10):
    L.append(programa8_19.valida_inteiro("Digite um número: ", 0, 20))
print(f"Soma: {sum(L)}")
