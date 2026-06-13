# Exercício 5.22 - Página 148

# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.

menu = [1,2,3,4,5]
tabuada = 1
while True:
    print("""
====Menu====

1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair""")
    
    try:
        escolha = int(input("Digite uma das opções do menu: "))
        if escolha not in menu:
            print("Precisa escolher uma das opções exibidas no menu!")
            continue
        elif escolha == 5:
            break
        else:
            try:
                numero = int(input("Deseja ver a tabuada de qual número: "))
                if numero <= 0:
                    print("Número precisa ser positivo")
                    continue
                
                while tabuada <= 10:
                    if escolha == 1:
                        print(f"{numero} + {tabuada} = {numero + tabuada}")
                        tabuada += 1
                        
                    elif escolha == 2:
                        print(f"{numero} - {tabuada} = {numero - tabuada}")
                        tabuada += 1
                        
                    elif escolha == 3:
                        print(f"{numero} x {tabuada} = {numero * tabuada}")
                        tabuada += 1
                        
                    elif escolha == 4:
                        print(f"{numero} / {tabuada} = {numero / tabuada:.2f}")
                        tabuada += 1
                tabuada = 1
                             
            except ValueError:
                print("Precisa digitar um número inteiro!")
    
    except ValueError:
        print("Precisa digitar um valor númerico!")
        
        
# import operator

# # Mapeando os números para as funções do módulo operator
# operacoes = {
#     1: operator.add,
#     2: operator.sub,
#     3: operator.truediv,
#     4: operator.mul
# }

# # Simulando uma escolha do usuário
# escolha = 1  # O usuário escolheu 'soma'
# valor1 = 10
# valor2 = 5

# # Executando a operação baseada na escolha
# if escolha in operacoes:
#     operador_escolhido = operacoes[escolha]
#     resultado = operador_escolhido(valor1, valor2)
#     print(f"Resultado: {resultado}")
# else:
#     print("Opção inválida")
