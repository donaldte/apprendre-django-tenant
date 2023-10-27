# Utilisez une image de base avec Python pour l'application Django
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt et installez les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste du code dans le conteneur
COPY . .

# Exposez le port sur lequel l'application Django écoute
EXPOSE 8000

# Commande pour démarrer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
