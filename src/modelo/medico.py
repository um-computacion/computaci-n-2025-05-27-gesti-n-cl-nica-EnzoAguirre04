"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/medico.py".
"""

#### Inicio del código.

### Inicio de Imports.

from typing import List, Optional

from src.modelo.especialidad import Especialidad
from src.modelo.excepciones import FormatoInvalidoException

### Fin de Imports.

### Inicio de la definición de la clase Medico.

class Medico:  # Representa a un médico de la clínica, con sus datos personales y especialidades.
    ## Atributos Privados.
    def __init__(self, nombre: str, matricula: str):
        if not nombre.strip():
            raise FormatoInvalidoException("El nombre del médico no puede estar vacío.")
        if not all(c.isalpha() or c.isspace() for c in nombre.strip()):
            raise FormatoInvalidoException("El nombre solo puede contener letras y espacios.")
        if not matricula.strip():
            raise FormatoInvalidoException("La matrícula no puede estar vacía.")
        self.__nombre__ = nombre.strip()  # Nombre completo del médico.
        self.__matricula__ = matricula.strip()  # Matrícula profesional del médico.
        self.__especialidades__ = []  # Lista de especialidades que el médico puede atender.

    ## Métodos.
    # Registro de Datos.
    def agregar_especialidad(self, especialidad: Especialidad):
        """Agrega una especialidad a la lista del médico si no está registrada."""
        if especialidad in self.__especialidades__:
            raise FormatoInvalidoException(f"El médico ya tiene la especialidad {especialidad.obtener_tipo()}.")
        self.__especialidades__.append(especialidad)

    # Acceso a Información.
    def obtener_matricula(self) -> str:
        """Devuelve la matrícula del médico."""
        return self.__matricula__

    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        """Devuelve la especialidad disponible para un día dado, o None si no hay ninguna."""
        dia = dia.lower()
        for especialidad in self.__especialidades__:
            if dia in [d.lower() for d in especialidad.obtener_dias()]:
                return especialidad.obtener_tipo()
        return None

    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación en cadena del médico."""
        especialidades_str = ", ".join([e.obtener_tipo() for e in self.__especialidades__]) or "Sin especialidades"
        return f"Médico: {self.__nombre__}, Matrícula: {self.__matricula__}, Especialidades: {especialidades_str}"

### Fin de la definición de la clase Medico.

#### Fin del código.