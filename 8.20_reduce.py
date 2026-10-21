from functools import reduce
import operator

print(reduce(min,[2,1,9,4]))

print(reduce(max,[1, 0, 9, 4]))

print(reduce(operator.add, [1,2,3]))


# Veja que ambos os exemplos poderiam ter sido implementados com as funções min e max diretamente:

print(max(*[2, 1, 9, 4]))

# 9 

print(min(*[2, 1, 9, 4]))

# 1

print(max(2, 1, 9, 4))

# 9

print(min(2, 1, 9, 4))

# 1

# Para somar os elementos de uma lista:

print(sum([2, 1, 9, 4]))

# 16

# Outra forma de chamar reduce é passando o elemento inicial como terceiro parâmetro:

print(reduce(lambda a,b: a + 1 if b % 2 == 0 else a, [2, 9, 4, 10, 5], 0))

# Uma observação importante: para esse tipo de contagem, muitas pessoas consideram 
# uma solução com sum mais legível do que reduce:

print(sum(1 for n in [2, 9, 4, 10, 5] if n % 2 == 0))

# Ela produz o mesmo resultado (3), mas costuma ser mais fácil de entender.
