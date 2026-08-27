nomes = ["Ana", "Carlos", "Maria"]

# Podemos também gerar exceções usando a intrução raise:


try:
    i = int(input("Digite o indice que quer imprimir: "))
    print(nomes[i])
except ValueError:
    print("Digite um número")
    raise
finally:
    print("Sempre o 'finally' é executado")

# Ao utilizarmos raise, podemos tratar a exceção dentro do except e passá-la adiante novamente.

"""
No exemplo, tanto o except quanto o finally foram executados. 
A instrução raise fez com que a exceção ValueError fosse passada adiante; como não há outro bloco
try para tratá-la, o interpretador exibe o traceback com a mensagem de erro.
"""
