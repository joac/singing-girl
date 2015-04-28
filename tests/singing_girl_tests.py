#! -*- coding: utf8 -*-

import unittest
from singing_girl import sing
from decimal import Decimal

class TestTraductorNumeros(unittest.TestCase):

    def assertSing(self, number, text):
        self.assertEquals(sing(number), text)

    def test_digitos(self):
        self.assertSing(0, 'cero')
        self.assertSing(1, 'uno')
        self.assertSing(2, 'dos')
        self.assertSing(3, 'tres')
        self.assertSing(4, 'cuatro')
        self.assertSing(5, 'cinco')
        self.assertSing(6, 'seis')
        self.assertSing(7, 'siete')
        self.assertSing(8, 'ocho')
        self.assertSing(9, 'nueve')

    def test_decenas(self):
        self.assertSing(10, 'diez')
        self.assertSing(11, 'once')
        self.assertSing(12, 'doce')
        self.assertSing(13, 'trece')
        self.assertSing(14, 'catorce')
        self.assertSing(15, 'quince')
        self.assertSing(16, 'dieciseis')
        self.assertSing(17, 'diecisiete')
        self.assertSing(18, 'dieciocho')
        self.assertSing(19, 'diecinueve')
        self.assertSing(20, 'veinte')
        self.assertSing(21, 'veintiuno')
        self.assertSing(22, 'veintidos')
        self.assertSing(23, 'veintitres')
        self.assertSing(24, 'veinticuatro')
        self.assertSing(25, 'veinticinco')
        self.assertSing(26, 'veintiseis')
        self.assertSing(27, 'veintisiete')
        self.assertSing(28, 'veintiocho')
        self.assertSing(29, 'veintinueve')
        self.assertSing(30, 'treinta')
        self.assertSing(37, 'treinta y siete')
        self.assertSing(40, 'cuarenta')
        self.assertSing(42, 'cuarenta y dos')
        self.assertSing(50, 'cincuenta')
        self.assertSing(55, 'cincuenta y cinco')
        self.assertSing(60, 'sesenta')
        self.assertSing(66, 'sesenta y seis')
        self.assertSing(70, 'setenta')
        self.assertSing(77, 'setenta y siete')
        self.assertSing(80, 'ochenta')
        self.assertSing(88, 'ochenta y ocho')
        self.assertSing(90, 'noventa')
        self.assertSing(99, 'noventa y nueve')

    def test_centenas(self):
        self.assertSing(100, 'cien')
        self.assertSing(111, 'ciento once')
        self.assertSing(200, 'doscientos')
        self.assertSing(222, 'doscientos veintidos')
        self.assertSing(300, 'trescientos')
        self.assertSing(333, 'trescientos treinta y tres')
        self.assertSing(400, 'cuatrocientos')
        self.assertSing(444, 'cuatrocientos cuarenta y cuatro')
        self.assertSing(500, 'quinientos')
        self.assertSing(555, 'quinientos cincuenta y cinco')
        self.assertSing(600, 'seiscientos')
        self.assertSing(666, 'seiscientos sesenta y seis')
        self.assertSing(700, 'setecientos')
        self.assertSing(777, 'setecientos setenta y siete')
        self.assertSing(800, 'ochocientos')
        self.assertSing(888, 'ochocientos ochenta y ocho')
        self.assertSing(900, 'novecientos')
        self.assertSing(953, 'novecientos cincuenta y tres')
        self.assertSing(999, 'novecientos noventa y nueve')

    def test_miles(self):
        self.assertSing(4326, 'cuatro mil trescientos veintiseis')
        self.assertSing(7532, 'siete mil quinientos treinta y dos')
        self.assertSing(1014, 'mil catorce')
        self.assertSing(21000, 'veintiun mil')
        self.assertSing(71000, 'setenta y un mil')

        self.assertSing(916543, 'novecientos dieciseis mil quinientos cuarenta y tres')

    def test_numeros_grandes(self):
        self.assertSing(1000000, 'un millon');
        self.assertSing(1000021, 'un millon veintiuno');
        self.assertSing(41000021, 'cuarenta y un millones veintiuno');
        self.assertSing(41000021, 'cuarenta y un millones veintiuno');

        self.assertSing(416010015, 'cuatrocientos dieciseis millones diez mil quince');
        self.assertSing(1123123123123123123123123123123123456123456, 'un millon ciento veintitres mil ciento veintitres billones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres trillones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres billones ciento veintitres mil cuatrocientos cincuenta y seis millones ciento veintitres mil cuatrocientos cincuenta y seis');

    def test_decimales(self):
        self.assertSing(16.1, 'dieciseis con 10/100')
        self.assertSing(16.321, 'dieciseis con 32/100')
        self.assertSing(16.80, 'dieciseis con 80/100')
        self.assertSing(16.51, 'dieciseis con 51/100')
        self.assertSing(1.75, 'uno con 75/100')
        self.assertSing(Decimal('1123123123123123123123123123123123456123456.33'), 'un millon ciento veintitres mil ciento veintitres billones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres trillones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres billones ciento veintitres mil cuatrocientos cincuenta y seis millones ciento veintitres mil cuatrocientos cincuenta y seis con 33/100')
        self.assertSing(Decimal('1123123123123123123123123123123123456123456.67'), 'un millon ciento veintitres mil ciento veintitres billones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres trillones ciento veintitres mil ciento veintitres millones ciento veintitres mil ciento veintitres billones ciento veintitres mil cuatrocientos cincuenta y seis millones ciento veintitres mil cuatrocientos cincuenta y seis con 67/100')



if __name__ == '__main__':

    unittest.main()

