# Clase de introduccion al lenguaje Python

## Presentacion

La presentacion esta alojada en Google Drive siguiendo [este enlace](https://docs.google.com/presentation/d/1nzkC94fOXa6eP_MsBQKoainw6cjJy-ROePSNjVBAurw/edit?usp=sharing)


##  Ejercicio

[Resolución en Python](https://github.com/pdep-utn-frd/clase-introduccion-python/blob/main/ejercicio.py)


[Resolución en Wollok](https://github.com/pdep-utn-frd/clase-introduccion-python/tree/main/ejercicio-wollok)

Se desea modelar las ordenes de un restaurant con el objetivo de
saber cuanto es el precio total de las mismas.

El menu es muy reducido, al menos por ahora, por lo que se cuenta unicamente con
2 platos principales y 1 postre:

### Platos principales:
* **Pizzas**
	Las pizzas pueden venir en 3 tamaños: grande, mediana y chica.
	Cada una de las variantes tiene un precio base que depende unicamente
	del tamano, ademas del precio propio del tipo de pizza.

	Los precios base son los siguientes:

	- Grande   $100
	- Mediana  $80
	- Chica    $50


	**Tipos de Pizza**
	- Muzzarella   $500
	- Calabresa
		- Grande   $700
		- Mediana  $600
		- Chica    $600
	- Napolitana
		El precio se calcula como la cantidad de letras del tamano de la pizza
		multiplicado por 100.



* **Hamburguesa completa**
	El precio base es $120 + $200 por medallon.
	Pueden tener entre 1 y 4 medallones.

### Postres
* **Flan**   $280
  
  *Adicional:*
  Se puede agregar dulce de leche por $20.


Se pide:
 1. Modelar las ordenes y los distintos platos.
 2. Poder calcular el precio total de una orden teniendo en cuenta
    que este se calcula como la suma de todos los platos que incluye
	mas un adicional de 15%.
 3. Realizar tests.
