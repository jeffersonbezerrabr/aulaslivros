# Um padrão de código é gerar uma lista com o resultado de uma função aplicada a outra lista;
# Ao utilizarmos a função map, a função a ser aplicada é passada no primeiro parâmetro
# e a lista ou iterável a aplicá-la em seguida. 
# A função map retorna uma lista com o resultado de cada chamada individual.
# Vejamos como isso funcionaria se tivéssemos de implementar map em Python;
# Vamos chamar a nossa implementação de map_1:

def map_1(funcao, valores):
    retorno = []
    for v in valores:
        retorno.append(funcao(v))
        
    return retorno

print(map_1(lambda x: x/2, [1,2,3]))

# O mesmo resultado teriamos chamando a função map do Python:

print(map(lambda x: x/2, [1, 2, 3]))

# Exceto que map retorna um iterador que gera os valores um a um. Podemos então
# usar list para ter uma lista como em nossa função map_1

print(list(map(lambda x: x/2, [1, 2, 3])))

# Porém, map é capaz de combinar várias listas, passando um elemento de cada para a função.
# Vejamos um exemplo para somar os elementos de duas listas:

print(list(map(lambda a, b: a + b, [1, 2, 3], [4, 5, 6])))

# Veja que map chamou a função lambda com dois parâmetros, um de cada lista, 
# resultando em, [1 + 4, 2 + 5, 3 + 6] ou [5, 6, 7].
# Para ficar mais claro, vamos modificar o exemplo para retornar uma tupla com os parâmetros:

print(list(map(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6])))

# Essa característica de map é muito interessante e Python tem outra função que
# nos permite combinar duas ou mais listas, uma a uma: zip.

print(zip([1, 2, 3], [4, 5, 6]))

# Que retorna um iterador, assim como map. Vamos expandi-loi com list:

print(list(zip([1, 2, 3], [4, 5, 6])))

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

soma = [a + b for a, b in zip(lista1, lista2)]
print(soma)  # Resultado: [5, 7, 9]

# Tanto map quanto zip combinam várias listas, elemento a elemento, até que uma
# das listas não tenha mais elementos. Se a lista têm tamanhos diferentes,
# o resultado é a combinação dos elementos com o tamanho da lista menor.

print(list(zip([1, 2], [4, 5, 6])))

# Vejamos agora como implementar nossa função map_2, usando zip
# para ser mais parecida com map do Python:

def map_2(funcao, *valores):
    retorno = []
    for v in zip(*valores):
        retorno.append(funcao(*v))
    
    return retorno

print(map_2(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6]))
