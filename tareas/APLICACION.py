#APLICACION arreglo persona
persona=[]
opcion=1
while opcion!=4:
    print "****Menu persona****"
    print "1.agregar"
    print "2.eliminar"
    print "3.reporte"
    print "4.salir"
    opcion= int(raw_input("seleccione un opcion(1-4): "))
    if opcion==1:
        print "***persona***"
        dni=raw_input("DNI: ")
        nombre=raw_input("Nombre: ")
        apellido=raw_input("Apellido: ")
        fecha_nacimiento=raw_input("Fecha de Nacimiento: ")
        talla= float(raw_input("Talla: "))
        persona.append([dni,nombre,apellido,fecha_nacimiento,talla])
    elif opcion==2:
        print "***eliminar***"
        i=0
        while i<len(persona):
            print i, persona[i]
            i+=1
            posicion_eliminar= int(raw_input("Ingrese la posicion que desea eliminar: "))
            persona.pop(posicion_eliminar)
            print "se elimino correctamente..."
    elif opcion==3:
                i=0
                print "***reporte***"
                while i<len(persona):
                    print i, persona[i]
                    i+=1
    else:
        print "Gracias por su visita..."
