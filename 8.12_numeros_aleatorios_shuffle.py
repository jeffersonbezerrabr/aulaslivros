# Shuffle - Página 254

# Se quisermos embaralhar os elementos de uma lista, podemos utilizat a função shuffle.
# Ela recebe a lista a embaralhar, alterando-a:

import random

a = list(range(1,11))
print(a)

random.shuffle(a)

print(a)