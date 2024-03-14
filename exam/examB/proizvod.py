import math

# nazivu,proizvođaču, godini proizvodnje, masi i materijalu od kojeg je proizvod napravljen .

def Proizvod(naziv, proizvodjac, godina, masa, materijal):

    validniMaterijali = ["DRVO", "PLASTIKA", "METAL", "DRUGI_MATERIJAL"]
    if materijal not in validniMaterijali:
        return False

    if masa < 0.01:
        return False

    return {
        'naziv' : naziv,
        'proizvodjac' : proizvodjac,
        'godina' : godina,
        'masa' : masa,
        'materijal' : materijal,
    }


def jeValidan(p): # p - recnik proizvoda
    if type(p) != dict:
        return False

    validniKljucevi = ['naziv', 'proizvodjac', 'godina', 'masa','materijal']
    for kljuc in p.keys():
        if kljuc not in validniKljucevi:
            return False

    return True


def adekvatnost(p): # p - je recnik proizvoda

    k = 0

    if p['materijal'] == "DRVO":
        k = 0.98
    elif p['materijal'] == "PLASTIKA":
        k = 0.93
    elif p['materijal'] == "METAL":
        k = 0.21
    else:
        #DRUGI_MATERIJAL
        k = 2.12
    
    a = ( (2050 - p['godina']) * math.sqrt(p['masa']) ) / (1 - k)

    return a



# Greska u ispisivanju vrednosti je bila zbog prisustva karaktera čćđ tako dalje
def formatiran(p):
    if not jeValidan:
        return False

    red1 = "{0:<12}{1:20s}{2:<13}{3:13.3f} kg\n".format("Naziv:", p['naziv'], "Masa:", p['masa'])
    red2 = "{0:<12}{1:<20s}{2:<13}{3:8d}. godina\n".format("Proizvodac:", p['proizvodjac'], "Proizvedeno:", p['godina'])

    materijal2 = "";
    if p['materijal'] == "DRVO":
        materijal2 = "drvo"
    elif p['materijal'] == "PLASTIKA":
        materijal2 = "plastika"
    elif p['materijal'] == "METAL":
        materijal2 = "metal"
    else:
        materijal2 = "drugi materijal"
    
    red3 = "{0:<12}{1:<20s}{2:<13}{3:16.3f}\n".format("Materijal:", materijal2, "Adekvatnost:", adekvatnost(p))

    return red1 + red2 + red3


def load(imeDatoteke):

    proizvodi = []
    file = open(imeDatoteke, "r")

    while True:
        try:
            naziv = file.readline().strip()
            proizvodjac = file.readline().strip()
            godina = int(file.read(5).strip())
            masa = int(file.read(3).strip()) / 1000 # Pretvaramo masu iz g u KG
            materijalAkronim = file.readline().strip()

            materijal = "";
            if materijalAkronim == "D":
                materijal = "DRVO"
            elif materijalAkronim == "P":
                materijal = "PLASTIKA"
            elif materijalAkronim == "M":
                materijal = "METAL"
            else:
                materijal = "DRUGI_MATERIJAL"

            proizvod = Proizvod(naziv, proizvodjac, godina, masa, materijal)
            proizvodi.append(proizvod)
            
        except:
            break
    

    file.close()
    return proizvodi
    
    





