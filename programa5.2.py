#Programa 5.2 - Página 147

#Podemos combinar vários *while* de forma a obter resultados mais interessantes,
#como a repetição com incrementos de duas variáveis. Imagine imprimir as
#tabuadas de multiplicação de 1 a 10. Vejamos como fazer isso.

#Programa 5.2 - Tabuada com repetições aninhadas

tabuada = 1

while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
    