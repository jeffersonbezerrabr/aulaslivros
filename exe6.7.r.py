#Exercício 6.7 - Página 166

#Faça um programa que leia uma expressão com parênteses.
#Usando pilhas, verifique se os parênteses foram
#abertos e fechados na ordem correta. Exemplo:

#(())       OK
# ()()(()())        OK
#())            Erro

l = []
x = 0

n = input("Digite uma expressão com parênteses: ")

while x < len(n):
    if n[x] == "(":
        l.append("(")
        x += 1
    
    elif n[x] == ")":
        if len(l) > 0:
            l.pop()
            x += 1
        else:
            print("Erro: Parêntese fechado sem aberto correspondente")
            exit()
    else:
        x += 1

if len(l) == 0:
    print("OK: Parênteses balanceados corretamente!")

else:
    print("Erro: parênteses abertos sem fechamento")
    