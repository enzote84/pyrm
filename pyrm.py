#
# DEMR
#
# clase: PyRM
#
# 2013-Oct-28
#

# importar clases de modulos:
import imagen
import archivo_imagen
import filtro_blurring_imagen
import filtro_cuantizacion_imagen
import detector_imagen

class PyRM(object):
    """
    Clase que modela al sistema de procesamiento de imagenes de resonancia magnetica.
    """
    
    def __init__(self):
        """
        Inicializar modulos.
        """
        
        # modulo de carga de imagen desde archivo:
        self.archi = archivo_imagen.ArchivoImagen()
        # banco de filtros:
        self.filtros = list()
        # detector de regiones:
        self.detector = detector_imagen.DetectorImagen()
    
    def cargarImagen(self, nombre_archi):
        """
        Cargar una imagen en memoria.
        """
        
        self.img = self.archi.cargarImagenIC2(nombre_archi)
    
    def imprimirDatosImagen(self):
        """
        Imprimir los datos de la imagen en pantalla.
        """
        
        print(self.img)
        self.img.imprimirPixeles()
    
    def agregarFiltro(self, tipo_filtro):
        """
        Agrega un filtro al banco de filtros, codificado segun lo siguiente:
        0 - filtro blurring
        1, N - filtro cuantizacion de N niveles
        """
        
        if tipo_filtro[0] == 0:
            self.filtros.append(filtro_blurring_imagen.FiltroBlurringImagen())
        elif tipo_filtro[0] == 1:
            self.filtros.append(filtro_cuantizacion_imagen.FiltroCuantizacionImagen(tipo_filtro[1]))
    
    def aplicarFiltros(self):
        """
        Aplica todos los filtros del banco de filtros a la imagen actual.
        """
        
        for filtro in self.filtros:
            filtro.filtrarImagen(self.img)
    
    def eliminarFiltros(self):
        """
        Elimina todos los filtros del banco de filtros.
        """
        
        del self.filtros[:]

    def detectarRegion(self, fila, columna):
        """
        Genera una imagen con la region detectada en el punto inicial fila, columna.
        """
        
        (self.img, self.area) = self.detector.detectarRegion(self.img, fila, columna)
    
