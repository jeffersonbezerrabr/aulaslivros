#Exercício 6.7 - Página 166

#Faça um programa que leia uma expressão com parênteses.
#Usando pilhas, verifique se os parênteses foram
#abertos e fechados na ordem correta. Exemplo:

#(())       OK
# ()()(()())        OK
#())            Erro

P = []
x = 0

expressao = str(input("Digite uma expressão com parênteses: "))

while x < len(expressao):
    if expressao[x] == "(":
        P.append("(")
        x += 1
    elif expressao[x] == ")":
        if len(P) > 0:
            P.pop()
            x += 1
        else:
            print("Erro: Parêntese fechado sem aberto correspondente")
            exit()
    else:
        x += 1
if len(P) == 0:
    print("OK: Parênteses balanceados corretamente!")
else:
    print("Erro: parênteses abertos sem fechamento")
        
    