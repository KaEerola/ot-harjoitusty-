import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortti_latautuu_oikein(self):
        self.maksukortti.lataa_rahaa(250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.50 euroa")
    
    def test_kortti_ota_rahaa_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_kortti_ota_rahaa_ei_onnistu(self):
        self.maksukortti.ota_rahaa(1250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_true_kun_onnistuu(self):
        tulos = self.maksukortti.ota_rahaa(300)
        self.assertTrue(tulos)

    def test_ota_rahaa_palauttaa_false_kun_ei_onnistu(self):
        tulos = self.maksukortti.ota_rahaa(1250)
        self.assertFalse(tulos)

    def test_saldo_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)