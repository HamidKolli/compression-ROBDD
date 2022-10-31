
from Tree import Tree,makeNode,makeLeaf


def luka (tree: Tree) :
    dict = {}
    tree = __luka(tree,dict)
    return (tree,dict)

def __luka(tree: Tree,dict:dict) -> Tree:
      #If tree.false == None also tree.true == None
    if tree.false == None :
        leaf = makeLeaf(tree.label)
        dict[tree.label] = tree
        return leaf
    labelFalse = __luka(tree.false,dict)
    labelTrue = __luka(tree.true,dict)
    node = makeNode(f"({labelFalse.label}) ({labelTrue.label}){tree.label}",labelFalse,labelTrue)
    dict[node.label] = tree
    return node

def compression(tree: Tree) -> Tree :
    (treeLuka,dict) = luka (tree)
    return __compression(treeLuka,dict)


def __compression(tree: Tree,dict:dict) -> Tree :
    if tree.false == None :
        return dict[tree.label]
    t = dict[tree.label]
    t.false = __compression(tree.false,dict)
    t.true = __compression(tree.true,dict)
    return t
