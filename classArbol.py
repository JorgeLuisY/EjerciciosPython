class Arbol :
	def __init__(self, carga , izquierdo = None , derecho = None):
		self.carga = carga
		self. izquierdo = izquierdo
		self.derecho = derecho

	def __str__(self):
		return str(self.carga)
	def obtenerCarga(self): return self.carga
	def obtenerIzquierdo(self): return self.izquierdo
	def obtenerDerecho(self): return self.derecho
	def asignarCarga(self, carga):self.carga = carga
	def asignarIzquierdo(self , izquierdo): self.izquierdo = izquierdo
	def asignarDerecho(self, derecho): self.derecho = derecho
	def total(arbol) :
		if arbol == None : return 0
		return total(arbol.izquierdo) + total(arbol.derecho) + carga
	def imprimirArbol(arbol):
		if arbol == None : return
		print (arbol.carga , )
		imprimirArbol(arbol.izquierdo)
		imprimirArbol(arbol.derecho)
	def imprimirArbolPostOrden(arbol):
		if arbol == None : return
		imprimirArbol(arbol.izquierdo)
		imprimirArbol(arbol.derecho)
		print (arbol.carga ,)
	def imprimirArbolEnOrden(arbol):
		if arbol == None : return
		imprimirArbolEnOrden(arbol.izquiedo)
		print (arbol.carga , )
		imprimirArbolEnOrden(arbol.derecho)
	def imprimirArbolIndentado(arbol, level=0) :
		if arbol == None : return
		imprimirArbolIndentado(arbol.derecho, level+1)
		print (' ' * level + str(arbol.carga))
		imprimirArbolIndentado(arbol.izquierdo, level+1)
