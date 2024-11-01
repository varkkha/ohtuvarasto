import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

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
        
    def test_lisays_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)  
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)  
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        
    def test_ottaminen_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)  
        self.assertAlmostEqual(saatu_maara, 0)  
        
    def test_ottaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)  
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0) 
    
    def test_konstruktori_nollatilavuus(self):
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)  
        self.assertAlmostEqual(varasto.saldo, 0.0)    

    def test_konstruktori_negatiivinen_tilavuus(self):
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)  
        self.assertAlmostEqual(varasto.saldo, 0.0)     

    def test_konstruktori_saldo_yhtaa_tilavuuden(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, varasto.tilavuus) 
        
    def test_konstruktori_negatiivinen_saldo(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0.0)
        
    def test_str_metodi(self):
        self.varasto.lisaa_varastoon(5)
        expected_str = f"saldo = 5.0, vielä tilaa 5.0"
        self.assertEqual(str(self.varasto), expected_str) 
