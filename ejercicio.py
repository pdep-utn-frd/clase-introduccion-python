# Cosas a tener en cuenta:
# override de metodos - no hay.
# objetos literales como los object de Wollok - no existen.

class Pizza():
    precio_por_tamanio = {
        "grande": 100,
        "mediana": 80,
        "chica": 50
    }

    def __init__(self, tamanio):
        self.tamanio = tamanio

    def precio_base(self):
        """
        Calcula el precio base de una pizza
        utilizando su tamanio.
        """
        return self.precio_por_tamanio[self.tamanio]

    def precio_tipo(self):
        pass

    def precio(self):
        return self.precio_base() + self.precio_tipo()


class Muzzarella(Pizza):
    def precio_tipo(self):
        return 500


class Calabresa(Pizza):
    def precio_tipo(self):
        if self.tamanio in ["mediana", "chica"]:
            return 600
        elif self.tamanio == "grande":
            return 700


class Napolitana(Pizza):
    def precio_tipo(self):
        return len(self.tamanio) * 100


class CantidadInvalida(Exception):
    def __init__(self, cantidad):
        mensaje = f"Se ingreso una cantidad invalida ({cantidad}) de medallones."
        # llamo al constructor de la clase Exception que toma un mensaje como
        # parametro.
        super().__init__(mensaje)


class Hamburguesa():
    def __init__(self, medallones):
		# notar que en este caso se realiza la validacion debido a
		# que se ejecuta el metodo medallones al asignarle un valor.
	    self.medallones = medallones

    @property  # getter
    def medallones(self):
        return self._medallones

    @medallones.setter
    def medallones(self, medallones):
        if 4 >= medallones >= 1:
            self._medallones = medallones
        else:
            raise CantidadInvalida(cantidad=medallones)

    def precio_base(self):
        return 120

    def precio(self):
        return self.precio_base() + 200 * self.medallones


class Flan():
    def __init__(self, tiene_dulce_de_leche=False):
        self.tiene_dulce_de_leche = tiene_dulce_de_leche

    def precio(self):
        if self.tiene_dulce_de_leche:
            return 300
        else:
            return 280


class Pedido():
    def __init__(self, comidas=[]):
        self.comidas = comidas

    def agregar_comida(self, comida):
        self.comidas.append(comida)

    def precio(self):
        precios = map(lambda c: c.precio(), self.comidas)
        return sum(precios) * 1.15
