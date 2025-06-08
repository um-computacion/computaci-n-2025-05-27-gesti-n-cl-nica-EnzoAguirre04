"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "/src/main.py".
"""

#### Inicio del código.

### Inicio de Imports.

from datetime import datetime
from typing import Optional

### Fin de Imports.

### Inicio de la definición de las clases.

class Paciente:  # Representa a un paciente de la clínica.
    ## Atributos Privados.
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre__ = nombre  # Nombre completo del paciente.
        self.__dni__ = dni  # DNI del paciente (identificador único).
        self.__fecha_nacimiento__ = fecha_nacimiento  # Fecha de nacimiento del paciente en formato dd/mm/aaaa.

    ## Métodos.
    # Acceso a Información.
    def obtener_dni(self) -> str:
        """Devuelve el DNI del paciente."""
        return self.__dni__

    # Representación.
    def __str__(self) -> str:
        """Representación en texto del paciente."""
        return f"Paciente: {self.__nombre__}, DNI: {self.__dni__}, Fecha de nacimiento: {self.__fecha_nacimiento__}"


class Especialidad:  # Representa una especialidad médica junto con los días de atención asociados.
    ## Atributos Privados.
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo__ = tipo  # Nombre de la especialidad (por ejemplo, "Pediatría", "Cardiología").
        self.__dias__ = [dia.lower() for dia in dias]  # Lista de días en los que se atiende esta especialidad, en minúsculas. | Uso lower() para que los días estén en minúsculas.

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


class Medico:  # Representa a un médico del sistema, con sus especialidades y matrícula profesional.
    ## Atributos Privados.
    def __init__(self, nombre: str, matricula: str):
        self.__nombre__ = nombre  # Nombre completo del médico.
        self.__matricula__ = matricula  # Matrícula profesional del médico (clave única).
        self.__especialidades__ = []  # Lista de especialidades con sus días de atención.

    ## Métodos.
    # Registro de Datos.
    def agregar_especialidad(self, especialidad: Especialidad):
        """Agrega una especialidad a la lista del médico."""
        self.__especialidades__.append(especialidad)

    # Acceso a Información.
    def obtener_matricula(self) -> str:
        """Devuelve la matrícula del médico."""
        return self.__matricula__

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        """Devuelve el nombre de la especialidad disponible en el día especificado, o None si no atiende ese día."""
        for esp in self.__especialidades__:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    # Representación.
    def __str__(self) -> str:
        """Representación legible del médico, incluyendo matrícula y especialidades."""
        especialidades_str = "\n  ".join(str(e) for e in self.__especialidades__) or "Sin especialidades"
        return f"Médico: {self.__nombre__}\nMatrícula: {self.__matricula__}\nEspecialidades:\n  {especialidades_str}"


class Turno:  # Representa un turno médico entre un paciente y un médico para una especialidad específica en una fecha y hora determinada.
    ## Atributos Privados.
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
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
            f"Turno:\n"
            f"  Paciente: {self.__paciente__.obtener_dni()} - {self.__paciente__}\n"
            f"  Médico: {self.__medico__.obtener_matricula()} - {self.__medico__}\n"
            f"  Especialidad: {self.__especialidad__}\n"
            f"  Fecha y hora: {fecha_formateada}"
        )


class Receta:  # Representa una receta médica emitida por un médico a un paciente, incluyendo los medicamentos recetados y la fecha de emisión.
    ## Atributos Privados.
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        self.__paciente__ = paciente  # Paciente al que se le emite la receta.
        self.__medico__ = medico  # Médico que emite la receta.
        self.__medicamentos__ = medicamentos  # Lista de medicamentos recetados.
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
    def obtener_turnos(self) -> list[Turno]:
        """Devuelve una copia de la lista de turnos del paciente."""
        return self.__turnos__.copy()

    def obtener_recetas(self) -> list[Receta]:
        """Devuelve una copia de la lista de recetas del paciente."""
        return self.__recetas__.copy()

    # Representación.
    def __str__(self) -> str:
        """Devuelve una representación textual de la historia clínica, incluyendo turnos y recetas."""
        turnos_str = "\n".join(str(t) for t in self.__turnos__) or "  Sin turnos registrados"
        recetas_str = "\n".join(str(r) for r in self.__recetas__) or "  Sin recetas registradas"
        return (
            f"Historia Clínica de {self.__paciente__}\n\n"
            f"Turnos:\n{turnos_str}\n\n"
            f"Recetas:\n{recetas_str}"
        )

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
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        """Registra un médico."""
        self.__medicos__[medico.obtener_matricula()] = medico

    def obtener_pacientes(self) -> list[Paciente]:
        """Devuelve todos los pacientes registrados."""
        return list(self.__pacientes__.values())

    def obtener_medicos(self) -> list[Medico]:
        """Devuelve todos los médicos registrados."""
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        """Devuelve un médico por su matrícula."""
        self.validar_existencia_medico(matricula)
        return self.__medicos__[matricula]

    # Turnos
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        """Agenda un turno si se cumplen todas las condiciones."""
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

    def obtener_turnos(self) -> list[Turno]:
        """Devuelve todos los turnos agendados."""
        return self.__turnos__.copy()

    # Recetas e Historias Clínicas
    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
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
            raise ValueError(f"No se encontró el paciente con DNI: {dni}")

    def validar_existencia_medico(self, matricula: str):
        """Verifica si un médico está registrado."""
        if matricula not in self.__medicos__:
            raise ValueError(f"No se encontró el médico con matrícula: {matricula}")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        """Verifica que no haya un turno duplicado."""
        for turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise ValueError("Ya existe un turno para ese médico en la fecha y hora indicadas.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        """Traduce un objeto datetime al día de la semana en español."""
        dias = {
            0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves",
            4: "viernes", 5: "sábado", 6: "domingo"
        }
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> Optional[str]:
        """Obtiene la especialidad disponible para un médico en un día."""
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        """Verifica que el médico atienda esa especialidad ese día."""
        especialidad_en_dia = self.obtener_especialidad_disponible(medico, dia_semana)
        if especialidad_en_dia is None:
            raise ValueError(f"El médico no atiende en {dia_semana}.")
        if especialidad_en_dia() != especialidad_solicitada:
            raise ValueError(f"El médico no atiende la especialidad '{especialidad_solicitada}' en {dia_semana}.")

### Fin de la definición de las clases.

#### Fin del código.