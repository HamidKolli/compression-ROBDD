import time
from code.Compression import compression_bdd
from code.Tools import taille_arbre_compresse_robdd
from code.Tree import cons_arbre
from experimentations.Gnuplot import plot
from experimentations.Table import *

import sys

if len(sys.argv) != 3 : 
    nombre_var = int(input("Tapez le nombre de variables des fonctions a experimente : "))
    nombre_max_fun = int(input("Tapez le nombre de fonctions bool (-1 si toutes): "))
    tab = False
else :
    nombre_var = int(sys.argv[1])
    nombre_max_fun = int(sys.argv[2])
    tab = True


if nombre_max_fun < 0 :
    nombre_max_fun = sys.maxsize
if nombre_var <= 1:
     borne_inf = 0
else:
    borne_inf = int(2**(2**(nombre_var - 1)))

borne_sup = int(2**(2**nombre_var))

dict_taille = {}
if nombre_max_fun == sys.maxsize :
    step = 1
else :
    step = (borne_sup -borne_inf)//nombre_max_fun 
nbr_func = 0
temps = 0
for i in range(borne_inf,borne_sup,step):
    nbr_func += 1
    if nbr_func > nombre_max_fun:
        nbr_func -=1
        break
    print(f"fonction : {i} nombre_var : {nombre_var} borne inf : {borne_inf} borne sup : {borne_sup} temps : {temps}")
    arbre = cons_arbre(i)
    temps_debut = time.time()
    tree = compression_bdd(arbre)
    temps_fin = time.time()
    temps += temps_fin - temps_debut
    taille = taille_arbre_compresse_robdd(tree)    
    try:
        dict_taille[taille] = dict_taille[taille] + 1
    except KeyError :
        dict_taille[taille] = 1
    


nbr_taille_differentes = 0
with open(f"./experimentations/gnuplot_data/nombre_var{nombre_var}.dat","w") as f:
    for k in {k: v for k, v in sorted(dict_taille.items(), key=lambda item: item[0])}:
        f.write(f"{k} {dict_taille[k]}\n")
        nbr_taille_differentes += 1
plot(nombre_var)

temps_par_robdd = temps/ nbr_func

if tab :
    add_line_in_table(nombre_var ,nbr_func ,nbr_taille_differentes ,time.strftime('%H:%M:%S', time.gmtime(temps))  ,temps_par_robdd)


