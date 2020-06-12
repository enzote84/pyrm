#
# DEMR
#
# clase: FiltroBlurringImagen
#
# 2013-Oct-23
#

# importar la clase Imagen y FiltroImagen:
import imagen
import filtro_imagen
# importar libreria para copiar:
import copy

class FiltroBlurringImagen(filtro_imagen.FiltroImagen):
    """
    Especializacion del FiltroImagen que realiza un borroneado
    de la imagen al filtrarla.
    """
    
    def filtrarImagen(self, img):
        """
        Metodo que permite filtrar una imagen.
        Implementado como un borroneado de la Imagen.
        """
        
        # generar una imagen temporal, copia de la imagen original:
        img_tmp = copy.deepcopy(img)
        
        # recorrer los pixeles de la imagen, excepto los bordes:
        fila_ini = 1
        fila_max = img.nPixelesY - 1
        columna_ini = 1
        columna_max = img.nPixelesX - 1
        for fila in range(fila_ini, fila_max):
            for columna in range(columna_ini, columna_max):
                # calcular el promedio de los vecinos:
                promedio = 0.0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        promedio = promedio + img_tmp.pixeles[fila+i][columna+j]
                promedio = promedio/9.0
                img.pixeles[fila][columna] = promedio

