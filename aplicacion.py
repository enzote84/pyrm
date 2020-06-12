#
# DEMR
#
# aplicacion PIRM13
#
# 2013-Oct-28
#

# importar clases:
import pyrm

# definir objeto manejar el sistema:
sistema = pyrm.PyRM()

# cargar la imagen desde el archivo elegido:
sistema.cargarImagen("imagenes/r1.ic2")

# informar valores originales de la imagen:
sistema.imprimirDatosImagen()

# seleccionar varios filtros:
sistema.agregarFiltro((0,))
sistema.agregarFiltro((0,))
sistema.agregarFiltro((1, 5))

# filtrar la imagen:
sistema.aplicarFiltros()

# informar valores filtrados de la imagen:
sistema.imprimirDatosImagen()

# eliminar banco de filtros:
sistema.eliminarFiltros()

# detectar region:
sistema.detectarRegion(5, 5)

# informar valores de la region:
sistema.imprimirDatosImagen()

# imprimir valor del area:
print("Area: " + str(sistema.area))
