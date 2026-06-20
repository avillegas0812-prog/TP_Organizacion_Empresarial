# TP - Organización Empresarial

## Integrantes

- Ariel Villegas
- Marilyn Ruiz

## Descripción del Proyecto

Este proyecto consiste en el análisis y automatización del proceso de solicitud de vacaciones de los empleados mediante un chatbot desarrollado en Python.

El objetivo es mejorar la gestión administrativa, reducir tiempos de respuesta y minimizar errores en el procesamiento de solicitudes.

## Tecnologías Utilizadas

- Python 3
- GitHub
- Excel
- BPMN 2.0

## Estructura del Proyecto

```
TP_Organizacion_Empresarial/
│
├── bot_vacaciones.py
├── empleados.xlsx
├── README.md
└── capturas/
```

## Funcionalidades

- Validación de legajo.
- Consulta de días disponibles.
- Solicitud de vacaciones.
- Aprobación o rechazo automático.
- Simulación de chatbot mediante consola.
- Gestión de datos mediante archivo Excel.

## Base de Datos

La información de empleados se almacena en una planilla Excel que contiene:

- Número de legajo.
- Nombre del empleado.
- Días de vacaciones disponibles.

## Ejemplo de Uso


BOT DE GESTION DE VACACIONES

Ingrese su numero de legajo: 1001

Bienvenido Juan Perez
Dias disponibles: 15

Seleccione una opcion:
1 - Consultar dias disponibles
2 - Solicitar vacaciones

Opcion: 2

Ingrese la cantidad de dias solicitados: 5

Solicitud aprobada.
Dias restantes: 10
```

## Diagrama BPMN

El proceso fue modelado utilizando BPMN 2.0 contemplando:

- Usuario
- Sistema / Chatbot
- Validación de legajo
- Verificación de saldo disponible
- Aprobación o rechazo de la solicitud

## Herramientas de Inteligencia Artificial Utilizadas

Se utilizó ChatGPT como apoyo para:

- Diseño del proceso.
- Elaboración del modelo BPMN.
- Generación de documentación.
- Desarrollo del código base en Python.

## Repositorio

Este repositorio contiene todos los archivos requeridos para la entrega del Trabajo Práctico Integrador de Organización Empresarial.
