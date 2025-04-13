# Quantycs - Documentación de Configuración y Despliegue

## Índice
1. [Visión General](#visión-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Backend](#backend)
4. [Frontend](#frontend)
5. [Base de Datos](#base-de-datos)
6. [Despliegue](#despliegue)
7. [Estado Actual](#estado-actual)

## Visión General
Quantycs es una aplicación web que demuestra la integración entre un backend FastAPI, una base de datos PostgreSQL y un frontend web. La aplicación permite visualizar y gestionar datos de prueba en tiempo real.

## Estructura del Proyecto
```
quantycs/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── init_db.py
├── frontend/
├── Documentation/
├── requirements.txt
├── runtime.txt
├── render.yaml
├── package.json
└── index.html
```

## Backend

### Tecnologías Utilizadas
- FastAPI (v0.104.1)
- SQLAlchemy (v2.0.23)
- Uvicorn (v0.24.0)
- PostgreSQL (via psycopg2-binary v2.9.9)

### Características Implementadas
1. **API REST con FastAPI**
   - Endpoint `/`: Ruta de bienvenida
   - Endpoint `/test-data`: Obtiene datos de prueba de la base de datos

2. **Modelo de Datos**
   ```python
   class TestData(Base):
       __tablename__ = "test_data"
       id = Column(Integer, primary_key=True, index=True)
       name = Column(String, index=True)
       description = Column(String)
       value = Column(Integer)
   ```

3. **Configuración de CORS**
   - Permite solicitudes desde cualquier origen
   - Habilita todos los métodos HTTP
   - Permite todos los headers

## Frontend

### Tecnologías Utilizadas
- HTML5
- CSS3
- JavaScript (Vanilla)

### Características Implementadas
1. **Interfaz de Usuario**
   - Diseño responsive
   - Indicador de estado de conexión
   - Botón de recarga manual
   - Actualización automática cada 5 segundos

2. **Funcionalidades**
   - Conexión en tiempo real con el backend
   - Manejo de errores y estados de carga
   - Visualización de datos en formato de tarjetas
   - Indicador de estado de conexión (Connected/Disconnected)

## Base de Datos

### Configuración
- Tipo: PostgreSQL
- Hosting: Render (quantycs_db)
- Conexión: Mediante URL interna de Render
- Tablas:
  - `test_data`: Almacena los datos de prueba

### Datos de Prueba
Se han implementado 5 registros de prueba con:
- Nombre
- Descripción
- Valor numérico

## Despliegue

### Backend (quantycs-api)
- Plataforma: Render
- Tipo: Web Service
- URL: https://quantycs-api.onrender.com
- Configuración:
  ```yaml
  - type: web
    name: quantycs-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python3 -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

### Frontend (quantycs-frontend)
- Plataforma: Render
- Tipo: Static Site
- Configuración:
  ```yaml
  - type: static
    name: quantycs-frontend
    buildCommand: echo "No build required"
    staticPublishPath: .
  ```

## Estado Actual

### Funcionalidades Implementadas
- ✅ Conexión exitosa con la base de datos
- ✅ API REST funcionando
- ✅ Frontend desplegado y conectado
- ✅ Actualización automática de datos
- ✅ Manejo de errores
- ✅ Indicador de estado de conexión

### Próximos Pasos
1. Implementar operaciones CRUD completas
2. Agregar autenticación de usuarios
3. Mejorar la interfaz de usuario
4. Agregar filtros y búsqueda
5. Implementar visualizaciones de datos

### URLs Importantes
- Backend API: https://quantycs-api.onrender.com
- Frontend: [URL del frontend en Render]
- Repositorio: https://github.com/CMejiaVergel/Quantycs

## Notas Adicionales
- La aplicación está configurada para desarrollo y producción
- Se utiliza la URL interna de la base de datos para mejor rendimiento
- El frontend se actualiza automáticamente cada 5 segundos
- Todos los componentes están versionados en Git 