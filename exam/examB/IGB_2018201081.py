
import proizvod

proizvodiLista = proizvod.load("proizvodi.dat")


noviProizvodi = []
for p in proizvodiLista:
    if proizvod.adekvatnost(p) < 240:
        noviProizvodi.append(p)

imeFajla = "filtriran{}.dat".format(len(noviProizvodi))
file = open(imeFajla, "w")

for p in noviProizvodi:
    file.write(proizvod.formatiran(p))

file.flush()
file.close()
