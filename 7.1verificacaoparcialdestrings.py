'''
 Quando você precisa verificar se uma string começa ou termina
 com algum caracteres, pode usar os métodos starswith e endswith.
 
 Esses metodos verificam apenas os primeiros (starswith) 
 ou os ultimos (endswith) caracteres da string, retornando
 False ou True
'''

nome = "João da Silva"

print(nome.startswith("João"))
print()
print(nome.startswith("joão"))
print()
print(nome.endswith("Silva"))
