# Évaluation Finale - Data Science avec Python : Projet de Prédiction de Prix de Vols

Ce dépôt rassemble notre travail pour l'évaluation finale.
Le but principal est d'analyser un dataset de vols indiens, de préparer les données, puis de construire un modèle prédictif (supervisé) et un modèle de segmentation (non supervisé).

**Problématique :** prédire le prix d'un vol en fonction de ses caractéristiques (durée, compagnie, escales, etc.) et segmenter les types de vols pour aider à mieux décider quand acheter un billet et limiter les coûts liés aux réservations de dernière minute.

### DATASET
Le dataset est disponible sur Kaggle : https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction

Il contient des informations sur des vols indiens : durée, compagnie aérienne, nombre d'escales, prix du billet, etc.

**Taille :** 300 153 lignes et 11 colonnes (features + cible).

### Colonnes

1) **Compagnie aérienne** : variable catégorielle (6 compagnies).
2) **Vol** : code de vol (catégorielle).
3) **Ville de départ** : variable catégorielle (6 villes).
4) **Heure de départ** : variable catégorielle dérivée (6 créneaux horaires).
5) **Escales** : variable catégorielle (3 valeurs distinctes).
6) **Heure d'arrivée** : variable catégorielle dérivée (6 créneaux horaires).
7) **Ville d'arrivée** : variable catégorielle (6 villes).
8) **Classe** : variable catégorielle (Business / Economy).
9) **Durée** : variable continue (durée totale du trajet en heures).
10) **Jours restants** : différence entre date de réservation et date du voyage.
11) **Prix** : variable cible.

## Ce qui a été fait

- **EDA & Preprocessing** : étude des données, gestion des valeurs manquantes, encodage et normalisation selon les besoins.
- **Modèle non supervisé (K-Means)** : segmentation des vols en profils types selon le prix et la durée.
- **Modèle supervisé (Random Forest)** : prédiction du prix des billets, export du modèle en `.pkl`.
- **API & interface web** : API FastAPI (`/predict`) + interface Streamlit pour tester les prédictions.

## Lancer le projet avec Docker

Un environnement Docker est fourni pour lancer le projet sans installer toutes les dépendances en local.

**Prérequis :** Docker Desktop installé.

### 1. Lancer les services (API + interface web)

Depuis la racine du projet, dans PowerShell ou CMD :

```bash
docker-compose up --build
```

### 2. Tester l'application

- Interface Streamlit : **http://127.0.0.1:8501**
- Documentation API FastAPI : **http://127.0.0.1:8000/docs**

Merci pour la lecture et la revue !