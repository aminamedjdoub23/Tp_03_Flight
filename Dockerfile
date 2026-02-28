# Utiliser une image Python officielle légère (version 3.10 recommandée pour la Data Science)
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du code de l'application
COPY . .

# Exposer le port de l'API FastAPI
EXPOSE 8000

# Commande par défaut au lancement du conteneur
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
