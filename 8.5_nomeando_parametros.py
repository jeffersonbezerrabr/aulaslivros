# 8.5 Nomeando Parâmetros - Página 238

# Python também tem uma sintaxe que exige o uso do parâmetros nomeados. - Página 239

def soma(*, a, b):
    return a + b

# que ao chamarmos sem especificar o nomede cada parâmetro, resulta em erro
#print(soma(2,3))

#Forma correta por conta do *
print(soma(a=2,b=3))

# O * também pode ser posicionado no meio da lista de parâmetros, fazendo que apenas os 
# parâmetros após o asterisco sejam obrigatoriamente chamados com nome.

def retangulo(largura, altura, *, caractere="*"):
    linha = caractere * largura
    for l in range(altura):
        print(linha)

# Que pode ser chamada com:

retangulo(20, 1)

# Mas que dá erro se tentarmos chamar passando caracteres sem nomeá-lo.

# retangulo(20, 1, "-")

# veja que apenas caractere deve obrigatoriamente ser passado com nome:

retangulo(20, 1, caractere="-")

# Mas que outros parâmetros também podem ser passados por posição ou por nome:

retangulo(largura=20,  altura=1, caractere="-")

retangulo(caractere=")", largura=30, altura= 2)

retangulo(caractere=")", altura= 2, largura=30)
