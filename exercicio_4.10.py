# Exercício 4.10 - Página 130

# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada.

while True:
    try:
        n1 = float(input("Informe o primeiro número: "))
        
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

while True:
    try:
        n2 = float(input("Informe o segundo número: "))
        
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    break

operadores = ["+","-","*","/"]

while True:
    operador = input("Digite a operação [+, -, *, /]: ")
    if operador not in operadores:
        print("Precisa digitar um dos operadores!")
        continue
    
    if operador == "+":
        total = n1 + n2
        operando = "Soma"
    elif operador == "-":
        total = n1 - n2
        operando = "Subtração"
    elif operador == "*":
        total = n1 * n2
        operando = "Multiplicação"
    elif operador == "/":
        if n2 == 0:
            print("Não é possível dividir por zero!")
            continue
        total = n1 / n2
        operando = "Divisão"
        
    break
        
print(f"A {operando} de {n1} {operador} {n2} é = {total:.2f}")
                
    