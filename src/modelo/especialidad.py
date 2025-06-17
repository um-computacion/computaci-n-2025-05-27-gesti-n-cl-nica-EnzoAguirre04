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

class Especialidad:  # Representa una especialidad médica junto con los días de atención asociados.
    ## Atributos Privados.
    DIAS_VALIDOS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    def __init__(self, tipo: str, dias: List[str]):
        if not tipo.strip():
            raise FormatoInvalidoException("El tipo de especialidad no puede estar vacío.")
        dias_normalizados = [dia.lower() for dia in dias]
        for dia in dias_normalizados:
            if dia not in self.DIAS_VALIDOS:
                raise FormatoInvalidoException(f"Día inválido: {dia}. Días válidos: {', '.join(self.DIAS_VALIDOS)}")
        
        self.__tipo__ = tipo  # Nombre de la especialidad (por ejemplo, "Pediatría", "Cardiología").
        self.__dias__ = dias_normalizados  # Lista de días en los que se atiende esta especialidad, en minúsculas.

    ## Métodos.
    # Acceso a Información.
    def obtener_especialidad(self) -> str:
        """Devuelve el nombre de la especialidad."""
        return self.__tipo__

    # Validaciones.
    def verificar_dia(self, dia: str) -> bool:
        """Devuelve True si la especialidad está disponible en el día proporcionado, false en caso contrario."""
        return dia.lower() in self.__dias__

    # Representación.
    def __str__(self) -> str:
        """Devuelve una cadena legible con el nombre de la especialidad y los días de atención."""
        dias_str = ", ".join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"
    
### Fin de la definición de la clase Especialidad.

#### Fin del código.