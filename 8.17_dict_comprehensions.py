# Podemos utilizar comprehensions para gerar dicionários, numa sintaxe similar à que
# utilizamos para gerar listas. Vejamos como criar um dicionário simples.

print({chave: valor * 2 for chave, valor in {"a": 1, "b": 2}.items()})

# Um dicionário invertido é útil quando queremos pesquisar pela chave ou pelo valor do dicionário principal.
# Veja que o método items gera uma tupla no formato chave, valor: {chave, valor}.
# Como no for temos for chave, valor, desempacotamos a tupla. 
# atribuindo o primeiro elemento a chave e o segundo a valor.

print({valor: chave for chave, valor in {"a": 1, "b": 2}.items()})

# Uma dict comprehensions tem os mesmos recursos de list comprehensions, como um if interno.

print({valor: chave for chave, valor in {"a": 1, "b": 2}.items() if valor % 2 == 0})

