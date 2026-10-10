import unittest

from loja import total


class TotalCase(unittest.TestCase):
    def test_CA_1_soma_os_precos(self):
        self.assertEqual(total([1, 2]), 3)
