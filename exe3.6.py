#exercício 3.6 do livro - pag 100
import time
media=7
reprovado=3

print("Vamos analisar as notas do aluno e verificar se ele passou.")
time.sleep(1)
print("Português:")
time.sleep(1)

primeiro_bimestre_p = int(input("Informe a nota do primeiro bimestre: "))
time.sleep(0.2)
segundo_bimestre_p = int(input("Informe a nota do segundo bimestre: "))
time.sleep(0.2)
terceiro_bimestre_p = int(input("Informe a nota do terceiro bimestre: "))
time.sleep(0.2)
quarto_bimestre_p = int(input("Informe a nota do quarto bimestre: "))
time.sleep(0.2)
media_notas_p=((primeiro_bimestre_p + segundo_bimestre_p + terceiro_bimestre_p + quarto_bimestre_p) / 4)

if media_notas_p >= media:
    print(f"Sua média foi: {media_notas_p} em português. Parabéns, você está aprovado!")
elif media_notas_p > reprovado and media_notas_p < media:
    print(f"Sua média foi: {media_notas_p} em português. Você ficou em recuperação!")
else:
    print(f"Sua média foi: {media_notas_p} em português. Infelizmente você não passou!")
    
print("Matemática:")
time.sleep(1)
primeiro_bimestre_m = int(input("Informe a nota do primeiro bimeste: "))
time.sleep(0.2)
segundo_bimestre_m = int(input("Informe a nota do segundo bimestre: "))
time.sleep(0.2)
terceiro_bimestre_m = int(input("Informe a nota do terceiro bimestre: "))
time.sleep(0.2)
quarto_bimestre_m = int(input("Informe a nota do quarto bimestre: "))
media_notas_m = ((primeiro_bimestre_m + segundo_bimestre_m + terceiro_bimestre_m + quarto_bimestre_m) / 4)

if media_notas_m >= media:
    print(f"Sua média foi: {media_notas_m} em matemática. Parabéns, você está aprovado!")
elif media_notas_m > reprovado and media_notas_m < media:
    print(f"Sua média foi: {media_notas_m} em matemática. Você ficou em recuperação!")
else:
    print(f"Sua média foi: {media_notas_m} em matemática. Infelizmente você não passou!")

print("Geografia:")
time.sleep(1)

primeiro_bimestre_g = int(input("Informe a nota do promeiro bimestre: "))
time.sleep(0.2)
segundo_bimestre_g = int(input("Informe a nota do segundo bimestre: "))
time.sleep(0.2)
terceiro_bimestre_g = int(input("Informe a nota do terceiro bimestre: "))
time.sleep(0.2)
quarto_bimestre_g = int(input("Informe a nota do quarto bimestre: "))
time.sleep(0.2)
media_notas_g = ((primeiro_bimestre_g + segundo_bimestre_g + terceiro_bimestre_g + quarto_bimestre_g) / 4)
time.sleep(0.2)

if media_notas_g >= media:
    print(f"Sua média foi: {media_notas_g} em geografia. Parabéns, você está aprovado!")
elif media_notas_g > reprovado and media_notas_g < media:
    print(f"Sua média foi: {media_notas_g} em geografia. Você ficou em recuperação!")
else:
    print(f"Sua média foi: {media_notas_g} em geografia. Infelizmente você não passou!")

print("Historia:")
time.sleep(1)

primeiro_bimestre_h = int(input("Informe a nota do primeiro bimestre: "))
time.sleep(0.2)
segundo_bimestre_h = int(input("Informe a nota do segundo bimestre: "))
time.sleep(0.2)
terceiro_bimestre_h = int(input("Informe a nota do terceiro bimestre: "))
time.sleep(0.2)
quarto_bimestre_h = int(input("Informe a nota do quarto bimestre: "))
time.sleep(0.2)
media_notas_h = ((primeiro_bimestre_h + segundo_bimestre_h + terceiro_bimestre_h + quarto_bimestre_h) / 4)

if media_notas_h >= media:
    print(f"Sua média foi: {media_notas_h} em historia. Parabéns, você está aprovado!")
elif media_notas_h > reprovado and media_notas_h < media:
    print(f"Sua média foi: {media_notas_h} em historia. Você ficou em recuperação!")
else:
    print(f"Sua média foi: {media_notas_h} em historia. Infelizmente você não passou!")
    

'''if media_notas_p >= media and media_notas_m >= media and media_nota_g >= media and media_nota_h >= media:
    print("Parabéns você foi aprovado!")
    print("Português: ", media_notas_p)
    print("Matemática: ", media_notas_m)
    print("Geografia: ", media_nota_g)
    print("História: ", media_nota_h)
elif media_notas_p == recuperacao and media_notas_m == recuperacao and media_nota_g == recuperacao and media_nota_h == recuperacao:
    print("Você ficou em recuperação!")
    print("Português: ", media_notas_p)
    print("Matemática: ", media_notas_m)
    print("Geografia: ", media_nota_g)
    print("História: ", media_nota_h)
else:
    print("Você está reprovado!")
    print("Português: ", media_notas_p)
    print("Matemática: ", media_notas_m)
    print("Geografia: ", media_nota_g)
    print("História: ", media_nota_h)'''
