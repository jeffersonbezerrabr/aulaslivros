#Exercício 4.14 - Página 131

#Reescreva o programa a seguir com if elif e else.
#Adicione as linhas necessárias para faze-lo funcionar em Python.

a = int(input("informe um número: "))

if a < 10:
    print("a é menor que 10")
    
elif a >= 10 and a < 20:
    print("a é maior que 10 e menor que 20")
    
else:
    print("a é maior que 20")
