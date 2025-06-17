"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/medico.py".
"""

#### Inicio del código.

### Inicio de Imports.

from typing import Optional

from src.modelo.excepciones import FormatoInvalidoException
from src.modelo.especialidad import Especialidad

### Fin de Imports.

### Inicio de la definición de la clase Medico.

class Medico:  # Representa a un médico del sistema, con sus especialidades y matrícula profesional.
    ## Atributos Privados.
    def __init__(self, nombre: str, matricula: str):
        if not nombre.strip():
            raise FormatoInvalidoException("El nombre del médico no puede estar vacío.")
        if not matricula.strip():
            raise FormatoInvalidoException("La matrícula del médico no puede estar vacía.")
        
        self.__nombre__ = nombre  # Nombre completo del médico.
        self.__matricula__ = matricula  # Matrícula profesional del médico (clave única).
        self.__especialidades__ = []  # Lista de especialidades con sus días de atención.

    ## Métodos.
    # Registro de Datos.
    def agregar_especialidad(self, especialidad: Especialidad):
        """Agrega una especialidad a la lista del médico."""
        if especialidad.obtener_especialidad() in [e.obtener_especialidad() for e in self.__especialidades__]:
            raise FormatoInvalidoException(f"La especialidad {especialidad.obtener_especialidad()} ya está registrada.")
        self.__especialidades__.append(especialidad)

    # Acceso a Información.
    def obtener_matricula(self) -> str:
        """Devuelve la matrícula del médico."""
        return self.__matricula__

    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        """Devuelve el nombre de la especialidad disponible en el día especificado, o None si no atiende ese día."""
        for esp in self.__especialidades__:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    # Representación.
    def __str__(self) -> str:
        """Representación legible del médico, incluyendo matrícula y especialidades."""
        especialidades_str = "\n  ".join(str(e) for e in self.__especialidades__) or "Sin especialidades"
        return f"Médico: {self.__nombre__}\nMatrícula: {self.__matricula__}\nEspecialidades:\n  {especialidades_str}"

### Fin de la definición de la clase Medico.

#### Fin del código.