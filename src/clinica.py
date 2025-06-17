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
from typing import Optional, List

from src.modelo.excepciones import PacienteNoEncontradoException
from src.modelo.excepciones import MedicoNoDisponibleException
from src.modelo.excepciones import TurnoOcupadoException
from src.modelo.excepciones import FormatoInvalidoException
from src.modelo.historiaclinica import HistoriaClinica
from src.modelo.medico import Medico
from src.modelo.paciente import Paciente
from src.modelo.receta import Receta
from src.modelo.turno import Turno

### Fin de Imports.

### Inicio de la definición de la clase principal Clinica.

class Clinica:
    ## Atributos Privados
    def __init__(self):
        self.__pacientes__ = {}  # Mapea DNI del paciente a su objeto correspondiente.
        self.__medicos__ = {}  # Mapea matrícula de médico a su objeto correspondiente.
        self.__turnos__ = []  # Lista de todos los turnos agendados.
        self.__historias_clinicas__ = {}  # Mapea DNI a su historia clínica.

    ## Métodos
    # Registro y Acceso
    def agregar_paciente(self, paciente: Paciente):
        """Registra un paciente y crea su historia clínica."""
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise FormatoInvalidoException(f"El paciente con DNI {dni} ya está registrado.")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        """Registra un médico."""
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise FormatoInvalidoException(f"El médico con matrícula {matricula} ya está registrado.")
        self.__medicos__[matricula] = medico

    def obtener_pacientes(self) -> List[Paciente]:
        """Devuelve todos los pacientes registrados."""
        return list(self.__pacientes__.values())

    def obtener_medicos(self) -> List[Medico]:
        """Devuelve todos los médicos registrados."""
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        """Devuelve un médico por su matrícula."""
        self.validar_existencia_medico(matricula)
        return self.__medicos__[matricula]

    # Turnos
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        """Agenda un turno si se cumplen todas las condiciones."""
        if fecha_hora < datetime.now():
            raise FormatoInvalidoException("No se pueden agendar turnos en fechas pasadas.")
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.__medicos__[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        paciente = self.__pacientes__[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)

        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def obtener_turnos(self) -> List[Turno]:
        """Devuelve todos los turnos agendados."""
        return self.__turnos__.copy()

    # Recetas e Historias Clínicas
    def emitir_receta(self, dni: str, matricula: str, medicamentos: List[str]):
        """Emite una receta para un paciente."""
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        """Devuelve la historia clínica completa de un paciente."""
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas__[dni]

    # Validaciones y Utilidades
    def validar_existencia_paciente(self, dni: str):
        """Verifica si un paciente está registrado."""
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException(f"No se encontró el paciente con DNI: {dni}")

    def validar_existencia_medico(self, matricula: str):
        """Verifica si un médico está registrado."""
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException(f"No se encontró el médico con matrícula: {matricula}")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        """Verifica que no haya un turno duplicado."""
        for turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("Ya existe un turno para ese médico en la fecha y hora indicadas.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        """Traduce un objeto datetime al día de la semana en español."""
        dias = {0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves", 4: "viernes", 5: "sábado", 6: "domingo"}
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> Optional[str]:
        """Obtiene la especialidad disponible para un médico en un día."""
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        """Verifica que el médico atienda esa especialidad ese día."""
        especialidad_en_dia = self.obtener_especialidad_disponible(medico, dia_semana)
        if especialidad_en_dia is None:
            raise MedicoNoDisponibleException(f"El médico no atiende en {dia_semana}.")
        if especialidad_en_dia != especialidad_solicitada:
            raise MedicoNoDisponibleException(f"El médico no atiende la especialidad '{especialidad_solicitada}' en {dia_semana}.")

### Fin de la definición de la clase principal Clinica.

#### Fin del código.