class Pizza {

	const property tamanio
	const precioPorTamanio = {
		const precios = new Dictionary()
		precios.put("grande", 100)
		precios.put("mediana", 80)
		precios.put("chica", 50)
		return precios
	}.apply()

	method precioBase() {
		return precioPorTamanio.get(tamanio)
	}

	method precioTipo()

	method precio() {
		return self.precioBase() + self.precioTipo()
	}

}

class Muzzarella inherits Pizza {

	override method precioTipo() = 500

}

class Calabresa inherits Pizza {

	override method precioTipo() {
		if ((tamanio == "mediana") or (tamanio == "chica")) {
			return 600
		} else {
			return 700
		}
	}

}

class Napolitana inherits Pizza {

	override method precioTipo() {
		return tamanio.size() * 100
	}

}

class CantidadInvalida inherits Exception {
	var cantidad
	override method message() {
		return "Se ingreso una cantidad invalida (" + cantidad + ") de medallones."
	}
}

class Hamburguesa {

	var medallones

	method initialize() {
		// se valida la cantidad de medallones.
		self.medallones(medallones)
	}

	method medallones() {
		return medallones
	}

	method medallones(cantidad) {
		if ((cantidad >= 1) and (cantidad <= 4)) {
			medallones = cantidad
		} else {
			throw new CantidadInvalida(cantidad=cantidad)
		}
	}

	method precioBase() = 120

	method precio() {
		return self.precioBase() + 200 * medallones
	}

}

class Flan {

	const tieneDulceDeLeche = false

	method precio() {
		if (tieneDulceDeLeche) {
			return 300
		} else {
			return 280
		}
	}

}

class Pedido {

	const comidas = []

	method agregar_comida(unaComida) {
		comidas.add(unaComida)
	}

	method precio() {
		const subtotal = comidas.sum({ comida => comida.precio() })
		return subtotal * 1.15
	}

}

