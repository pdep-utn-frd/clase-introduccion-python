# vamos a usar la lib de testing que viene incluida en Python,
# pero hay otras, como por ejemplo:
# pytest
# nosetest
import unittest
from ejercicio import *

class EjercicioTest(unittest.TestCase):
	def test_precio_base_grande_de_muzza_es_100(self):
		grande_de_muzza = Muzzarella("grande")
		self.assertEqual(grande_de_muzza.precio_base(), 100)

	def test_precio_total_grande_de_muzza_es_600(self):
		"""
		El precio total de una grande de muzza debe ser
		600 debido a que su precio base es 100 y las pizzas
		de muzza cuestan 500 independientemente de su tamanio.
		"""
		grande_de_muzza = Muzzarella("grande")
		precio_base = grande_de_muzza.precio_base()
		precio_muzza = grande_de_muzza.precio_tipo()
		self.assertEqual(grande_de_muzza.precio(), precio_muzza + precio_base)

	def test_precio_napolitana_chica(self):
		napo_chica = Napolitana("chica")
		precio_base = napo_chica.precio_base()
		self.assertEqual(50, precio_base)
		precio_tipo = napo_chica.precio_tipo()
		self.assertEqual(500, precio_tipo)
		self.assertEqual(precio_tipo + precio_base, napo_chica.precio())

	# Dato random - convenciones de nombres (de metodos/variables):
	# testNosePuedeCrearHamburguesasInvalidas(self) <- camel case (usado java)
	# En Lisp se usa kebab-case: test-no-se-pueden-crear-hamburguesas-invalidas
	# En Python se usa snake case
	# Mas info en https://en.wikipedia.org/wiki/Naming_convention_(programming)
	def test_no_se_pueden_crear_hamburguesas_invalidas(self):
		self.assertRaises(CantidadInvalida, Hamburguesa, 10)

	def test_precio_del_flan(self):
		flan_sin_ddl = Flan(tiene_dulce_de_leche=False)
		self.assertEqual(280, flan_sin_ddl.precio())
		flan_con_ddl = Flan(tiene_dulce_de_leche=True)
		self.assertEqual(300, flan_con_ddl.precio())

	def test_pedido_vacio_cuesta_0(self):
		pedido_vacio = Pedido()
		self.assertEqual(0, pedido_vacio.precio())

	def test_pedido_con_muzza_y_flan_cuesta_900(self):
		muzza_grande = Muzzarella(tamanio="grande")
		flan_con_ddl = Flan(tiene_dulce_de_leche=True)
		pedido = Pedido(comidas=[muzza_grande, flan_con_ddl])
		sub_total = muzza_grande.precio() + flan_con_ddl.precio()
		self.assertEqual(sub_total * 1.15, pedido.precio())

# corro los tests
unittest.main()
