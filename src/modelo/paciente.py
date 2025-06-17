"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/paciente.py".
"""

#### Inicio del código.

### Inicio de Imports.

from datetime import datetime

from src.modelo.excepciones import FormatoInvalidoException

### Fin de Imports.

### Inicio de la definición de la clase Paciente.

class Paciente:  # Representa a un paciente de la clínica, con sus datos personales.
    ## Atributos Privados.
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre.strip():
            raise FormatoInvalidoException("El nombre del paciente no puede estar vacío.")
        if not all(c.isalpha() or c.isspace() for c in nombre.strip()):
            raise FormatoInvalidoException("El nombre solo puede contener letras y espacios.")
        if not dni.strip() or not dni.isdigit() or len(dni) != 8:
            raise FormatoInvalidoException("El DNI debe ser un número de 8 dígitos.")
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise FormatoInvalidoException("La fecha de nacimiento debe estar en formato dd/mm/aaaa.")
        self.__nombre__ = nombre.strip()  # Nombre completo del paciente.
        self.__dni__ = dni.strip()  # DNI del paciente.
        self.__fecha_nacimiento__ = fecha_nacimiento  # Fecha de nacimiento en formato "dd/mm/aaaa".

    ## Métodos.
    # Acceso a Información.
    def obtener_dni(self) -> str:
        """Devuelve el DNI del paciente."""
        return self.__dni__

    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación en cadena del paciente."""
        return f"Paciente: {self.__nombre__}, DNI: {self.__dni__}, Fecha de nacimiento: {self.__fecha_nacimiento__}"

### Fin de la definición de la clase Paciente.

#### Fin del código.