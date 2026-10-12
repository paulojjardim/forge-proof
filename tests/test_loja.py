"""Os critérios da análise #11 — os portes nas compras abaixo de 50 €."""

import unittest

from loja import total


class PortesCase(unittest.TestCase):
    def test_CA_1_abaixo_de_50_o_total_inclui_os_portes(self):
        self.assertEqual(total([10, 20]), 33.5)
        self.assertEqual(total([49.99]), 53.49)

    def test_CA_2_a_partir_de_50_nao_ha_portes(self):
        self.assertEqual(total([50]), 50)
        self.assertEqual(total([30, 40]), 70)

    def test_CA_2_o_limite_conta_antes_do_desconto(self):
        # 60 € com 50 % de desconto fica em 30 €, e continua sem portes.
        self.assertEqual(total([60], desconto=50), 30)


class DescontoCase(unittest.TestCase):
    def test_CA_3_desconto_fora_de_0_a_100_e_recusado(self):
        for desconto in (-10, 150):
            with self.subTest(desconto):
                with self.assertRaises(ValueError):
                    total([10], desconto=desconto)

    def test_CA_3_os_limites_valem(self):
        self.assertEqual(total([60], desconto=0), 60)
        self.assertEqual(total([60], desconto=100), 0)

    def test_CA_4_o_desconto_aplica_se_ao_total_com_portes(self):
        self.assertEqual(total([40], desconto=10), 39.15)


class CarrinhoVazioCase(unittest.TestCase):
    def test_um_carrinho_vazio_custa_zero(self):
        self.assertEqual(total([]), 0)
