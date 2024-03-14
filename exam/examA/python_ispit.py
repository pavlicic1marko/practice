import json
import industrijski_robot

print("Milos Mravik, 2014200501, 21.10.2020.")

lista = industrijski_robot.load("ulaz.dat")

suma = 0

for ir in lista:
    suma += industrijski_robot.efikasnost(ir)

srVr = suma / len(lista)

lista2 = []

for ir in lista:
    if industrijski_robot.efikasnost(ir) >= 0.5 * srVr and industrijski_robot.efikasnost(ir) <= 1.5 * srVr:
        lista2.append(ir)
        print(industrijski_robot.efikasnost(ir))

#print(lista2)

imeDatoteke = "lista_{0:d}_{1:d}.json".format(len(lista),len(lista2))

dat = open(imeDatoteke, "w")

json.dump(lista2, dat)

dat.close()
