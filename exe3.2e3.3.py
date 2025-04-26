'''a = ("a")
b = ("b")

print(a!=b)'''
#Exercício 3.3

'''a = True
b = False
c = True

print("a and a:",a and a)
print("b and b:", b and b)
print("not c:", not c)
print("not b:", not b)
print("not a:", not a)
print("a and b:", a and b)
print("b and c:", b and c)
print("a or c:", a or c)
print("b or c:", b or c)
print("c or a:", c or a)
print("c or b:", c or b)
print("c or c:", c or c)
print("b or b:", b or b)'''

#Exercício 3.2.1

idade = int(input("Qual a sua idade? "))
salário = int(input("Qual o seu salário: "))

if idade >= 18 and salário >= 1000:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
    