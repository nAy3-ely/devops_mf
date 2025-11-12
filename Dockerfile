# IMAGEN BASE
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 80

# Ejecutar la aplicación
CMD ["python", "app.py"]
