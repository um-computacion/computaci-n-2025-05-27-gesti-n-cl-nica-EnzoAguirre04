"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/historiaclinica.py".
"""

#### Inicio del código.

### Inicio de Imports.

from typing import List

from src.modelo.paciente import Paciente
from src.modelo.receta import Receta
from src.modelo.turno import Turno

### Fin de Imports.

### Inicio de la definición de la clase HistoriaClinica.

class HistoriaClinica:  # Clase que almacena la información médica de un paciente: turnos y recetas.
    ## Atributos Privados.
    def __init__(self, paciente: Paciente):
        self.__paciente__ = paciente  # Paciente al que pertenece la historia clínica.
        self.__turnos__ = []  # Lista de turnos agendados del paciente.
        self.__recetas__ = []  # Lista de recetas emitidas para el paciente.

    ## Métodos.
    # Registro de Datos.
    def agregar_turno(self, turno: Turno):
        """Agrega un nuevo turno a la historia clínica."""
        self.__turnos__.append(turno)

    def agregar_receta(self, receta: Receta):
        """Agrega una receta médica a la historia clínica."""
        self.__recetas__.append(receta)

    # Acceso a Información.
    def obtener_turnos(self) -> List[Turno]:
        """Devuelve una copia de la lista de turnos del paciente."""
        return self.__turnos__.copy()

    def obtener_recetas(self) -> List[Receta]:
        """Devuelve una copia de la lista de recetas del paciente."""
        return self.__recetas__.copy()

    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación textual de la historia clínica, incluyendo turnos y recetas."""
        turnos_str = "\n".join(str(t) for t in self.__turnos__) if self.__turnos__ else "  Sin turnos registrados"
        recetas_str = "\n".join(str(r) for r in self.__recetas__) if self.__recetas__ else "  Sin recetas registradas"
        return (
            f"Historia Clínica de {self.__paciente__}\n\n"
            f"Turnos:\n{turnos_str}\n\n"
            f"Recetas:\n{recetas_str}"
        )

### Fin de la definición de la clase HistoriaClinica.

#### Fin del código.