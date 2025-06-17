"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/src/cli.py".
"""
### Inicio del código.

## Inicio de Imports.

import os
from datetime import datetime

from src.clinica import Clinica
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad
from src.modelo.excepciones import ClinicaException, FormatoInvalidoException

## Fin de Imports.

## Inicio de la definición de la clase CLI.

class CLI:
    """Clase que representa la interfaz de usuario por consola (Command Line Interface) para interactuar con el sistema de gestión de clínica."""
    """Su función es solicitar datos al usuario, invocar los métodos correspondientes de la clase principal "Clinica", capturar las excepciones personalizadas y mostrar mensajes claros y amigables."""

    # Método Constructor.
    def __init__(self):
        self.clinica = Clinica()  # Instancia principal del sistema de gestión.

    # Método para limpiar la pantalla.
    def _limpiar_pantalla(self):
        """Limpia la pantalla según el sistema operativo."""
        os.system("cls" if os.name == "nt" else "clear")

    # Método para validar entradas no vacías.
    def _validar_entrada_no_vacia(self, valor: str, campo: str) -> str:
        """Valida que la entrada no esté vacía. Lanza FormatoInvalidoException si lo está."""
        if not valor.strip():
            raise FormatoInvalidoException(f"El campo '{campo}' no puede estar vacío.")
        return valor.strip()

    # Método Principal.
    def iniciar(self):
        """Muestra un menú interactivo de forma continua hasta que el usuario elija salir. Cada opción llama a un método específico que realiza una operación sobre la clínica."""
        while True:
            self._limpiar_pantalla()  # Limpiar pantalla antes de mostrar el menú
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")

            opcion = input("Seleccione una opción: ").strip()

            try:
                if opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_turnos()
                elif opcion == "8":
                    self.ver_pacientes()
                elif opcion == "9":
                    self.ver_medicos()
                elif opcion == "0":
                    self._limpiar_pantalla()
                    print("Saliendo del sistema.")
                    break
                else:
                    print("Opción inválida. Por favor, elija una opción del 0 al 9.")
            except ClinicaException as e:
                print(f"[ERROR] {e}")
            input("Presione Enter para continuar...")  # Pausa para que el usuario vea el mensaje

    # Métodos privados de operaciones específicas.

    def agregar_paciente(self):
        """Solicita los datos de un paciente, crea el objeto correspondiente y lo registra en la clínica."""
        try:
            nombre = self._validar_entrada_no_vacia(input("Nombre completo: "), "nombre")
            dni = self._validar_entrada_no_vacia(input("DNI: "), "DNI")
            fecha = self._validar_entrada_no_vacia(input("Fecha de nacimiento (dd/mm/aaaa): "), "fecha de nacimiento")
            paciente = Paciente(nombre, dni, fecha)
            self.clinica.agregar_paciente(paciente)
            print("✅ Paciente registrado con éxito.")
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def agregar_medico(self):
        """Solicita los datos de un médico y lo registra en el sistema."""
        try:
            nombre = self._validar_entrada_no_vacia(input("Nombre completo del médico: "), "nombre")
            matricula = self._validar_entrada_no_vacia(input("Matrícula: "), "matrícula")
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print("✅ Médico registrado con éxito.")
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def agregar_especialidad(self):
        """Solicita una especialidad y sus días de atención, y la agrega a un médico ya registrado mediante su matrícula."""
        try:
            matricula = self._validar_entrada_no_vacia(input("Matrícula del médico: "), "matrícula")
            nombre_especialidad = self._validar_entrada_no_vacia(input("Nombre de la especialidad: "), "especialidad")
            dias = self._validar_entrada_no_vacia(input("Días de atención (separados por coma, en minúsculas): "), "días de atención")
            dias_lista = [d.strip() for d in dias.split(",") if d.strip()]
            if not dias_lista:
                raise FormatoInvalidoException("Debe especificar al menos un día de atención.")
            especialidad = Especialidad(nombre_especialidad, dias_lista)
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            medico.agregar_especialidad(especialidad)
            print("✅ Especialidad agregada al médico.")
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def agendar_turno(self):
        """Solicita los datos necesarios para agendar un turno, valida el formato de fecha y lo registra en el sistema si no hay conflictos."""
        try:
            dni = self._validar_entrada_no_vacia(input("DNI del paciente: "), "DNI")
            matricula = self._validar_entrada_no_vacia(input("Matrícula del médico: "), "matrícula")
            especialidad = self._validar_entrada_no_vacia(input("Especialidad: "), "especialidad")
            fecha_str = self._validar_entrada_no_vacia(input("Fecha y hora (dd/mm/aaaa HH:MM): "), "fecha y hora")
            try:
                fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            except ValueError:
                raise FormatoInvalidoException("Formato de fecha inválido. Use dd/mm/aaaa HH:MM.")
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("✅ Turno agendado con éxito.")
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def emitir_receta(self):
        """Solicita los datos para emitir una receta (paciente, médico y medicamentos) y la registra en la historia clínica del paciente."""
        try:
            dni = self._validar_entrada_no_vacia(input("DNI del paciente: "), "DNI")
            matricula = self._validar_entrada_no_vacia(input("Matrícula del médico: "), "matrícula")
            medicamentos = self._validar_entrada_no_vacia(input("Medicamentos (separados por coma): "), "medicamentos")
            lista = [m.strip() for m in medicamentos.split(",") if m.strip()]
            if not lista:
                raise FormatoInvalidoException("Debe especificar al menos un medicamento.")
            self.clinica.emitir_receta(dni, matricula, lista)
            print("✅ Receta emitida con éxito.")
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def ver_historia_clinica(self):
        """Muestra toda la historia clínica (turnos y recetas) de un paciente dado su DNI."""
        try:
            dni = self._validar_entrada_no_vacia(input("DNI del paciente: "), "DNI")
            historia = self.clinica.obtener_historia_clinica(dni)
            print(historia)
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def ver_turnos(self):
        """Muestra todos los turnos registrados en el sistema."""
        try:
            turnos = self.clinica.obtener_turnos()
            if not turnos:
                print("No hay turnos registrados.")
            else:
                for turno in turnos:
                    print(turno)
                    print("-" * 30)
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def ver_pacientes(self):
        """Muestra todos los pacientes registrados."""
        try:
            pacientes = self.clinica.obtener_pacientes()
            if not pacientes:
                print("No hay pacientes registrados.")
            else:
                for paciente in pacientes:
                    print(paciente)
        except ClinicaException as e:
            print(f"[ERROR] {e}")

    def ver_medicos(self):
        """Muestra todos los médicos registrados."""
        try:
            medicos = self.clinica.obtener_medicos()
            if not medicos:
                print("No hay médicos registrados.")
            else:
                for medico in medicos:
                    print(medico)
        except ClinicaException as e:
            print(f"[ERROR] {e}")

## Fin de la definición de la clase CLI.

### Fin del código.