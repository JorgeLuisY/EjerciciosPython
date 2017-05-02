def animal() :
	# arbol con un solo nodo
	raiz = Arbol("pajaro")
	# Hasta que el usuario salga
	while True:
		print()
		if not si(" Estas pensando en un animal ? ") : break
		# recorrer el Arbol
		arbol = raiz
		while arbol.obtenerIzquierdo() != None :
			prompt = arbol.obtenerCarga() + " ?"
			if si(prompt):
				arbol = arbol.obtenerDerecho()
			else:
				arbol = arbol.obtenerIzquierdo()
		# conjeturar!
		conjetura = arbol.obtenerCarga()
		prompt = "¿ Es un " + conjetura + " ? "
		if si(prompt) :
			print ("¡Soy el mejor!" + '\n' + " ******************** ! FIN DEL JUEGO ¡ ******************** "+ '\n'+ '\n'+ '\n')
			continue
		# obtener mas informacion
		prompt = "Cual es el nombre del animal ?  \n"
		animal = input(prompt)
		prompt = "Que pregunta permite distinguir, un %s de un %s ? \n"
		pregunta = input(prompt % (animal,conjetura))
		# agrega mas informacion al Arbol
		arbol.asignarCarga(pregunta)
		prompt = "Si el animal fuera un %s , la respuesta seria ?  \n"
		if si(prompt % animal) :
			arbol.asignarIzquierdo(Arbol(conjetura))
			arbol.asignarDerecho(Arbol(animal))
		else :
			arbol.asignarIzquierdo(Arbol(animal))
			arbol.asignarDerecho(Arbol(conjetura))
			
def si(pregunta):
	respuesta = (input(pregunta + "\n")).lower()
	print()
	return ( respuesta[0] == 's' or  respuesta[0] == 'y' )
                
