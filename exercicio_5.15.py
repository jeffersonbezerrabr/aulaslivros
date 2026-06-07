# Exercício 5.15 - Página 145

# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto:

"""
Código Preço
1      0,50
2      1,00 
3      4,00
5      7,00
9      8,00
"""

codigos = {1:0.50, 2:1.00, 3:4.00, 5:7.00, 9:8.00}
total = 0
while True:
    try:
        codigo = int(input("Digite o código do produto ou 0(zero) para finalizar: "))
        if codigo == 0:
            break
        
        if codigo not in codigos:
            print("Precisa digitar um dos códigos [1, 2, 3, 5, 9]")
            continue
        
        while True:
            try:
                qntd = int(input(f"Quantidade do produto de código {codigo}: "))
                if qntd > 0:
                    break
                
                else:
                    print("Digite uma quantidade positiva.")
                    
            except ValueError:
                print("Digite um número inteiro válido.")

        total += codigos[codigo] * qntd
            
    except ValueError:
        print("Precisa digitar um valor númerico")
        
if total > 0:
    print(f"O total de compras foi: R$ {total:.2f}")

else:
    print("Não comprou nada!")
            