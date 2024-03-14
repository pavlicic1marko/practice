import math

def IndustrijskiRobot(proizvodjac, model, godina, sslk, potrosnja, sati, vp):
    if godina < 2000 or sslk < 1 or potrosnja < 1:
        return -1

    if vp not in ["hidraulicni pogon", "elektromotorni pogon", "magnetni linearni aktuator"]:
        return -1

    return{
        "proizvodjac": proizvodjac,
        "model": model,
        "godina_proizvodnje": godina,
        "broj_stepeni_slobode_kretanja": sslk,
        "potrosnja_elektricne_energije": potrosnja,
        "maksimalan_broj_radnih_sati": sati,
        "vrsta_pogona_pokretnih_delova": vp
        }

def efikasnost(ir):
    if type(ir) != dict:
        return -1

    if ir["vrsta_pogona_pokretnih_delova"] == "hidraulicni pogon":
        L = 1.33
    elif ir["vrsta_pogona_pokretnih_delova"] == "elektromotorni pogon":
        L = 2.00
    else:
        L = 1.00

    return (ir['potrosnja_elektricne_energije'] * L) / ((ir['broj_stepeni_slobode_kretanja'] - 2)* math.sqrt(ir['maksimalan_broj_radnih_sati']))

def load(imeDatoteke):
    lista = []

    dat = open(imeDatoteke,"r")

    #dokle kog ima nesto u datoteci, beskonacka while petlja
    
    while True:
        try:
            potrosnja           = float(dat.read(8).strip())
            sati                = int(dat.read(8).strip())
            godina              = int(dat.read(5).strip())
            proizvodjac         = dat.readline().strip()   #NOVI RED
            sslk                = int(dat.read(8).strip())
            vrstaPogonaAkronim  = dat.read(8).strip()
            model               = dat.readline().strip()   #NOVI RED

            if vrstaPogonaAkronim == "MLA":
                vp = "magnetni linearni aktuator"
            elif vrstaPogonaAkronim == "EMP":
                vp = "elektromotorni pogon"
            else:
                vp = "hidraulicni pogon"

            ir = IndustrijskiRobot(proizvodjac, model, godina, sslk, potrosnja, sati, vp)

            if(ir == -1):
                print("Doslo je greske prilikom unosa robota u listu!")
            else:
                lista.append(ir)
            
        except ValueError:
            break

    dat.close()

    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if efikasnost(lista[i]) > efikasnost(lista[i+1]):
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                
    return lista
