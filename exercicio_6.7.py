# Exercício 6.7 - Página 166

# Faça um programa que leia uma expressão com parentêses.
# Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
# Exemplo:
"""
(())    OK
()()(()())  OK
() )    Erro
"""

pilha = []
x = 0
n = input("Digite uma expressão com parênteses: ")

while x < len(n):
    if n[x] == "(":
        pilha.append(n[x])
    
        
    elif n[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    
    x += 1
        
if not pilha:
    print("Abertura e fechamento corretos")

else:
    print("Incorreto")