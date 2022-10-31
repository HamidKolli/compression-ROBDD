

from Dot import dot
from Tools import completion, decomposition, table
from Tree import cons_arbre
from Compression import compression, luka



def main ():
    print(f'>>decomposition {decomposition(38)}')
    print(f'>>completion {completion([False, True, True, False, False, True], 4)}')
    print(f'>>completion {completion([False, True, True, False, False, True], 8)}')
    print(f'>>table {table(38,8)}')

    dot(cons_arbre(38),"const_arbre")
    dot(luka(cons_arbre(38))[0],"luka_arbre")
    dot(compression(cons_arbre(38)),"compression arbre")

if __name__ == "__main__":
    main()