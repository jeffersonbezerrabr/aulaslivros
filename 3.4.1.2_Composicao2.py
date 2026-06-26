nome = "João"
idade = 22
grana = 51.34

# print("%s tem %d anos e R$ %f no bolso" % (nome, idade, grana))
# print("%12s tem %3d anos e R$ %5.2f no bolso" % (nome, idade, grana))
# print("%12s tem %03d anos e R$ %5.2f no bolso" % (nome, idade, grana))
# print("%-12s tem %-3d anos e R$ %-5.2f no bolso" % (nome, idade, grana))

print("{} tem {} anos e R$ {} no bolso".format(nome, idade, grana))
print("{:12} tem {:3} anos e R$ {:5.2f} no bolso".format(nome, idade, grana))
print("{:12} tem {:03} anos e R$ {:5.2f} no bolso".format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R$ {:5.2f} no bolso".format(nome, idade, grana))