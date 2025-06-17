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

class Paciente:  # Representa a un paciente de la clínica.
    ## Atributos Privados.
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre.strip():
            raise FormatoInvalidoException("El nombre del paciente no puede estar vacío.")
        if not self._validar_dni(dni):
            raise FormatoInvalidoException("El DNI debe contener 8 dígitos numéricos.")
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise FormatoInvalidoException("Formato de fecha de nacimiento inválido. Use dd/mm/aaaa.")
        
        self.__nombre__ = nombre  # Nombre completo del paciente.
        self.__dni__ = dni  # DNI del paciente (identificador único).
        self.__fecha_nacimiento__ = fecha_nacimiento  # Fecha de nacimiento del paciente en formato dd/mm/aaaa.

    ## Métodos.
    # Validaciones.
    def _validar_dni(self, dni: str) -> bool:
        """Valida que el DNI contenga 8 dígitos numéricos."""
        return dni.isdigit() and len(dni) == 8

    # Acceso a Información.
    def obtener_dni(self) -> str:
        """Devuelve el DNI del paciente."""
        return self.__dni__

    # Representación.
    def __str__(self) -> str:
        """Representación en texto del paciente."""
        return f"Paciente: {self.__nombre__}, DNI: {self.__dni__}, Fecha de nacimiento: {self.__fecha_nacimiento__}"

### Fin de la definición de la clase Paciente.

#### Fin del código.