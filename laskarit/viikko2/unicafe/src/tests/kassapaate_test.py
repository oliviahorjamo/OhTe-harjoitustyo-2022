import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(500)

    def test_raha_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)

    def test_rahamaara_kasvaa_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_vaihtorahat_oikein_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)

    def test_rahamaara_kasvaa_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_vaihtorahat_oikein_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(410), 10)

    def test_lounaat_kasvaa_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_lounaat_kasvaa_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maksu_ei_riittava_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maksu_ei_riittava_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(390), 390)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)


    def test_onnistunut_korttiosto_palauttaa_true_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_onnistunut_korttiosto_palauttaa_true_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        
    
    def test_korttiosto_vahentaa_saldoa_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 260)

    def test_korttiosto_vahentaa_saldoa_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)

    def test_korttiosto_lisaa_myytyja_lounaita_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)


    def test_korttiosto_lisaa_myytyja_lounaita_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_ei_tarpeeksi_rahaa_edullinen(self):
        self.kortti.ota_rahaa(300)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_ei_tarpeeksi_rahaa_palauttaa_false_maukas(self):
        self.kortti.ota_rahaa(300)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo, 200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_lataa_rahaa_onnistuu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 600)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_lataa_rahaa_ei_onnistu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, 500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    
    