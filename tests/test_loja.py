import unittest

from loja import total


class TotalCase(unittest.TestCase):
    def test_CA_1_soma_os_precos(self):
        self.assertEqual(total([1, 2]), 3)


class DescontoCase(unittest.TestCase):
    def test_CA_2_desconto_fora_de_0_a_100_e_recusado(self):
        for desconto in (-10, 150):
            with self.subTest(desconto):
                with self.assertRaises(ValueError):
                    total([10], desconto=desconto)

    def test_CA_2_os_limites_valem(self):
        self.assertEqual(total([10], desconto=0), 10)
        self.assertEqual(total([10], desconto=100), 0)
