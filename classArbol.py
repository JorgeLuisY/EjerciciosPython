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
	def imprimirArbol(self):
		if self == None : return
		print (self.carga , )
		imprimirArbol(self.izquierdo)
		imprimirArbol(self.derecho)
	def imprimirArbolPostOrden(self):
		if self == None : return
		imprimirArbolPostOrden(self.izquierdo)
		imprimirArbolPostOrden(self.derecho)
		print (self.carga ,)
	def imprimirArbolEnOrden(self):
		if self == None : return
		imprimirArbolEnOrden(self.izquiedo)
		print (self.carga , )
		imprimirArbolEnOrden(self.derecho)
	def imprimirArbolIndentado(self, level=0) :
		if self == None : return
		imprimirArbolIndentado(self.derecho, level+1)
		print (' ' * level + str(self.carga))
		imprimirArbolIndentado(self.izquierdo, level+1)
