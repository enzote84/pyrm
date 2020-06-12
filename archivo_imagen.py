#
# DEMR
#
# clase: ArchivoImagen
#
# 2013-Oct-19
#

# importar la clase Imagen:
import imagen
# importar libreria para la conversion de binarios:
import struct

class ArchivoImagen(object):
    """
    Clase que permite la carga de una imagen desde un archivo.
    """
    
    def cargarImagenIC2(self, nombre_archi):
        """
        Cargar una imagen almacenada en un archivo con formato IC2
        Formato del archivo:
        Cabecera: 5 lineas de propiedades en cualquier orden
            propiedad = valor
        Propiedades: ancho, alto, unidad, nPixelesX, nPixelesY
        Binario: pixeles como valores de punto flotante de 4 bytes
        """
        
        # objeto Imagen a retornar:
        img = imagen.Imagen()
        # manipulador del archivo:
        archi = open(nombre_archi, "r")
        # verificacion de la lectura:
        archi_ok = True
        
        # leer la cabecera:
        i = 0
        while i < 5 and archi_ok:
            # leer una linea
            linea = archi.readline().strip()
            # extraer propiedad y valor:
            pos_igual = linea.find("=")
            propiedad = linea[0:(pos_igual - 1)]
            valor = linea[(pos_igual + 2):]
            # ver a cual propiedad corresponde:
            if "ancho" == propiedad:
                img.ancho = float(valor)
            elif "alto" == propiedad:
                img.alto = float(valor)
            elif "unidad" == propiedad:
                img.unidad = valor
            elif "nPixelesX" == propiedad:
                img.nPixelesX = int(valor)
            elif "nPixelesY" == propiedad:
                img.nPixelesY = int(valor)
            else:
                # considerar el caso en el que el archivo sea erroneo:
                print("Error al leer cabecera del archivo: " + nombre_archi)
                archi_ok = False
            i = i + 1
        
        # guardar la posicion de fin de cabecera y cerrar el archivo:
        parte_binaria = archi.tell()
        archi.close()
        
        # leer los pixeles:
        if archi_ok:
            # abrir el archivo en modo binario:
            archi = open(nombre_archi, "rb")
            # moverse a la parte binaria:
            archi.seek(parte_binaria)
            # leer los pixeles:
            for y in range(img.nPixelesY):
                fila = []
                for x in range(img.nPixelesX):
                    # leer un pixel de 4 bytes (devuelve un string)
                    # y convertirlo a flotante:
                    (pixel,) = struct.unpack("f", archi.read(4))
                    fila.append(pixel)
                # agregar la fila a la matriz de la imagen:
                img.pixeles.append(fila)
            # cerrar archivo:
            archi.close()
        
        return img
