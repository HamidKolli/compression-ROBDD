import unittest
from code.Tree import *
class Tree_test(unittest.TestCase):
    def test_makeLeaf(self):
        leaf = makeLeaf(True)
        self.assertEqual(leaf.label,True)
        self.assertEqual(leaf.false,None)
        self.assertEqual(leaf.true,None)

    def test_makeNode(self):
        leaf = makeLeaf(True)
        leaf2 = makeLeaf(False)
        node = makeNode("x",leaf,leaf2)
        self.assertEqual(node.label,"x")
        self.assertEqual(node.false,leaf)
        self.assertEqual(node.true,leaf2)
    
    def test_makeNode_exception(self):
        try :
            makeNode("",None,None)
            self.assertTrue(False)
        except TreeException:
            self.assertTrue(True)


    def test_cons_arbre(self):
        tree = cons_arbre(38)
        self.assertEqual(tree.label, "x_3")

        self.assertEqual(tree.false.label, "x_2")
        self.assertEqual(tree.true.label, "x_2")

        self.assertEqual(tree.false.false.label, "x_1")
        self.assertEqual(tree.false.true.label, "x_1")
        self.assertEqual(tree.true.false.label, "x_1")
        self.assertEqual(tree.true.true.label, "x_1")

        self.assertEqual(tree.false.false.false.label, False)
        self.assertEqual(tree.false.false.true.label, True)
        self.assertEqual(tree.false.true.false.label, True)
        self.assertEqual(tree.false.true.true.label, False)
        self.assertEqual(tree.true.false.false.label, False)
        self.assertEqual(tree.true.false.true.label, True)
        self.assertEqual(tree.true.true.false.label, False)
        self.assertEqual(tree.true.true.true.label, False)




if __name__ == '__main__':
    unittest.main()