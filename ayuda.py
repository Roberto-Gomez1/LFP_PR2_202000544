import csv
from Obj import Obj


def lectura():
    aux = []
    with open('LaLigaBot-LFP.csv') as a:
        reader = csv.reader(a)
        for aa in reader:
            aux.append(Obj(aa[0],aa[1],aa[2],aa[3],aa[4],aa[5],aa[6]))
    return aux