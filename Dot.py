from Tree import Tree


def dot(tree : Tree,name : str):
    with open(f"./dot/{name}.dot","w") as f:
        f.write("digraph\n")
        f.write("{\n")
        __dot(tree,1,f)
        f.write("}")

def __dot(tree:Tree,number,f):
    number = 1
    if tree.false == None:
        return
    if  tree.write:
        return
    f.write(f"{tree.label}_{tree.id}[label=\"{tree.label}\"];\n{tree.false.label}_{tree.false.id}[label=\"{tree.false.label}\"];\n{tree.label}_{tree.id}-> {tree.false.label}_{tree.false.id} [label=\"false\"]\n")
    f.write(f"{tree.true.label}_{tree.true.id}[label=\"{tree.true.label}\"];\n{tree.label}_{tree.id} -> {tree.true.label}_{tree.true.id} [label=\"true\"]\n")
    tree.write = True
    number+=1
    __dot(tree.false,number,f)
    number+=2
    __dot(tree.true,number,f)