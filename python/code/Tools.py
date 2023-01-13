
def decomposition(number):
    l = []
    while number != 0 :
        l.append(number % 2 == 1)
        number = number // 2
    return l


def init_visited(tree):
    tree.visited = False
    if tree.false == None:
        return tree
    init_visited(tree.false)
    init_visited(tree.true)

def taille_arbre_compresse_robdd(tree) :
    init_visited(tree)
    return _taille_arbre_compresse_robdd(tree)


def _taille_arbre_compresse_robdd(tree) :
    if (tree.visited):
        return 0
    tree.visited = True
    if(tree.false == None):
        return 1
    return 1 + _taille_arbre_compresse_robdd(tree.false) + _taille_arbre_compresse_robdd(tree.true)

def completion(l,length):
    if len(l) >= length:
        return l[:length]

    while len(l) < length :
        l.append(False)
    return l


def table(x,n):
    return completion(decomposition(x),n)


def hash_luka(a,b,c,n,m):
    return a + b * m + c * m * n

class TreeException  (Exception):
    def __init__(self, s):
        super().__init__(s)




