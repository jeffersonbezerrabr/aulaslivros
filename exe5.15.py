#Exercício 5.15 - Página 145

#Escreva um programa para controlar uma pequena máquina registradora.
#Você deve solicitar ao usuário que digite o código do produto
#e a quantidade comprada. Utilize a tabela de códigos a seguir para
#obter o preço de cada produto:

'''
Código   preço
1        0,50
2        1,00
3        4,00
5        7,00
9        8,00
'''
#Seu programa deve exibir o total das compras depois que o usuário
#digitar 0(Zero). Qualquer outro código deve gerar a mensagem
#de erro "Código inválido."

pcod1 = 0.50
pcod2 = 1
pcod3 = 4
pcod5 = 7
pcod9 = 8

soma = 0
x = 0
qnt = 0

while True:
    c = int(input("Qual o código do produto: "))
    q = int(input("Quantidade do produto: "))
    if c == 0:
        break
    elif c == 1:
        soma += pcod1 * q
    elif c == 2:
        soma += pcod2 * q
    elif c == 3:
        soma += pcod3 * q
    elif c == 5:
        soma += pcod5 * q
    elif c == 9:
        soma += pcod9 * q
    else:
        print("Código invalido")
print(f"Valor total das compras: R${soma:5.2f}")