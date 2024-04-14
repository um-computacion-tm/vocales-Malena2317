import unittest
import unicodedata

from contador_vocal import contar_vocales  # type: ignore



class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})
    

    def test_contar_máquina(self):
        resultado = contar_vocales('máquina')
        self.assertEqual(resultado, {'a': 1, 'á':1, 'i':1, 'u':1 })


    def test_contar_Árbol(self):
        resultado = contar_vocales('Árbol')
        self.assertEqual(resultado, { 'á':1, 'o':1 }) 

    def test_contar_ÁRBOL(self):
        resultado = contar_vocales('ÁRBOL')
        self.assertEqual(resultado, { 'á':1, 'o':1 }) 

    def test_contar_Esdrújula(self):
        resultado = contar_vocales('Esdrújula')
        self.assertEqual(resultado, { 'a':1, 'u':1 , 'ú':1, 'e':1 }) 

    def test_contar_PAPÁ(self):
        resultado = contar_vocales('PAPÁ')
        self.assertEqual(resultado, { 'a':1, 'á':1 }) 


    



unittest.main()



