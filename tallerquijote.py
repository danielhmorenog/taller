import re
import matplotlib.pyplot as plt
import numpy as np
cadena = (open("D:/UNIVERSIDAD/UCEVA/2020-1/inteligencia/DonQuijote.txt",mode="r",encoding="utf-8")).read()
print(cadena)
print()
wait = input("PRESS ENTER TO CONTINUE.")
saltos=re.findall("\n",cadena) #profe porque si es windwos se usa solo \n
print()
print("Los saltos de linea son:", len(saltos))
print()
wait = input("PRESS ENTER TO CONTINUE.")
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print()
print("***Conteo de las palabras***")
print()
for k, v in word_count(cadena).items():
    print("Palabra: '{0}' con {1} repeticiones".format(k, v))
print()
wait = input("PRESS ENTER TO CONTINUE.")
print()
print("***5 palabras mas repetidas***")
print()
ordenada=sorted(word_count(cadena).items(),key = lambda x : x[1], reverse=True)
for k, v in ordenada[0:5]:
    print("Palabra: '{0}' con {1} repeticiones".format(k, v))
print()
wait = input("PRESS ENTER TO CONTINUE.")
print()
a = np.array(ordenada[0:5])
plt.bar(np.flip(a[:,0]),np.flip(a[:,1]))
plt.show()