# Use an official Python runtime as a parent image
FROM python:3-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requis dans le conteneur
COPY backend/requirements.txt ./
COPY backend/main.py ./

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port sur lequel votre application Python s'exécute
EXPOSE 8000

# Démarre votre application Python
CMD ["python", "main.py"]