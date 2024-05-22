"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    """
    Clase persona.
    """
    def __init__(self, vale_name, value_nif, value_apellidos):
        """
        Inicializador de la clase persona.

        :param vale_name: Nombre de la persona.
        :param value_nif: Dni de la persona.
        :param value_apellidos: Apellidos de la persona.
        """
        self.__nif = value_nif
        self.__nombre = vale_name
        self.__apellidos = value_apellidos


class Estudiante(Persona):
    """
    Clase estudiante derivada de persona.
    """
    nif = "11111111Z";
    curso = "Primaria";
    nombre = "Nombre";
    apellidos = "Apellidos";

    def __init__(self):
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Inicializador de lc clase estudiante.

        :param nif: DNI del estudiante.
        :param curso: Curso del estudiante.
        :param nombre: Nombre del estudiante.
        :param apellidos: Apellidos del estudiante.
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """
        Getter del dni.

        :return: DNI del estudiante.
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Setter del dni.

        :param value: Valor a introducir.
        :return: Nada
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Getter del curso.

        :return: Curso del estudiante.
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Setter del curso.

        :param value: Valor del curso a introducir.
        :return: Nada.
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Getter del nombre.

        :return: Nombre del estudiante.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Setter del nombre.

        :param value: Valor del nombre a introducir.
        :return: Nada.
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Getter de los apellidos.

        :return: Apellidos del estudiante.
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Setter de los apellidos del estudiante.

        :param value: Valor de los apellidos a introducir.
        :return: Nada.
        """
        self.__apellidos = value

