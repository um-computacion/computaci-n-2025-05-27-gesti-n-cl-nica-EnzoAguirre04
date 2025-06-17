"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/turno.py".
"""

#### Inicio del código.

### Inicio de Imports.

from datetime import datetime

from src.modelo.excepciones import FormatoInvalidoException
from src.modelo.medico import Medico
from src.modelo.paciente import Paciente

### Fin de Imports.

### Inicio de la definición de la clase Turno.

class Turno:  # Representa un turno médico entre un paciente y un médico para una especialidad específica en una fecha y hora determinada.
    ## Atributos Privados.
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not especialidad.strip():
            raise FormatoInvalidoException("La especialidad no puede estar vacía.")
        self.__paciente__ = paciente  # Paciente que asiste al turno.
        self.__medico__ = medico  # Médico asignado al turno.
        self.__fecha_hora__ = fecha_hora  # Fecha y hora del turno.
        self.__especialidad__ = especialidad  # Especialidad médica del turno.

    ## Métodos.
    # Acceso a Información
    def obtener_medico(self) -> Medico:
        """Devuelve el médico asignado al turno."""
        return self.__medico__

    def obtener_fecha_hora(self) -> datetime:
        """Devuelve la fecha y hora del turno."""
        return self.__fecha_hora__

    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación legible del turno, incluyendo paciente, médico, especialidad y fecha/hora."""
        fecha_formateada = self.__fecha_hora__.strftime("%d/%m/%Y %H:%M")
        return (
            f"Paciente: {self.__paciente__.__nombre__} (DNI: {self.__paciente__.obtener_dni()}), "
            f"Médico: {self.__medico__.__nombre__} (Matrícula: {self.__medico__.obtener_matricula()}), "
            f"Especialidad: {self.__especialidad__}, "
            f"Fecha: {fecha_formateada}"
        )

### Fin de la definición de la clase Turno.

#### Fin del código.