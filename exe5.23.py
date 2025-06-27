#Exercício 5.23 - Página 149

#Escreva um programa que leia um número e verifique se é ou não um número primo;
#Para fazer essa verificação, calcule o resto da divisão do número por 2
#e depois por todos os números ímpares até o número lido.
#Se o resto de uma dessas divisões for igual a zero, o número não é primo.
#Observe que 0 e 1 não são primos e que 2 é o unico número primo que é par.

# Programa que verifica se um número é primo (versão comentada)

# Linha 1: Solicita um número ao usuário e converte para inteiro
numero = int(input("Digite um número: "))

# Linhas 2-3: Verifica se o número é 0 ou 1 (não são primos)
if numero == 0 or numero == 1:
    print(f"{numero} não é primo")

# Linhas 4-5: Verifica se o número é 2 (único par primo)
elif numero == 2:
    print(f"{numero} é primo.")

# Linhas 6-7: Verifica se o número é par maior que 2 (não é primo)
elif numero % 2 == 0:
    print(f"{numero} não é primo, pois é par e divisível por 2")

# Linhas 8-16: Verifica números ímpares maiores que 2
elif numero > 2 and numero % 2 != 0:
    # Inicia o divisor i com 3 (primeiro ímpar após 1)
    i = 3
    
    # Loop que testa divisores ímpares até a metade do número
    while i <= numero / 2:
        # Se o número for divisível por i, não é primo
        if numero % i == 0:
            print(f"{numero} não é primo")
            break  # Sai do loop imediatamente
        i += 2  # Incrementa para o próximo ímpar (3, 5, 7...)
    
    # Else do while: executa se o loop terminar sem encontrar divisores
    else:
        print(f"{numero} é primo")
    
