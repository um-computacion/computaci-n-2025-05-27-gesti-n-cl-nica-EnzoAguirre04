"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/receta.py".
"""

#### Inicio del código.

### Inicio de Imports.

from datetime import datetime
from typing import List

from src.modelo.excepciones import RecetaInvalidaException
from src.modelo.medico import Medico
from src.modelo.paciente import Paciente

### Fin de Imports.

### Inicio de la definición de la clase Receta.

class Receta:  # Representa una receta médica emitida por un médico a un paciente, incluyendo los medicamentos recetados y la fecha de emisión.
    ## Atributos Privados.
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: List[str]):
        if not medicamentos or any(not med.strip() for med in medicamentos):
            raise RecetaInvalidaException("La lista de medicamentos no puede estar vacía o contener entradas inválidas.")
        self.__paciente__ = paciente  # Paciente al que se le emite la receta.
        self.__medico__ = medico  # Médico que emite la receta.
        self.__medicamentos__ = [med.strip() for med in medicamentos]  # Lista de medicamentos recetados.
        self.__fecha = datetime.now()  # Fecha de emisión de la receta. | Asignada automáticamente con datetime.now().

    ## Métodos.
    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación en cadena de la receta."""
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        medicamentos_str = ", ".join(self.__medicamentos__) or "Sin medicamentos"
        return (
            f"Receta\n"
            f"  Fecha: {fecha_str}\n"
            f"  Paciente: {self.__paciente__.obtener_dni()} - {self.__paciente__}\n"
            f"  Médico: {self.__medico__.obtener_matricula()} - {self.__medico__}\n"
            f"  Medicamentos: {medicamentos_str}"
        )

### Fin de la definición de la clase Receta.

#### Fin del código.