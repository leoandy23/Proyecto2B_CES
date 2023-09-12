# Guía para la Creación de la API de Personas

## Descripción General

Este documento proporciona una guía detallada para desarrollar una API de personas utilizando Flask y Firebase. Esta API permitirá las siguientes operaciones:

- Crear una persona
- Obtener todas las personas
- Actualizar una persona
- Eliminar una persona
- Obtener una persona por ID
- Filtrar personas por semestre

## Pre-requisitos

- Python 3.x instalado
- Acceso a una base de datos Firebase
- Entorno virtual de Python (Opcional pero recomendado)

## Instalación de Dependencias

### Paso 1: Crear un Entorno Virtual (Opcional pero Recomendado)

Crear un entorno virtual es una buena práctica para aislar las dependencias del proyecto. Para crear uno, ejecute el siguiente comando en la raíz de su proyecto:

```bash
python -m venv venv
```

Para activar el entorno virtual:

- En Windows:

  ```bash
  .\venv\Scripts\Activate
  ```

- En macOS y Linux:

  ```bash
  source venv/bin/activate
  ```

### Paso 2: Instalar Dependencias

Una vez que el entorno virtual está activado (o si eliges no usar uno), puedes instalar las dependencias requeridas.

Ejecute el siguiente comando para instalar las bibliotecas necesarias:

```bash
pip install Flask firebase_admin
```

Esto instalará Flask, que es un micro marco web para Python, y `firebase_admin`, que es el SDK de administrador de Firebase que te permitirá interactuar con la base de datos Firestore.

### Paso 3: Verificar la Instalación

Para asegurarte de que todas las dependencias se han instalado correctamente, puedes ejecutar el siguiente comando:

```bash
pip freeze
```

Este comando mostrará una lista de todas las bibliotecas instaladas. Asegúrate de que `Flask` y `firebase_admin` aparezcan en la lista.

### Paso 4: Credenciales de Firebase (Opcional)

Si aún no has descargado tu archivo de credenciales de Firebase, asegúrate de hacerlo desde la consola de Firebase y coloca el archivo JSON en un lugar seguro y accesible para tu aplicación.

## Desarrollo

Una vez que las dependencias están instaladas, puedes proceder con el desarrollo de la API. Aquí hay un resumen de los pasos a seguir:

1. Importar las bibliotecas necesarias.
2. Inicializar la aplicación Flask.
3. Conectar con Firebase.
4. Definir las rutas y funciones para manejar las peticiones.

## Pruebas

Realiza pruebas unitarias y funcionales para asegurarte de que la API funcione como se espera.

## Despliegue

Después de probar la API, puedes desplegarla en un servidor. Asegúrate de configurar las variables de entorno y las credenciales de Firebase según sea necesario.
