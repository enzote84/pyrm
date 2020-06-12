#
# DEMR
#
# clase: FiltroImagen
#
# 2013-Oct-21
#

# importar la clase Imagen.
import imagen

class FiltroImagen(object):
    """
    Clase base de una jerarquia de clases de filtros.
    Esta clase es abstracta, ya que no tiene sentido implementar un
    filtro sin una forma particular de filtrar.
    Todos los filtros son polimorficos y filtran cada uno a su forma.
    """
    
    def filtrarImagen(self, img):
        """
        Metodo que permite filtrar una imagen.
        Se redefine en clases hijas.
        """

