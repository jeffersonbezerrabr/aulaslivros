# Programa 8.12: Função retângulo com parâmetros obrigatórios e opcionais. - Página 238

def retangulo(largura, altura, caractere = "*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)
        
retangulo(3, 4)

retangulo(largura = 3, altura = 4)

retangulo(altura = 4, largura=3)

retangulo(caractere="-", altura=4, largura=3)
