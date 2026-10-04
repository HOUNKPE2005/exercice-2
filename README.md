# RodiumAI API – Exercice 2

Ce projet est un script Python interactif qui utilise directement l'API RodiumAI avec `requests` pour effectuer des générations de texte, d'images et de vidéos.
Il permet de naviguer entre les trois étapes, de rester sur une étape, de revenir en arrière ou de passer à la suivante.

## Installation

Le projet utilise **Python 3.12.10**.

Installer les dépendances avec :

```bash
pip install -r requirements.txt
```

## Configuration du `.env`

Copier le fichier `.env.example` vers `.env` :

```bash
cp .env.example .env
```

Puis ajouter votre clé API RodiumAI dans le fichier `.env` :

```env
RODIUMAI_API_KEY=votre_cle_api
```

Ne partagez jamais votre fichier `.env` et ne publiez pas votre clé API sur GitHub.

## Lancer le script

Exécuter la commande suivante :

```bash
python main.py
```

Le script propose trois étapes :

1. Chat conversationnel
2. Génération d'image
3. Génération de vidéo

Les commandes disponibles sont :

* `r` : rester sur l'étape actuelle
* `s` : passer à l'étape suivante
* `b` : revenir à l'étape précédente
* `q` : quitter le programme