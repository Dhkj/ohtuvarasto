import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)







    # Konstruktorin testit
    def test_konstruktori_kasittelee_oikein_negatiivisen_tilavuuden(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_kasittelee_oikein_negatiivisen_alkusaldon(self):
        # konstruktori/alkusaldo oikein?
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_kasittelee_oikein_tilavuutta_pienemman_saldon(self):
        self.varasto = Varasto(10, 8)
        # Testaa erikseen tilavuus ja saldo?
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_konstruktori_kasittelee_oikein_liian_suuren_saldon(self):
        self.varasto = Varasto(10, 12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    # Paljonko mahtuu?

    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_sopiva_maara(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_varastoon_ylisuuri_maara(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    # Ota varastosta:

    def test_ota_varastosta_negatiivinen_maara(self)
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_varastosta_kaikki_maara(self)
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(12)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_varastosta_sopiva_maara(self)
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    # Str:

    def test_oikein__str__(self):
        # return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 0.0, vielä tilaa 10.0")





    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
