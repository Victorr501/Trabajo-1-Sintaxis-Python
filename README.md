# Calculadora de Promedios Escolares

Un script interactivo en Python diseñado para gestionar materias y calificaciones escolares mediante la consola. Permite registrar asignaturas, validar notas, calcular el promedio general, filtrar materias aprobadas o reprobadas y encontrar las calificaciones extremas (máxima y mínima).

## 🚀 Características

- **Entrada interactiva:** Registro dinámico de asignaturas y calificaciones.
- **Validación robusta:** Control de errores para evitar ingresos no numéricos y restricción de calificaciones al rango de 0 a 10.
- **Manejo de estructuras de datos:** Uso óptimo de listas paralelas para el almacenamiento y sincronización de datos sin recurrir a Programación Orientada a Objetos (POO).
- **Análisis estadístico básico:**
  - Cálculo automático del promedio general.
  - Clasificación de materias (Aprobadas / Reprobadas) según un umbral personalizable (por defecto 5.0).
  - Identificación exacta de las materias con la calificación más alta y más baja.
- **Control de excepciones:** Manejo adecuado para casos en los que no se registren materias.

## 🛠️ Requisitos

- Python 3.x instalado en el sistema.

## 📁 Estructura del Código

El archivo principal `calculadora_promedios.py` contiene las siguientes funciones modulares:

1. `ingresar_calificaciones()`: Captura los nombres de las materias y sus notas. Implementa bucles de validación y retorna dos listas sincronizadas.
2. `calcular_promedio(calificaciones)`: Recibe la lista de notas y devuelve la media aritmética. Cuenta con protección contra listas vacías.
3. `determinar_estado(calificaciones, umbral=5.0)`: Clasifica las materias utilizando *list comprehensions* y devuelve listas con los índices correspondientes.
4. `encontrar_extremos(calificaciones)`: Encuentra las posiciones del valor máximo y mínimo en la lista para mapearlos con sus respectivos nombres.
5. `main()`: Orquesta la ejecución del programa, gestiona el flujo principal y da formato al resumen final expuesto al usuario.

## 💻 Instrucciones de Uso

1. Descarga o clona el archivo `calculadora_promedios.py` en tu equipo.
2. Abre una terminal o línea de comandos en la carpeta donde se encuentra el archivo.
3. Ejecuta el programa con el siguiente comando:
   ```bash
   python calculadora_promedios.py