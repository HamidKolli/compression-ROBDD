

from code.Dot import dot
from code.Tools import completion, decomposition, table
from code.Tree import cons_arbre
from code.Compression import compression, compression_bdd, luka



def main ():
    print(f'>>decomposition {decomposition(38)}')
    print(f'>>completion {completion([False, True, True, False, False, True], 4)}')
    print(f'>>completion {completion([False, True, True, False, False, True], 8)}')
    print(f'>>table {table(38,8)}')
    (tree,d) = luka(cons_arbre(38))
    dot(cons_arbre(38),"const_arbre")
    dot(tree,"luka_arbre")
    dot(compression(cons_arbre(38)),"compression arbre")
    terminal_tree = compression_bdd(d,tree)
    dot(terminal_tree,"compression_bdd")

if __name__ == "__main__":
    main()