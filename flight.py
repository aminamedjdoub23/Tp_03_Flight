import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   

df = pd.read_csv("Clean_Dataset.csv")
df = pd.read_csv("economy.csv")
df = pd.read_csv("business.csv")


df = df.drop(df.columns[0], axis=1)  # ne contient que des Id inutiles
df = df.drop(df.columns[1], axis=1)  # supprime la colonne flight qui est inutile

print(df.sample(10)) # affiche 10 lignes aléatoires

print(df.isnull().sum()) # affiche le nombre de valeurs manquantes par colonne

print(df.duplicated().sum()) 
print("il y a", df.duplicated().sum(), "doublons") # affiche le nombre de doublons
df.drop_duplicates(inplace=True)


print(df.shape) # affiche le nombre de lignes et de colonnes

print(df.columns) # affiche les noms des colonnes


# montre toutes les villes sources et destinations et les informations sur les vols
print("les villes sources sont :",df['source_city'].unique())
print("les villes destinations sont :",df['destination_city'].unique())

#affiche les differentes airlines et les infos sur les vols
print("les airlines sont :",df['airline'].unique()) 
print( "les informations sur les vols sont :",df['airline'].value_counts())
df = df.drop(df.columns[2], axis=1)  # les compagnies ne sont pas utiles pour le modéle

#affiche les differentes classes et les infos sur les vols
print("les classes sont :",df['class'].unique()) 
print( "les informations sur les vols sont :",df['class'].value_counts())
