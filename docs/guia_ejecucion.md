# Guía de Ejecución del Sistema

Este documento explica cómo ejecutar el sistema de gestión para una clínica y cómo correr las pruebas unitarias.

## 👤 Información del Alumno:

### 📋 Datos Personales:
- **Nombre y Apellido**: Enzo Agustín Aguirre Polenta
- **Ciclo Lectivo**: 2025
- **Carrera**: Ingeniería en Informática

## Requisitos Previos:

- **Python 3.8 o superior** instalado.
- Sistema operativo: Windows, Linux, o macOS.
- Clonar o descargar el repositorio del proyecto:
  ```bash
  git clone git@github.com:um-computacion/computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04.git
  cd computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04
  ```

## Cómo Ejecutar el Sistema:

1. **Navegar al directorio raíz del proyecto**:
   ```bash
   cd computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04
   ```

2. **Ejecutar el programa principal**:
   ```bash
   python main.py
   ```

3. **Interacción con la CLI**:
   - Al ejecutar `main.py`, se muestra un menú interactivo:
     ```
     --- Menú Clínica ---
     1. Agregar paciente
     2. Agregar médico
     3. Agendar turno
     4. Agregar especialidad
     5. Emitir receta
     6. Ver historia clínica
     7. Ver todos los turnos
     8. Ver todos los pacientes
     9. Ver todos los médicos
     0. Salir

     ```
   - Seleccioná una opción ingresando un número (0-9) y seguí las instrucciones en pantalla.
   - Ejemplo: Para agregar un paciente, seleccioná `1`, luego ingresá nombre, DNI, y fecha de nacimiento.

## Cómo Ejecutar las Pruebas Unitarias:

1. **Navegar al directorio raíz del proyecto** (si no estás ya ahí):
   ```bash
   cd computaci-n-2025-05-27-gesti-n-cl-nica-EnzoAguirre04
   ```

2. **Ejecutar todas las pruebas**:
   ```bash
   python -m unittest discover tests
   ```

3. **Salida esperada**:
   - Si todas las pruebas pasan, verás algo como esto:
     ```
     ........................
     ----------------------------------------------------------------------
     Ran 25 tests in 0.008s
     OK
     ```
   - Si alguna prueba falla, se mostrará un traceback con detalles del error.

4. **Cobertura de las pruebas**:
   - Las pruebas en `tests/test_clinica.py` cubren:
     - Registro de pacientes y médicos.
     - Agendamiento de turnos.
     - Emisión de recetas.
     - Gestión de historias clínicas.
     - Validaciones de datos (nombres, DNI, horarios, etc.).
     - Casos de error (duplicados, datos inválidos, etc.).

## Notas:

- No se requieren dependencias externas; el sistema usa la biblioteca estándar de Python.
- Los datos se almacenan en memoria, por lo que se reinician al cerrar el programa.