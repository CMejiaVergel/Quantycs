# Quantycs - Sistema de Gestión de Inventario

## Descripción
Quantycs es un sistema de gestión de inventario desarrollado con FastAPI (backend) y React (frontend). El sistema permite gestionar productos, categorías, proveedores y realizar operaciones de inventario.

## Características
- Gestión de productos y categorías
- Control de inventario
- Gestión de proveedores
- Interfaz de usuario moderna y responsiva
- API RESTful
- Dockerización para fácil despliegue

## Requisitos Previos
- Python 3.8+
- Node.js 16+
- Docker y Docker Compose (opcional)

## Instalación

### Método 1: Instalación Local

#### Backend
1. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
.\venv\Scripts\activate  # En Windows
```

2. Instalar dependencias:
```bash
cd backend
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

4. Iniciar el servidor:
```bash
uvicorn app.main:app --reload
```

#### Frontend
1. Instalar dependencias:
```bash
cd frontend
npm install
```

2. Iniciar el servidor de desarrollo:
```bash
npm run dev
```

### Método 2: Usando Docker

1. Construir las imágenes:
```bash
docker build -t quantycs-backend -f Dockerfile.backend .
docker build -t quantycs-frontend -f Dockerfile.frontend .
```

2. Iniciar los contenedores:
```bash
docker run -p 8000:8000 quantycs-backend
docker run -p 3000:3000 quantycs-frontend
```

## Estructura del Proyecto
```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
├── Dockerfile.backend
├── Dockerfile.frontend
└── README.md
```

## Contribución
1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abrir un Pull Request

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 