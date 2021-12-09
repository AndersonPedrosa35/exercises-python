from exercise_dia2 import television
import unittest

class test_television(unittest.TestCase):
    def test_aumentar_volume(self):
        samsung = television(145)
        volume_anterior = samsung.volume
        samsung.aumentar_volume()
        self.assertEqual(samsung.volume, volume_anterior + 1)

    def test_diminuir_volume(self):
        samsung = television(145)
        volume_anterior = samsung.volume
        samsung.diminuir_volume()
        self.assertEqual(samsung.volume, volume_anterior - 1)
    
    def test_modificar_canal(self):
        samsung = television(145)
        samsung.modificar_canal(20)
        self.assertEqual(samsung.canal, 20)
    
    def test_exception_modificar_canal(self):
        samsung = television(145)
        with self.assertRaises(ValueError):
            samsung.modificar_canal(101)

    def test_liga_desligar(self):
        samsung = television(145)
        samsung.liga_desligar()
        self.assertEqual(samsung.ligada, True)

# def teste_television_render():
#     "Deve renderizar a instancia do objeto, mostrando os seus atributos"
#     sansumg = television(145)
#     assert sansumg.tamanho in {'volume': 50, 'canal': 1, 'tamanho': 145, 'ligada': False}
   