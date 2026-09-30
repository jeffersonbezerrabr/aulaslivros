# Programa 8.16: Função imprime_maior com número indeterminado de parâmetros - Página 243

def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)
        
imprime_maior("Maior:", 4,3,15,5)
imprime_maior("Max:", *[1, 7, 9])
imprime_maior("Max:")
