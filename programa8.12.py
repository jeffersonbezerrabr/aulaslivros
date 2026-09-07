# Programa 8.12 - Página 238
# Função retângulo com parâmetros obrigatorios e opicionais

def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)
        

retangulo(3, 4)
print()
retangulo(largura= 3, altura= 4)
print()
retangulo(altura=4, largura= 3)
print()
retangulo(caractere="-", altura=4, largura= 3)
