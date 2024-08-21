import math
import unittest
import primeraLibreria as lc

class TestlibrarycMethods(unittest.TestCase):

    def test_suma(self):
        a = (3, -5)
        b = (-1, 4)
        suma = lc.sumaC(a, b)
        self.assertEqual(suma, (2, -1))

        a = (1, 4)
        b = (1, -3)
        suma2 = lc.sumaC(a, b)
        self.assertEqual(suma2, (2, 1))

    def test_resta(self):
        a = (2, -4)
        b = (5, 3)
        resta = lc.restaC(a, b)
        self.assertEqual(resta, (-3, -7))

        a = (6, 2)
        b = (1, -3)
        resta2 = lc.restaC(a, b)
        self.assertEqual(resta2, (5, 5))

    def test_multiplicacion(self):
        a = (3, -1)
        b = (1, 4)
        producto = lc.multiplicacionC(a, b)
        self.assertEqual(producto, (7, 11))

        a = (-2, 1)
        b = (3, 7)
        producto2 = lc.multiplicacionC(a, b)
        self.assertEqual(producto2, (-13, -11))

    def test_division(self):
        a = (-2, 1)
        b = (1, 2)
        division = lc.divisionC(a, b)
        self.assertAlmostEqual(division[0], 0.0)
        self.assertAlmostEqual(division[1], 1.0)

        a = (5, 10)
        b = (1, 2)
        division2 = lc.divisionC(a, b)
        self.assertAlmostEqual(division2[0], 5.0)
        self.assertAlmostEqual(division2[1], 0.0)

    def test_moduloC(self):
        a = (1, 1)
        modulo = lc.moduloC(a)
        self.assertAlmostEqual(modulo, math.sqrt(2))

        a = (3, 4)
        modulo2 = lc.moduloC(a)
        self.assertAlmostEqual(modulo2, 5)

    def test_conjugadoC(self):
        a = (-5, 4)
        conjugado = lc.conjugadoC(a)
        self.assertEqual(conjugado, (-5, -4))

        a = (6, -2)
        conjugado2 = lc.conjugadoC(a)
        self.assertEqual(conjugado2, (6, 2))

    def test_PolarToCart(self):
        a = 3.7
        b = 1.8
        polar1 = lc.PolarToCart(a, b)
        self.assertAlmostEqual(polar1[0], -0.8406477503644223)
        self.assertAlmostEqual(polar1[1], 3.603236234249322)

        a = 4.5
        b = 1.5
        polar2 = lc.PolarToCart(a, b)
        self.assertAlmostEqual(polar2[0], 0.3183174075046631)
        self.assertAlmostEqual(polar2[1], 4.488727439718245)

    def test_CartToPolar(self):
        a = (-5, 3.2)
        polar1 = lc.CartToPolar(a)
        self.assertAlmostEqual(polar1[0], 5.936328831862332)
        self.assertAlmostEqual(polar1[1], -0.5693131911006619)

        a = (3, 4)
        polar2 = lc.CartToPolar(a)
        self.assertAlmostEqual(polar2[0], 5)
        self.assertAlmostEqual(polar2[1], math.atan2(4, 3))

    def test_faseDeC(self):
        a = (1, 1)
        fase1 = lc.faseDeC(a)
        self.assertAlmostEqual(fase1, math.atan2(1, 1))

        a = (3, -2)
        fase2 = lc.faseDeC(a)
        self.assertAlmostEqual(fase2, math.atan2(-2, 3))

if __name__ == '__main__':
    unittest.main()