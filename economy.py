import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   

df = pd.read_csv("economy.csv")


df.drop(['date'], axis=1, inplace=True)  # n'est pas utile
df.drop(['ch_code', 'num_code'], axis=1, inplace=True)  # supprime les codes de vols qui sont inutiles

print(df.sample(10)) # affiche 10 lignes aléatoires

print(df.isnull().sum()) # affiche le nombre de valeurs manquantes par colonne

print(df.duplicated().sum()) 
print("il y a", df.duplicated().sum(), "doublons") # affiche le nombre de doublons
df.drop_duplicates(inplace=True)


print(df.shape) # affiche le nombre de lignes et de colonnes

print(df.columns) # affiche les noms des colonnes


# montre toutes les villes sources et destinations et les informations sur les vols
print("les villes sources sont :",df['from'].unique())
print("les villes destinations sont :",df['to'].unique())

#affiche les differentes airlines et les infos sur les vols
print("les airlines sont :",df['airline'].unique()) 
print( "les informations sur les vols sont :",df['airline'].value_counts())
df.drop(['airline'], axis=1, inplace=True)  # les compagnies ne sont pas utiles pour le modéle

# Les donnees sont uniquement pour la classe economy
print("Toutes les donnees concernent la classe Economy")
