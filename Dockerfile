# Dockerfile para el backend (FastAPI)
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente del backend
COPY app/ ./app

# Exponer el puerto (Render usará la variable de entorno PORT)
ENV PORT=8000
EXPOSE $PORT

# Comando para iniciar el backend
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT 