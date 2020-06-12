#
# DEMR
#
# clase: FiltroCuantizacionImagen
#
# 2013-Oct-23
#

# importar la clase Imagen y FiltroImagen:
import imagen
import filtro_imagen

class FiltroCuantizacionImagen(filtro_imagen.FiltroImagen):
    """
    Especializacion del FiltroImagen que realiza un pixelado
    de la imagen en N niveles al filtrarla.
    """
    
    def __init__(self, N):
        """
        Inicializacion de los N niveles de cuantizacion.
        """
        
        # el nivel minimo de cuantizacion es 2:
        if N >= 2:
            self.niveles = N
        else:
            print("Nivel de pixeles incorrecto. Se utilizara el valor 2")
            self.niveles = 2
        
    def filtrarImagen(self, img):
        """
        Metodo que permite filtrar una imagen.
        Implementado como un cuantizado de la Imagen.
        """

        # generar una lista de valores cuantizados:
        pixel_min = img.intensidadMinima()
        pixel_max = img.intensidadMaxima()
        delta_cuantico = (pixel_max - pixel_min)/(self.niveles - 1)
        valores_cuantizados = list()
        while pixel_min <= pixel_max:
            valores_cuantizados.append(pixel_min)
            pixel_min = pixel_min + delta_cuantico
        
        # recorrer los pixeles de la imagen:
        fila_ini = 0
        fila_max = img.nPixelesY
        columna_ini = 0
        columna_max = img.nPixelesX
        for fila in range(fila_ini, fila_max):
            for columna in range(columna_ini, columna_max):
                # verificar a cual de los valores cuantizados se acerca mas el pixel:
                for i in range(len(valores_cuantizados) - 1):
                    if valores_cuantizados[i] <= img.pixeles[fila][columna] <= valores_cuantizados[i+1]:
                        dif1 = img.pixeles[fila][columna] - valores_cuantizados[i]
                        dif2 = valores_cuantizados[i+1] - img.pixeles[fila][columna]
                        if dif1 < dif2:
                            img.pixeles[fila][columna] = valores_cuantizados[i]
                        else:
                            img.pixeles[fila][columna] = valores_cuantizados[i+1]


