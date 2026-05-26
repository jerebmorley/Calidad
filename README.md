# Calculadora CI

Proyecto académico para construir un entorno de Integración Continua.

## Tecnologías utilizadas

- Python
- Flask
- pytest
- Git
- GitHub
- GitHub Actions
- Render
- Slack

## Ejecutar el proyecto localmente

Crear y activar entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate

## Health check

El endpoint `/health` permite verificar si la aplicación está disponible.

Ejemplo:

```bash
curl http://127.0.0.1:5000/health