#!/bin/bash

# Script de restauración para la configuración de Render
echo "Iniciando restauración de la configuración de Render..."

# Restaurar configuración original de Render
cp render.config.yaml ../render.yaml
echo "✓ Configuración original de Render restaurada"

# Restaurar configuración de Docker
cp docker.config.yaml ../render.docker.yaml
echo "✓ Configuración de Docker restaurada"

# Restaurar Dockerfiles
echo "$(grep -A 1000 "dockerfile: |" docker.config.yaml | grep -v "dockerfile: |" | sed 's/^    //')" > ../Dockerfile.backend
echo "✓ Dockerfile.backend restaurado"

echo "$(grep -A 1000 "frontend:" -A 1000 docker.config.yaml | grep -A 1000 "dockerfile: |" | grep -v "dockerfile: |" | sed 's/^    //')" > ../Dockerfile.frontend
echo "✓ Dockerfile.frontend restaurado"

# Restaurar docker-compose
echo "$(grep -A 1000 "docker-compose: |" docker.config.yaml | grep -v "docker-compose: |" | sed 's/^    //')" > ../docker-compose.yml
echo "✓ docker-compose.yml restaurado"

echo "Restauración completada. Verifica los archivos en el directorio raíz." 