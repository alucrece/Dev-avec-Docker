# Orchestration, Résilience et Industrialisation Docker

Ce projet consiste en une application conteneurisée complète suivant une architecture 3-tier. Elle permet d'afficher un dashboard d'étudiants avec un compteur de vues global et persistant.

## Installation et Lancement

1. **Cloner le projet** :
   ```bash
   git clone <URL_DU_DEPOT_ICI>
   cd <NOM_DU_DOSSIER>
2. **Configuration des secrets** : 
   Créez un fichier `.env` à la racine du projet. Ajoutez-y le contenu suivant en adaptant les valeurs si nécessaire :
   ```env
   POSTGRES_PASSWORD=votre_mot_de_passe
   POSTGRES_USER=votre_utilisateur
   POSTGRES_DB=votre_nom_de_db
3. Lancez la stack avec Docker Compose :

```bash
docker-compose up --build
````
L'application est accessible à l'adresse suivante : http://localhost:8080
