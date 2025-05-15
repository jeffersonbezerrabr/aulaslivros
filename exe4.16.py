#Exercício 4.16 - Página 132

#Corrija o programa a seguir:

#media = input("Digite sua média: ")

#if media < 4:
#    print("Infelizmente você reprovou")
    
#if media < 7:
#    print("Você ficou em recuperação")
    
#if media > 7:
#    print("Você passou de ano")

media = float(input("Digite sua média: "))

if media < 4:
    print("Infelizmente você ficou em recuperação")
    
elif media >= 4 and media < 7:
    print("Você ficou em recuperação")
    
else:
    print("Você passou de ano")
    