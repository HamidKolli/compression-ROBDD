import unittest
from code.Compression import compression_bdd
from code.Tools import *
from code.Tree import cons_arbre

class Tools_test(unittest.TestCase):
    def test_decomposition(self):
        self.assertEqual(decomposition(38),[False, True, True, False, False, True])
        self.assertEqual(decomposition(12),[False, False, True, True])
        self.assertEqual(decomposition(128),[False, False, False, False, False, False, False, True])

    def test_completion(self):
        self.assertEqual(completion(decomposition(38),2),[False, True])
        self.assertEqual(completion(decomposition(38),6),[False, True, True, False, False, True])
        self.assertEqual(completion(decomposition(38),13),[False, True, True, False, False, True, False, False, False, False, False, False, False])

        
    def test_table(self):
        self.assertEqual(table(38,2),[False, True])
        self.assertEqual(table(38,6),[False, True, True, False, False, True])
        self.assertEqual(table(38,13),[False, True, True, False, False, True, False, False, False, False, False, False, False])

    def test_taille_compression_robdd(self):
        self.assertEqual(taille_arbre_compresse_robdd(compression_bdd(cons_arbre(38))),7)



if __name__ == '__main__':
    unittest.main()