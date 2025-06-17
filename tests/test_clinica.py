"""
Computación I - Sistema de Gestión para una Clínica.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/tests/test_clinica.py".
"""

### Inicio del código.

## Inicio de Imports.

import unittest
from datetime import datetime, timedelta

from src.clinica import Clinica
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad
from src.modelo.turno import Turno
from src.modelo.receta import Receta
from src.modelo.historiaclinica import HistoriaClinica
from src.modelo.excepciones import (
    FormatoInvalidoException,
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
)

## Fin de Imports.

## Inicio de la definición de la clase TestClinica para las pruebas unitarias.

class TestClinica(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dr Ana Lopez", "M123")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.fecha_futura = datetime.now() + timedelta(days=1)
        self.fecha_futura = self.fecha_futura.replace(hour=10, minute=0, second=0, microsecond=0)

    # Pruebas para Paciente
    def test_registro_paciente_exitoso(self):
        """Verifica que un paciente se registre correctamente."""
        self.clinica.agregar_paciente(self.paciente)
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "12345678")

    def test_paciente_duplicado(self):
        """Verifica que no se pueda registrar un paciente con DNI duplicado."""
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(FormatoInvalidoException):
            self.clinica.agregar_paciente(self.paciente)

    def test_paciente_datos_invalidos(self):
        """Verifica que se lancen errores por datos inválidos."""
        with self.assertRaises(FormatoInvalidoException):
            Paciente("", "12345678", "01/01/1990")  # Nombre vacío
        with self.assertRaises(FormatoInvalidoException):
            Paciente("Juan123", "12345678", "01/01/1990")  # Nombre inválido
        with self.assertRaises(FormatoInvalidoException):
            Paciente("Juan Perez", "123", "01/01/1990")  # DNI inválido
        with self.assertRaises(FormatoInvalidoException):
            Paciente("Juan Perez", "12345678", "2023-01-01")  # Fecha inválida

    # Pruebas para Medico
    def test_registro_medico_exitoso(self):
        """Verifica que un médico se registre correctamente."""
        self.clinica.agregar_medico(self.medico)
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "M123")

    def test_medico_duplicado(self):
        """Verifica que no se pueda registrar un médico con matrícula duplicada."""
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(FormatoInvalidoException):
            self.clinica.agregar_medico(self.medico)

    def test_medico_datos_invalidos(self):
        """Verifica que se lancen errores por datos inválidos."""
        with self.assertRaises(FormatoInvalidoException):
            Medico("", "M123")  # Nombre vacío
        with self.assertRaises(FormatoInvalidoException):
            Medico("Ana123", "M123")  # Nombre inválido
        with self.assertRaises(FormatoInvalidoException):
            Medico("Dr Ana Lopez", "")  # Matrícula vacía

    # Pruebas para Especialidad
    def test_agregar_especialidad_exitoso(self):
        """Verifica que se pueda agregar una especialidad a un médico."""
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Cardiología")

    def test_especialidad_duplicada(self):
        """Verifica que no se pueda agregar una especialidad duplicada."""
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        with self.assertRaises(FormatoInvalidoException):
            self.medico.agregar_especialidad(self.especialidad)

    def test_dias_invalidos(self):
        """Verifica que se lance error por días inválidos."""
        with self.assertRaises(FormatoInvalidoException):
            Especialidad("Cardiología", ["invalidodia"])

    def test_agregar_especialidad_medico_no_registrado(self):
        """Verifica que no se pueda agregar especialidad a un médico no registrado."""
        clinica_vacia = Clinica()
        with self.assertRaises(MedicoNoDisponibleException):
            clinica_vacia.obtener_medico_por_matricula("M123")

    # Pruebas para Turno
    def test_agendar_turno_exitoso(self):
        """Verifica que se pueda agendar un turno válido."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agendar_turno("12345678", "M123", "Cardiología", self.fecha_futura)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_fecha_hora(), self.fecha_futura)

    def test_turno_duplicado(self):
        """Verifica que no se pueda agendar un turno duplicado."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agendar_turno("12345678", "M123", "Cardiología", self.fecha_futura)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M123", "Cardiología", self.fecha_futura)

    def test_turno_paciente_no_existe(self):
        """Verifica que se lance error si el paciente no existe."""
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "M123", "Cardiología", self.fecha_futura)

    def test_turno_medico_no_existe(self):
        """Verifica que se lance error si el médico no existe."""
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M999", "Cardiología", self.fecha_futura)

    def test_turno_especialidad_no_valida(self):
        """Verifica que se lance error si la especialidad no es atendida."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M123", "Pediatría", self.fecha_futura)

    def test_turno_dia_no_atendido(self):
        """Verifica que se lance error si el médico no atiende ese día."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        fecha_martes = self.fecha_futura + timedelta(days=1)  # Asegura que sea martes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M123", "Cardiología", fecha_martes)

    def test_turno_hora_no_laboral(self):
        """Verifica que se lance error por turno fuera de horario laboral."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        fecha_no_laboral = self.fecha_futura.replace(hour=23)
        with self.assertRaises(FormatoInvalidoException):
            self.clinica.agendar_turno("12345678", "M123", "Cardiología", fecha_no_laboral)

    def test_turno_fecha_pasada(self):
        """Verifica que se lance error por turno en fecha pasada."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        fecha_pasada = datetime.now() - timedelta(days=1)
        with self.assertRaises(FormatoInvalidoException):
            self.clinica.agendar_turno("12345678", "M123", "Cardiología", fecha_pasada)

    # Pruebas para Receta
    def test_emitir_receta_exitoso(self):
        """Verifica que se pueda emitir una receta válida."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.clinica.emitir_receta("12345678", "M123", ["Ibuprofeno", "Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIn("Ibuprofeno, Paracetamol", str(recetas[0]))  # Ajustado para nuevo formato de __str__

    def test_receta_paciente_no_existe(self):
        """Verifica que se lance error si el paciente no existe."""
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "M123", ["Ibuprofeno"])

    def test_receta_medico_no_existe(self):
        """Verifica que se lance error si el médico no existe."""
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("12345678", "M999", ["Ibuprofeno"])

    def test_receta_medicamentos_vacios(self):
        """Verifica que se lance error si no hay medicamentos."""
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [])

    def test_receta_medicamento_invalido(self):
        """Verifica que se lance error por medicamentos con caracteres no permitidos."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M123", ["Ibuprofeno!", "Paracetamol"])

    # Pruebas para Historia clínica
    def test_historia_clinica_registro_correcto(self):
        """Verifica que turnos y recetas se guarden en la historia clínica."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agendar_turno("12345678", "M123", "Cardiología", self.fecha_futura)
        self.clinica.emitir_receta("12345678", "M123", ["Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)
        self.assertIn("Cardiología", str(historia))
        self.assertIn("Ibuprofeno", str(historia))

    def test_flujo_completo(self):
        """Verifica un flujo completo: paciente, médico, especialidad, turno, receta, historia clínica."""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agendar_turno("12345678", "M123", "Cardiología", self.fecha_futura)
        self.clinica.emitir_receta("12345678", "M123", ["Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)
        self.assertIn("Cardiología", str(historia))
        self.assertIn("Ibuprofeno", str(historia))
    
## Inicio de la definición de la clase TestClinica para las pruebas unitarias.

if __name__ == "__main__":
    unittest.main()

### Fin del código