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
        self.assertSing(16, 'dieciséis')
        self.assertSing(17, 'diecisiete')
        self.assertSing(18, 'dieciocho')
        self.assertSing(19, 'diecinueve')
        self.assertSing(20, 'veinte')
        self.assertSing(21, 'veintiuno')
        self.assertSing(22, 'veintidós')
        self.assertSing(23, 'veintitrés')
        self.assertSing(24, 'veinticuatro')
        self.assertSing(25, 'veinticinco')
        self.assertSing(26, 'veintiséis')
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
        self.assertSing(222, 'doscientos veintidós')
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
        self.assertSing(4326, 'cuatro mil trescientos veintiséis')
        self.assertSing(7532, 'siete mil quinientos treinta y dos')
        self.assertSing(1014, 'mil catorce')
        self.assertSing(21000, 'veintiún mil')
        self.assertSing(71000, 'setenta y un mil')

        self.assertSing(916543, 'novecientos dieciséis mil quinientos cuarenta y tres')


    def test_millones(self):
        self.assertSing(10 ** 6, 'un millón')
        self.assertSing(10 ** 12, 'un billón')
        self.assertSing(10 ** 18, 'un trillón')
        self.assertSing(10 ** 24, 'un cuatrillón')


    def test_numeros_grandes(self):
        self.assertSing(1000000, 'un millón')
        self.assertSing(1000021, 'un millón veintiuno')
        self.assertSing(41000021, 'cuarenta y un millones veintiuno')
        self.assertSing(41000021, 'cuarenta y un millones veintiuno')

        self.assertSing(416010015, 'cuatrocientos dieciséis millones diez mil quince')
        self.assertSing(123123123123123123123456123456,
                        'ciento veintitrés mil ciento veintitrés cuatrillones '
                        'ciento veintitrés mil ciento veintitrés trillones '
                        'ciento veintitrés mil ciento veintitrés billones '
                        'ciento veintitrés mil cuatrocientos cincuenta y seis millones '
                        'ciento veintitrés mil cuatrocientos cincuenta y seis')

    def test_decimales(self):
        self.assertSing(16.1, 'dieciséis con 10/100')
        self.assertSing(16.321, 'dieciséis con 32/100')
        self.assertSing(16.80, 'dieciséis con 80/100')
        self.assertSing(16.51, 'dieciséis con 51/100')
        self.assertSing(1.75, 'uno con 75/100')
        self.assertSing(Decimal('123123123123123123123456123456.33'),
                        'ciento veintitrés mil ciento veintitrés cuatrillones '
                        'ciento veintitrés mil ciento veintitrés trillones '
                        'ciento veintitrés mil ciento veintitrés billones '
                        'ciento veintitrés mil cuatrocientos cincuenta y seis millones '
                        'ciento veintitrés mil cuatrocientos cincuenta y seis con 33/100')
        self.assertSing(Decimal('123123123123123123123456123456.67'),
                        'ciento veintitrés mil ciento veintitrés cuatrillones '
                        'ciento veintitrés mil ciento veintitrés trillones '
                        'ciento veintitrés mil ciento veintitrés billones '
                        'ciento veintitrés mil cuatrocientos cincuenta y seis millones '
                        'ciento veintitrés mil cuatrocientos cincuenta y seis con 67/100')

    def test_value_error_raised_on_invalid_number(self):
        self.assertRaises(ValueError, sing, 10 ** 30)


if __name__ == '__main__':
    unittest.main()
