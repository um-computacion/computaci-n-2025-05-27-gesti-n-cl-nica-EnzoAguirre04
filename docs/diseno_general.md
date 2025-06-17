# Diseño General del Sistema

Este documento proporciona una explicación breve del diseño del sistema de gestión para una clínica y un diagrama de la estructura de archivos.

## 👤 Información del Alumno:

### 📋 Datos Personales:
- **Nombre y Apellido**: Enzo Agustín Aguirre Polenta
- **Ciclo Lectivo**: 2025
- **Carrera**: Ingeniería en Informática

## Explicación del Diseño:

El sistema es una aplicación en Python que permite gestionar una clínica médica. Los usuarios interactúan a través de una interfaz de línea de comandos (CLI) para realizar tareas como registrar pacientes, agendar turnos, emitir recetas, y consultar historias clínicas. El diseño es simple y modular, dividido en tres partes principales:

- **Datos (Modelo)**: Clases como `Paciente`, `Medico`, y `Turno` almacenan la información y validan datos (por ejemplo, nombres solo con letras, horarios entre 8:00 y 20:00). Estas clases están en la carpeta `src/modelo/`.
- **Lógica (Controlador)**: La clase `Clinica` coordina todo, conectando pacientes, médicos, turnos, y recetas. Está en `src/clinica.py`.
- **Interfaz (Vista)**: La CLI en `src/cli.py` muestra un menú fácil de usar y maneja los errores con mensajes claros, como `[INFO]` para éxito y `[ERROR]` para problemas.

Es importante aclarar que el sistema no guarda datos permanentemente (se reinician al cerrar).

## Diagrama de Archivos:

```
computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04/
│
├── src/                          # Código fuente del sistema
│   ├── __init__.py               # Para indicar que la carpeta es un paquete
│   ├── modelo/                   # Clases del modelo (datos y validaciones)
│   │   ├── __init__.py           # Para indicar que la carpeta es un paquete
│   │   ├── excepciones.py        # Excepciones personalizadas (FormatoInvalidoException, etc.)
│   │   ├── paciente.py           # Clase Paciente (nombre, DNI, fecha de nacimiento)
│   │   ├── medico.py             # Clase Medico (nombre, matrícula, especialidades)
│   │   ├── especialidad.py       # Clase Especialidad (tipo, días de atención)
│   │   ├── turno.py              # Clase Turno (paciente, médico, fecha, especialidad)
│   │   ├── receta.py             # Clase Receta (paciente, médico, medicamentos, fecha)
│   │   └── historiaclinica.py    # Clase HistoriaClinica (paciente, turnos, recetas)
│   │
│   ├── clinica.py                # Clase Clinica (controlador, gestiona la lógica)
│   ├── cli.py                    # Interfaz de línea de comandos (vista)
│   └── main.py                   # Punto de entrada del programa
│
├── tests/                        # Pruebas unitarias
│   └── __init__.py               # Para indicar que la carpeta es un paquete
│   └── test_clinica.py           # Pruebas para todas las funcionalidades
│
├── docs/                         # Documentación
│   ├── guia_ejecucion.md         # Instrucciones para ejecutar el sistema y pruebas
│   └── diseno_general.md         # Diseño general y diagrama de archivos
│
└── README.md                     # Información general del proyecto y la tarea
```