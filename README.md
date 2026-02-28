# Évaluation Finale - Data Science avec Python : Projet de Prédiction de Prix de Vols

Ce dépôt rassemble notre travail pour l'évaluation finale. Le but principal était d'analyser un dataset de vols indiens, de préparer les données, et de créer à la fois un modèle prédictif (Supervisé) et un modèle de segmentation (Non Supervisé).
Probematique : predire le prix d'un vol en fonction de ses caractéristiques (durée, compagnie, etc.) et segmenter les types de vols selon leurs caractéristiques pour des compagnie qui souhaitent trouver quand acheter leur billets des vols et reduire les couts liés à l'achat du dernier minute.

## Dataset
Le dataset utilisé est un ensemble de données de vols indiens disponible sur Kaggle : https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction, et comprenant des informations telles que la durée du vol, la compagnie aérienne, le nombre d'escales, et le prix du billet.
Total données : 
    300153 lignes et 11 colonnes (features).
    
Colonnes : 
1) Compagnie aérienne : Le nom de la compagnie aérienne est stocké dans la colonne correspondante. Il s'agit d'une variable catégorielle qui comprend 6 compagnies aériennes différentes.

2) Vol : La variable « Vol » contient le code de vol de l'avion. Il s'agit d'une variable catégorielle.

3) Ville de départ : Ville de départ du vol. Il s'agit d'une variable catégorielle qui comprend 6 villes uniques.

4) Heure de départ : Cette variable catégorielle dérivée est obtenue en regroupant les périodes de temps en intervalles. Elle stocke l'heure de départ et comprend 6 étiquettes horaires uniques.

5) Escales : Cette variable catégorielle à 3 valeurs distinctes stocke le nombre d'escales entre les villes de départ et d'arrivée.

6) Heure d'arrivée : Cette variable catégorielle dérivée est créée en regroupant les intervalles de temps. Elle comprend six étiquettes horaires distinctes et contient l'heure d'arrivée.

7) Ville d'arrivée : Ville où le vol atterrira. Il s'agit d'une variable catégorielle qui comprend 6 villes uniques.

8) Classe : Cette variable catégorielle contient des informations sur la classe de siège. Elle comporte deux valeurs distinctes : Affaires et Économie.

9) Durée : Variable continue affichant la durée totale du trajet entre les villes, en heures.

10) Jours restants : Caractéristique dérivée calculée en soustrayant la date de réservation de la date du voyage.

11) Prix : Variable cible contenant le prix du billet.

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