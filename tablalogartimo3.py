# Este programa proporciona una tabla de valores de los logaritmos de potencias de dos 

import math #esta linea traera la funcion logaritmica 

x = 1.0
while x < 100.0 :
	print(x, '\t' , math.log(x)/math.log(2.0))
	x = x * 2.0
