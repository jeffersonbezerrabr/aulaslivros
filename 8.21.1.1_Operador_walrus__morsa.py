# Também podemos utilizar o Walrus em expressões com if:

a = "TeXtO"

a = n.lower() if (n := a.strip()) else "-"

print(a)

# E podemos usar o Walrus com f-strings, mas sempre escrevendo-o entre parênteses:

a = [1, 2, 3]

print(f"{a=} tem {(tamanho := len(a))} elementos que somam {(soma := sum(a))} e tem média {soma / tamanho}")