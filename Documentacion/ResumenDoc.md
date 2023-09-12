# API de Personas

La API de Personas ofrece una forma sencilla y efectiva de gestionar información sobre personas dentro de un entorno académico. Proporciona un conjunto de funciones para realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre entidades de personas.

En este documento se encuentra un resumen de la documentación de la API, para ver la documentación completa ir al siguiente enlace [Documentacion API Personas](https://documenter.getpostman.com/view/26000547/2s9YC2zZPZ)

## Base URL

`http://127.0.0.1:5000/`

## Endpoints

### Crear Persona

- **URL**: `/persons`
- **Método HTTP**: `POST`
- **Descripción**: Añade una nueva persona al sistema.

#### Parámetros del cuerpo de la solicitud (Request Body)

- `name`: Nombre de la persona.
- `lastName`: Apellido de la persona.
- `age`: Edad de la persona.
- `semester`: Semestre académico de la persona.
- `career`: Carrera académica de la persona.

---

### Obtener Personas

- **URL**: `/persons`
- **Método HTTP**: `GET`
- **Descripción**: Obtiene una lista de todas las personas en el sistema.

---

### Actualizar Persona

- **URL**: `/persons/<id>`
- **Método HTTP**: `PUT`
- **Descripción**: Actualiza la información de una persona existente.

---

### Eliminar Persona

- **URL**: `/persons/<id>`
- **Método HTTP**: `DELETE`
- **Descripción**: Elimina una persona del sistema.

---

### Obtener Persona por ID

- **URL**: `/persons/<id>`
- **Método HTTP**: `GET`
- **Descripción**: Obtiene la información de una persona específica por su ID.

---

### Obtener Personas por Semestre

- **URL**: `/persons/semester/<semester>`
- **Método HTTP**: `GET`
- **Descripción**: Obtiene la lista de personas en un semestre específico.

---

## Respuestas Comunes

- `200 OK`: La operación fue exitosa.
- `201 Created`: Se creó un nuevo recurso exitosamente.
- `400 Bad Request`: La solicitud tiene parámetros inválidos.
- `404 Not Found`: El recurso solicitado no se encuentra.
- `500 Internal Server Error`: Error interno del servidor.
