from code.Tree import Tree
from code.Tools import init_visited



def dot(tree : Tree,name : str):
    init_visited(tree)
    with open(f"./dot/{name}.dot","w") as f:
        f.write("graph\n")
        f.write("{\n")
        __dot(tree,1,f)
        f.write("}")

def __dot(tree:Tree,number,f):
    if tree.false == None:
        return
    if  tree.visited:
        return
    f.write(f"\"{tree.label}_{tree.id}\"[label=\"{tree.label}\"];\n\"{tree.false.label}_{tree.false.id}\"[label=\"{tree.false.label}\"];\n\"{tree.label}_{tree.id}\" -- \"{tree.false.label}_{tree.false.id}\" [color=green,penwidth=1.0]\n")
    f.write(f"\"{tree.true.label}_{tree.true.id}\"[label=\"{tree.true.label}\"];\n\"{tree.label}_{tree.id}\" -- \"{tree.true.label}_{tree.true.id}\" [color=red,penwidth=1.0]\n")
    tree.visited = True
    __dot(tree.false,number,f)
    __dot(tree.true,number,f)