
from Tools import TreeException, table

from math import log2 as log


ident = 1
class Tree:
    def __init__(self,label):
        global ident
        self.label = label
        self.false = None
        self.true = None
        self.write = False
        self.id = ident
        ident+=1

   


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
    log2n = log(number)
    log2nInt = int(log2n)
    
    if log2n >  log2nInt:
        log2nInt +=1
   
    while log(log2nInt) > int(log(log2nInt)):
        log2nInt +=1

    t = table(number,log2nInt)
    return __cons_arbre(int(log(log2nInt)),t[:len(t)//2],t[len(t)//2:])


def __cons_arbre(number:int,arrayLeft : list, arrayRight: list) -> Tree:
        #  len(arrayLeft) = len(arrayRight) because len(arrayLeft)+len(arrayRight) is a power of 2 
        if len(arrayLeft) == 1 :
            return makeNode(f"x_{number}",makeLeaf(arrayLeft[0]),makeLeaf(arrayRight[0]))
        return makeNode(f"x_{number}",
                                    __cons_arbre(number-1,arrayLeft[:len(arrayLeft)//2],arrayLeft[len(arrayLeft)//2:]),
                                         __cons_arbre(number-1,arrayRight[:len(arrayRight)//2],arrayRight[len(arrayRight)//2:]))
   
   






    



    


