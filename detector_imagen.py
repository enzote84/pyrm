#
# DEMR
#
# clase: DetectorImagen
#
# 2013-Oct-24
#

# importar Imagen:
import imagen
# importar libreria para copiar:
import copy

# definir la clase DetectorImagen:
class DetectorImagen(object):
    """
    Clase que permite detectar estructuras dentro de una Imagen.
    """
    
    def detectarRegion(self, img, fila, columna):
        """
        Esta funcion genera una imagen con la region detectada y el valo de la
        cantidad de pixeles detectados.
        """
        
        # contador de pixeles detectados:
        self.area = 0
        # imagen con la region detectada:
        self.region = copy.deepcopy(img)
        # limpiar los pixeles de la region:
        for i in range(self.region.nPixelesY):
            for j in range(self.region.nPixelesX):
                self.region.pixeles[i][j] = 0.0
        # color que se busca en la region:
        self.color = img.pixeles[fila][columna]

        # ejecutar el pintor:
        self.pintor(img, fila, columna)
        
        # retornar una tupla con los valores:
        return (self.region, self.area)
        
    # algoritmo del pintor para encontrar la region:
    def pintor(self, img, fila, columna):
        """
        Funcion recursiva que aplica el algoritmo del pintor.
        """
        
        # verificar que el pixel pertenece a la imagen:
        if fila >= 0 and columna >= 0 and fila < img.nPixelesY and columna < img.nPixelesX:
            # verificar que el color sea valido:
            if img.pixeles[fila][columna] >= self.color*0.9 and img.pixeles[fila][columna] <= self.color*1.1:
                # verificar que todavia no paso por ahi:
                    if self.region.pixeles[fila][columna] == 0.0:
                        # pintar la region de blanco:
                        self.region.pixeles[fila][columna] = 1.0
                        # incrementar el contador de area:
                        self.area = self.area + 1
                        # ejecutar el pintor en los 8 pixeles vecinos:
                        self.pintor(img, fila+1, columna+1)
                        self.pintor(img, fila+1, columna)
                        self.pintor(img, fila+1, columna-1)
                        self.pintor(img, fila, columna+1)
                        self.pintor(img, fila, columna-1)
                        self.pintor(img, fila-1, columna+1)
                        self.pintor(img, fila-1, columna)
                        self.pintor(img, fila-1, columna-1)
    

