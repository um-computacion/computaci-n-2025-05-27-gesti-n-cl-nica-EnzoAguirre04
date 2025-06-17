"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/especialidad.py".
"""

#### Inicio del código.

### Inicio de Imports.

from typing import List

from src.modelo.excepciones import FormatoInvalidoException

### Fin de Imports.

### Inicio de la definición de la clase Especialidad.

class Especialidad:  # Representa una especialidad médica con su tipo y los días en que se atiende.
    ## Atributos Privados.
    def __init__(self, tipo: str, dias: List[str]):
        if not tipo.strip():
            raise FormatoInvalidoException("El tipo de especialidad no puede estar vacío.")
        valid_days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        if not dias or any(not dia.strip() or dia.strip().lower() not in valid_days for dia in dias):
            raise FormatoInvalidoException("Los días deben ser válidos (lunes a domingo).")
        self.__tipo__ = tipo.strip()  # Nombre de la especialidad (ej. Cardiología).
        self.__dias__ = [dia.strip().lower() for dia in dias]  # Lista de días de atención.

    ## Métodos.
    # Acceso a Información.
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de la especialidad."""
        return self.__tipo__

    def obtener_dias(self) -> List[str]:
        """Devuelve una copia de la lista de días de atención."""
        return self.__dias__.copy()

    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación en cadena de la especialidad."""
        return f"Especialidad: {self.__tipo__}, Días: {', '.join(self.__dias__)}"

### Fin de la definición de la clase Especialidad.

#### Fin del código.