#
# DEMR
#
# clase: Imagen
#
# 2013-Oct-19
#

class Imagen(object):
    """
    Clase que modela a una imagen en memoria.
    Atributos: pixeles, ancho, alto, unidad, nPixelesX, nPixelesY
    """
    
    def __init__(self):
        # inicializar atributos:
        # pixeles:
        self.pixeles = []
        # metadatos:
        self.ancho = 0.0
        self.alto = 0.0
        self.unidad = ""
        self.nPixelesX = 0
        self.nPixelesY = 0

    def __str__(self):
        # ver metadatos de la imagen:
        texto = "Dimension: " + str(self.ancho) + " x " + str(self.alto) + " " + self.unidad + "\n"
        texto += "Pixeles: " + str(self.nPixelesX) + " x " + str(self.nPixelesY)
        return texto
    
    def imprimirPixeles(self):
        # imprimir pixeles en pantalla:
        for fila in self.pixeles:
            cadena = ""
            for pixel in fila:
                cadena = cadena + str(pixel) + " "
            print(cadena)

    def intensidadMinima(self):
        """
        Calcula la intensidad minima de la imagen
        """
        
        minimo = float('inf')
        for fila in self.pixeles:
            for pixel in fila:
                if pixel < minimo:
                    minimo = pixel
        return minimo
    
    def intensidadMaxima(self):
        """
        Calcula la intensidad maxima de la imagen
        """
        
        maximo = float('-inf')
        for fila in self.pixeles:
            for pixel in fila:
                if maximo < pixel:
                    maximo = pixel
        return maximo

