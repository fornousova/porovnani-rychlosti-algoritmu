from binarni_vyhledavani import binarni_vyhledavani
from trivialni_algoritmus import hledani_cisla
import time
import random

opakovani = 1000
pole = list(range(1, 100000))
test = [random.randint(1, 100000) for i in range(opakovani)]

start = time.time()
for i in range(opakovani):
    hledani_cisla(pole,test[i])
end = time.time()

print(end-start)

start = time.time()
for i in range(opakovani):
    binarni_vyhledavani(pole, test[i])
end = time.time()


print(end-start)