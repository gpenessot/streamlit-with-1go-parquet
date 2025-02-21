# Streamlit with 1Go Parquet

Ce dépôt propose une application Streamlit simple qui lit un fichier Parquet d'environ 1 Go en utilisant Polars pour un traitement performant des gros datasets.

## Prérequis

- Python 3.11 (ou supérieur)
- [uv](https://github.com/pdm-project/uv) pour la gestion de l'environnement virtuel et des dépendances
- Streamlit
- Polars

## Installation

1. Clonez le dépôt et accédez au dossier du projet :
   ```bash
   git clone <URL_DU_DEPOT>
   cd streamlit-with-1go-parquet
   ```

2. Créez votre environnement virtuel et installez les dépendances (toutes définies dans le fichier `pyproject.toml`) :
   ```bash
   uv init
   uv sync
   ```

## Génération du dataset

Le script `generate_dataset.py` génère un dataset fictif d'environ 1 Go au format Parquet (compression "uncompressed").

Exécutez :
```bash
python generate_dataset.py
```
Le fichier généré s'appelle `dataset_1GB.parquet`.

## Lancement de l'application Streamlit

Pour démarrer l'application, lancez la commande suivante :
```bash
streamlit run app.py
```
L'application lira le fichier Parquet généré et affichera un aperçu des données.

## Remarques

- Polars offre une lecture rapide des fichiers Parquet comparée à Pandas.
- L'utilisation de uv avec un fichier `pyproject.toml` simplifie la gestion de l'environnement et des dépendances.

## License

Ce projet est sous licence [MIT](LICENSE).