
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

def compression_bdd(dict : dict, tree:Tree):
    return deletion_rules(dict,{},margin_rules({},terminal_rules(dict,tree)))

def terminal_rules(dict : dict, tree:Tree):
    if tree.false == None :
        return dict[tree.label]
    return makeNode(tree.label,terminal_rules(dict,tree.false),terminal_rules(dict,tree.true))
    

def margin_rules(dict:dict,tree:Tree):
    try :
        dict[tree.label]
        print(f"trouve {tree.label}\n")
        return dict[tree.label]

    except KeyError :
        if tree.false == None :
            dict[tree.label] = tree
            return tree
        print(f"pas trouve {tree.label}\n")
        dict[tree.label] = makeNode(tree.label,margin_rules(dict, tree.false),margin_rules(dict, tree.true))
        return dict[tree.label]



def deletion_rules(dict:dict,dict2 : dict,tree:Tree):
    try :
        return dict2[tree.label]
    except KeyError :
        if tree.false == None :
            return dict[tree.label]
        if tree.false == tree.true :
            if tree.false.false == None:
                return tree.false
            dict2[tree.label] = makeNode(dict[tree.false.label].label, deletion_rules(dict,dict2,tree.false.false),deletion_rules(dict,dict2,tree.false.true))
            return dict2[tree.label]
        dict2[tree.label] = makeNode(dict[tree.label].label,deletion_rules(dict,dict2,tree.false),deletion_rules(dict,dict2,tree.true))
        return dict2[tree.label]