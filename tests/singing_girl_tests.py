#! -*- coding: utf8 -*-
from __future__ import unicode_literals

import unittest
import singing_girl
from decimal import Decimal

class TestTraductorNumeros(unittest.TestCase):
    def setUp(self):
        self.trad = singing_girl.Singer()

    def test_digitos(self):
        self.assertEquals(self.trad.sing(0), 'cero')
        self.assertEquals(self.trad.sing(1), 'uno')
        self.assertEquals(self.trad.sing(2), 'dos')
        self.assertEquals(self.trad.sing(3), 'tres')
        self.assertEquals(self.trad.sing(4), 'cuatro')
        self.assertEquals(self.trad.sing(5), 'cinco')
        self.assertEquals(self.trad.sing(6), 'seis')
        self.assertEquals(self.trad.sing(7), 'siete')
        self.assertEquals(self.trad.sing(8), 'ocho')
        self.assertEquals(self.trad.sing(9), 'nueve')

    def test_decenas(self):
        self.assertEquals(self.trad.sing(10), 'diez')
        self.assertEquals(self.trad.sing(11), 'once')
        self.assertEquals(self.trad.sing(12), 'doce')
        self.assertEquals(self.trad.sing(13), 'trece')
        self.assertEquals(self.trad.sing(14), 'catorce')
        self.assertEquals(self.trad.sing(15), 'quince')
        self.assertEquals(self.trad.sing(16), 'dieciseis')
        self.assertEquals(self.trad.sing(17), 'diecisiete')
        self.assertEquals(self.trad.sing(18), 'dieciocho')
        self.assertEquals(self.trad.sing(19), 'diecinueve')
        self.assertEquals(self.trad.sing(20), 'veinte')
        self.assertEquals(self.trad.sing(21), 'veintiuno')
        self.assertEquals(self.trad.sing(22), 'veintidós')
        self.assertEquals(self.trad.sing(23), 'veintitrés')
        self.assertEquals(self.trad.sing(24), 'veinticuatro')
        self.assertEquals(self.trad.sing(25), 'veinticinco')
        self.assertEquals(self.trad.sing(26), 'veintiseis')
        self.assertEquals(self.trad.sing(27), 'veintisiete')
        self.assertEquals(self.trad.sing(28), 'veintiocho')
        self.assertEquals(self.trad.sing(29), 'veintinueve')
        self.assertEquals(self.trad.sing(30), 'treinta')
        self.assertEquals(self.trad.sing(37), 'treinta y siete')
        self.assertEquals(self.trad.sing(40), 'cuarenta')
        self.assertEquals(self.trad.sing(42), 'cuarenta y dos')
        self.assertEquals(self.trad.sing(50), 'cincuenta')
        self.assertEquals(self.trad.sing(55), 'cincuenta y cinco')
        self.assertEquals(self.trad.sing(60), 'sesenta')
        self.assertEquals(self.trad.sing(66), 'sesenta y seis')
        self.assertEquals(self.trad.sing(70), 'setenta')
        self.assertEquals(self.trad.sing(77), 'setenta y siete')
        self.assertEquals(self.trad.sing(80), 'ochenta')
        self.assertEquals(self.trad.sing(88), 'ochenta y ocho')
        self.assertEquals(self.trad.sing(90), 'noventa')
        self.assertEquals(self.trad.sing(99), 'noventa y nueve')

    def test_centenas(self):
        self.assertEquals(self.trad.sing(100), 'cien')
        self.assertEquals(self.trad.sing(111), 'ciento once')
        self.assertEquals(self.trad.sing(200), 'doscientos')
        self.assertEquals(self.trad.sing(222), 'doscientos veintidos')
        self.assertEquals(self.trad.sing(300), 'trescientos')
        self.assertEquals(self.trad.sing(333), 'trescientos treinta y tres')
        self.assertEquals(self.trad.sing(400), 'cuatrocientos')
        self.assertEquals(self.trad.sing(444), 'cuatrocientos cuarenta y cuatro')
        self.assertEquals(self.trad.sing(500), 'quinientos')
        self.assertEquals(self.trad.sing(555), 'quinientos cincuenta y cinco')
        self.assertEquals(self.trad.sing(600), 'seiscientos')
        self.assertEquals(self.trad.sing(666), 'seiscientos sesenta y seis')
        self.assertEquals(self.trad.sing(700), 'setecientos')
        self.assertEquals(self.trad.sing(777), 'setecientos setenta y siete')
        self.assertEquals(self.trad.sing(800), 'ochocientos')
        self.assertEquals(self.trad.sing(888), 'ochocientos ochenta y ocho')
        self.assertEquals(self.trad.sing(900), 'novecientos')
        self.assertEquals(self.trad.sing(953), 'novecientos cincuenta y tres')
        self.assertEquals(self.trad.sing(999), 'novecientos noventa y nueve')

    def test_miles(self):
        self.assertEquals(self.trad.sing(4326), 'cuatro mil trescientos veintiseis')
        self.assertEquals(self.trad.sing(7532), 'siete mil quinientos treinta y dos')
        self.assertEquals(self.trad.sing(1014), 'mil catorce')
        self.assertEquals(self.trad.sing(21000), 'veintiun mil')
        self.assertEquals(self.trad.sing(71000), 'setenta y un mil')

        self.assertEquals(self.trad.sing(916543), 'novecientos dieciseis mil quinientos cuarenta y tres')

    def test_numeros_grandes(self):
        self.assertEquals(self.trad.sing(1000000), 'un millón');
        self.assertEquals(self.trad.sing(1000021), 'un millón veintiuno');
        self.assertEquals(self.trad.sing(41000021), 'cuarenta y un millones veintiuno');
        self.assertEquals(self.trad.sing(41000021), 'cuarenta y un millones veintiuno');

        self.assertEquals(self.trad.sing(416010015), 'cuatrocientos dieciseis millones diez mil quince');
        self.assertEquals(self.trad.sing(1123123123123123123123123123123123456123456), 'un millon ciento veintitres mil ciento veintitres billones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres trillones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres billones ciento veintitres mil cuatrocientos cincuenta y seis millones ciento veintitres mil cuatrocientos cincuenta y seis');

    def test_decimales(self):
        self.assertEquals(self.trad.sing(16.1), 'dieciseis con 10/100')
        self.assertEquals(self.trad.sing(16.321), 'dieciseis con 32/100')
        self.assertEquals(self.trad.sing(16.80), 'dieciseis con 80/100')
        self.assertEquals(self.trad.sing(16.51), 'dieciseis con 51/100')
        self.assertEquals(self.trad.sing(1.75), 'uno con 75/100')
        self.assertEquals(self.trad.sing(Decimal('1123123123123123123123123123123123456123456.33')), 'un millon ciento veintitres mil ciento veintitres billones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres trillones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres billones ciento veintitres mil cuatrocientos cincuenta y seis millones ciento veintitres mil cuatrocientos cincuenta y seis con 33/100');
        self.assertEquals(self.trad.sing(Decimal('1123123123123123123123123123123123456123456.67')), 'un millon ciento veintitres mil ciento veintitres billones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres trillones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres billones ciento veintitres mil cuatrocientos cincuenta y seis millones ciento veintitres mil cuatrocientos cincuenta y seis con 67/100');



if __name__ == '__main__':

    unittest.main()

