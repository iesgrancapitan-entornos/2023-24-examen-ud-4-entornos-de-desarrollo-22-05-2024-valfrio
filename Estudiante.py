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
    def __init__(self, vale_name, value_nif, value_apellidos):
        self.__nif = value_nif
        self.__nombre = vale_name
        self.__apellidos = value_apellidos


class Estudiante(Persona):
    nif = "11111111Z";
    curso = "Primaria";
    nombre = "Nombre";
    apellidos = "Apellidos";

    def __init__(self):
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        return self.__nif

    @nif.setter
    def nif(self, value):
        self.__nif = value

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, value):
        self.__curso = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        self.__nombre = value

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value

