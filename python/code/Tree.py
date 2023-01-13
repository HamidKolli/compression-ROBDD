
from code.Tools import TreeException, table

from math import log2 as log


ident = 1
class Tree:
    def __init__(self,label):
        global ident
        self.label = label
        self.false = None
        self.true = None
        self.taille = 0
        self.hauteur = 0
        self.visited = False
        self.id = ident
        ident+=1
    def __repr__(self) -> str:
        return f"{self.label}"

    



    

    


def makeLeaf(label : bool) -> Tree:
    return Tree(label)


def makeNode(label : str, treeF : Tree, treeT : Tree) -> Tree :
    if treeF == None or treeT  == None :
        raise TreeException("Node must have exactly two children")
    tree = Tree(label)
    tree.false = treeF
    tree.true = treeT
    return tree

def cons_arbre(number : int) -> Tree :
    log2nInt = 2
    if number != 0 :
        log2n = log(number) 
        log2nInt = int(log2n) + 1
        
        if log2n >  log2nInt:
            log2nInt +=1
    
        while log(log2nInt) > int(log(log2nInt)):
            log2nInt +=1
    if log2nInt < 2:
        log2nInt = 2
    t = table(number,log2nInt)
    
    tree =  __cons_arbre(int(log(log2nInt)),t[:len(t)//2],t[len(t)//2:])
    tree.taille = len(t) * 2 -1
    tree.hauteur = int(len(t))
    return tree


def __cons_arbre(number:int,arrayLeft : list, arrayRight: list) -> Tree:
    #  len(arrayLeft) = len(arrayRight) because len(arrayLeft)+len(arrayRight) is a power of 2 
    if len(arrayLeft) == 0  and  len(arrayRight) == 1 :
        return makeLeaf(arrayRight[0])
    if len(arrayLeft) == 1  and  len(arrayRight) == 0 :
        return makeLeaf(arrayLeft[0])
    if len(arrayLeft) == 1 :
        return makeNode(f"x_{number}",makeLeaf(arrayLeft[0]),makeLeaf(arrayRight[0]))
    return makeNode(f"x_{number}",
                                __cons_arbre(number-1,arrayLeft[:len(arrayLeft)//2],arrayLeft[len(arrayLeft)//2:]),
                                        __cons_arbre(number-1,arrayRight[:len(arrayRight)//2],arrayRight[len(arrayRight)//2:]))








    



    


