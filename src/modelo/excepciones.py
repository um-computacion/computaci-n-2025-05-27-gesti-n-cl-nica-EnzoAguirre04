"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/modelo/excepciones.py".
"""

## Inicio del código.

# Inicio de las excepciones personalizadas.

class ClinicaException(Exception):
    """Excepción base para errores específicos del sistema de la clínica."""
    pass

class PacienteNoEncontradoException(ClinicaException):
    """Excepción lanzada cuando no se encuentra un paciente con el DNI proporcionado."""
    pass

class MedicoNoDisponibleException(ClinicaException):
    """Excepción lanzada cuando un médico no está registrado o no atiende en el día/especialidad especificado."""
    pass

class TurnoOcupadoException(ClinicaException):
    """Excepción lanzada cuando se intenta agendar un turno en una fecha y hora ya ocupada."""
    pass

class RecetaInvalidaException(ClinicaException):
    """Excepción lanzada cuando la lista de medicamentos es inválida."""
    pass

class FormatoInvalidoException(ClinicaException):
    """Excepción lanzada cuando un formato de entrada (DNI, fecha, día) es inválido."""
    pass

# Fin de las excepciones personalizadas.

## Fin del código.