"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:
    """
    Clase gato.
    """
    def maullar(self):
        """
        Método para que el gato maulle.

        :return: Nada.
        """
        self.maullido = 'Miau'
        print(self.maullido);

g = Gato();
g.maullar();
