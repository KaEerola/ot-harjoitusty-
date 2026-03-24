import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteen_rahat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_myytyjen_lounaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kassapaatteen_osta_edullinen_kateisella_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kassapaatteen_osta_maukas_kateisella_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kassapaatteen_osta_edullinen_kateisella_ei_onnistu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassapaatteen_osta_maukas_kateisella_ei_onnistu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassapaatteen_osta_edullinen_kortilla_oikein(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(onnistui)
        self.assertEqual(self.kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kassapaatteen_osta_maukas_kortilla_oikein(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(onnistui)
        self.assertEqual(self.kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kassapaatteen_osta_edullinen_kortilla_ei_onnistu(self):
        self.kortti.ota_rahaa(800)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertFalse(onnistui)
        self.assertEqual(self.kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_osta_maukas_kortilla_ei_onnistu(self):
        self.kortti.ota_rahaa(800)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertFalse(onnistui)
        self.assertEqual(self.kortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassapaatteen_lataa_rahaa_kortille_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kassapaatteen_lataa_rahaa_kortille_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassapaatteen_kassassa_rahaa_euroina_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)