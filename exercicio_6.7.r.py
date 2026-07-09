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
expressao = input("Digite uma expressão com parênteses: ")

for e in expressao:
    if e == "(":
        pilha.append(e)
        
    elif e == ")":
        if pilha:
            pilha.pop()
        
        else:
            pilha.append(")")
            break

if not pilha:
    print("Abertura e fechamento corretos")
else:
    print("Incorreto")