# Évaluation Finale - Data Science avec Python : Projet de Prédiction de Prix de Vols

Ce dépôt rassemble notre travail pour l'évaluation finale. Le but principal était d'analyser un dataset de vols indiens, de préparer les données, et de créer à la fois un modèle prédictif (Supervisé) et un modèle de segmentation (Non Supervisé).

## Ce qui a été fait
- **EDA & Preprocessing** : Étude des données, gestion des variables manquantes, normalisation. Un notebook complet contient nos déductions.
- **Modèle Non Supervisé (K-Means)** : On a utilisé cet algoritme pour découvrir 3 profils types de vols selon le prix et la durée. Utile pour segmenter les clients ! Lisez le `.ipynb` pour comprendre notre conclusion.
- **Modèle Supervisé (Random Forest)** : Modèle complet d'une précision de prédiction très correcte pour estimer les prix. Il a été mis en fichier `.pkl` à la fin.
- **API & Interface Web** : Un point d'entrée API (`/predict`) tournant avec FastAPI, couplé à une belle interface graphique dynamique développée avec **Streamlit** pour tester le modèle super facilement.

##  Lancer le projet entier avec Docker

On a implémenté un système sous Docker pour ne pas à avoir à installer localement toutes les librairies et être sûrs que ça tourne partout d'un seul clic. 

**Prérequis** : Avoir installé Docker Desktop.

**1. Lancer les serveurs (API + Interface Web) :**
Dans votre terminal (sous Windows PowerShell ou Cmd par exemple), à la racine du dossier, executez : 
```bash
docker-compose up --build
```
*Le serveur va télécharger l'environnement complet et lancer les deux applications en parallèle.*

**2. Tester le modèle visuellement !**
- Allez sur la page de l'Application Web Streamlit : **`http://127.0.0.1:8501`**
Sélectionnez votre ville, la durée du vol, etc. et cliquez sur Prédire pour voir la magie opérer !

*l'API pure tourne en background sur `http://127.0.0.1:8000/docs`).*

Merci pour la lecture et la revue !