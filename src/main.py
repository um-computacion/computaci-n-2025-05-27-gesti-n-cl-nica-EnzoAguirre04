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

### Fin de la definición de las clases.

#### Fin del código.