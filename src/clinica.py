"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/clinica.py".
"""

#### Inicio del código.

### Inicio de Imports.

from datetime import datetime
from typing import Dict, List, Optional

from src.modelo.excepciones import (
    FormatoInvalidoException,
    MedicoNoDisponibleException,
    PacienteNoEncontradoException,
    TurnoOcupadoException,
)
from src.modelo.historiaclinica import HistoriaClinica
from src.modelo.medico import Medico
from src.modelo.paciente import Paciente
from src.modelo.receta import Receta
from src.modelo.turno import Turno

### Fin de Imports.

### Inicio de la definición de la clase Clinica.

class Clinica:  # Clase principal que gestiona pacientes, médicos, turnos y recetas.
    ## Atributos Privados.
    def __init__(self):
        self.__pacientes__: Dict[str, Paciente] = {}  # Diccionario de pacientes (DNI -> Paciente).
        self.__medicos__: Dict[str, Medico] = {}  # Diccionario de médicos (Matrícula -> Médico).
        self.__turnos__: List[Turno] = []  # Lista de turnos agendados.
        self.__historias_clinicas__: Dict[str, HistoriaClinica] = {}  # Diccionario de historias clínicas (DNI -> HistoriaClinica).

    ## Métodos.
    # Registro de Pacientes y Médicos.
    def agregar_paciente(self, paciente: Paciente):
        """Registra un nuevo paciente en la clínica."""
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise FormatoInvalidoException(f"El paciente con DNI {dni} ya está registrado.")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        """Registra un nuevo médico en la clínica."""
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise FormatoInvalidoException(f"El médico con matrícula {matricula} ya está registrado.")
        self.__medicos__[matricula] = medico

    # Gestión de Turnos.
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        """Agenda un turno para un paciente con un médico en una fecha específica."""
        if fecha_hora < datetime.now():
            raise FormatoInvalidoException("No se pueden agendar turnos en fechas pasadas.")
        if fecha_hora.hour < 8 or fecha_hora.hour >= 20:
            raise FormatoInvalidoException("Los turnos deben agendarse entre las 8:00 y las 20:00.")
        paciente = self.obtener_paciente_por_dni(dni)
        medico = self.obtener_medico_por_matricula(matricula)
        # Mapear días de la semana de inglés a español
        dias_ingles_a_espanol = {
            "monday": "lunes",
            "tuesday": "martes",
            "wednesday": "miércoles",
            "thursday": "jueves",
            "friday": "viernes",
            "saturday": "sábado",
            "sunday": "domingo"
        }
        dia_semana = dias_ingles_a_espanol.get(fecha_hora.strftime("%A").lower(), fecha_hora.strftime("%A").lower())
        if medico.obtener_especialidad_para_dia(dia_semana) != especialidad:
            raise MedicoNoDisponibleException(f"El médico no atiende {especialidad} los días {dia_semana}.")
        for turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("El médico ya tiene un turno asignado en esa fecha y hora.")
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    # Gestión de Recetas.
    def emitir_receta(self, dni: str, matricula: str, medicamentos: List[str]):
        """Emite una receta médica para un paciente."""
        paciente = self.obtener_paciente_por_dni(dni)
        medico = self.obtener_medico_por_matricula(matricula)
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    # Acceso a Información.
    def obtener_paciente_por_dni(self, dni: str) -> Paciente:
        """Devuelve un paciente dado su DNI."""
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException(f"No se encontró un paciente con DNI {dni}.")
        return self.__pacientes__[dni]

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        """Devuelve un médico dada su matrícula."""
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException(f"No se encontró un médico con matrícula {matricula}.")
        return self.__medicos__[matricula]

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        """Devuelve la historia clínica de un paciente."""
        if dni not in self.__historias_clinicas__:
            raise PacienteNoEncontradoException(f"No se encontró una historia clínica para el DNI {dni}.")
        return self.__historias_clinicas__[dni]

    def obtener_turnos(self) -> List[Turno]:
        """Devuelve una copia de la lista de turnos."""
        return self.__turnos__.copy()

    def obtener_pacientes(self) -> List[Paciente]:
        """Devuelve una copia de la lista de pacientes."""
        return list(self.__pacientes__.values())

    def obtener_medicos(self) -> List[Medico]:
        """Devuelve una copia de la lista de médicos."""
        return list(self.__medicos__.values())

### Fin de la definición de la clase Clinica.

#### Fin del código.