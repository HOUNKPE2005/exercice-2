# Import des bibliothèques nécessaires
import os
import base64
import requests
from dotenv import load_dotenv


# DEFINITION DES DIFFENTS MODELES A UTILISER POUR L'EXERCICE
CHAT_MODEL = "google/gemini-3.8-flash"
IMAGE_MODEL = "google/gemini-3.1-flash-lite-image"
VIDEO_MODEL = "openai/sora-2"

# chargement des variables d'environnements
load_dotenv()
API_KEY = os.getenv("RODIUMAI_API_KEY")
BASE_URL = "https://api.rodiumai.io/v1"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


# ETAPE 1 : LE CHAT CONVERSATIONNEL

def chat():

    question = input("Votre question : ")

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=HEADERS,
        json={
            "model": CHAT_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }
    )

    if response.status_code != 200:
        data = response.json()
        error = data.get("error", {})
        print(
            f"Erreur HTTP {response.status_code} | "
            f"error_code : {error.get('error_code', 'inconnu')} | "
            f"{error.get('message', 'Erreur inconnue')}"
        )
        return

    data = response.json()

    print("\nRéponse :")
    print(data["choices"][0]["message"]["content"])

    print(f"Coût : {data.get('cost_rodi', 'inconnu')} RODI")


# ÉTAPE 2 : IMAGE

def image():

    description = input("Décrivez l'image : ")

    response = requests.post(
        f"{BASE_URL}/images/generations",
        headers=HEADERS,
        json={
            "model": IMAGE_MODEL,
            "prompt": description,
            "n": 1,
            "size": "1024x1024",
            "quality": "medium"
        }
    )

    if response.status_code != 200:
        data = response.json()
        error = data.get("error", {})
        print(
            f"Erreur HTTP {response.status_code} | "
            f"error_code : {error.get('error_code', 'inconnu')} | "
            f"{error.get('message', 'Erreur inconnue')}"
        )
        return

    data = response.json()

    image_base64 = data["data"][0]["b64_json"]

    image = base64.b64decode(image_base64)

    with open("image.png", "wb") as fichier:
        fichier.write(image)

    print("Image enregistrée : image.png")


# ÉTAPE 3 : VIDÉO

def video():

    description = input("Décrivez la vidéo : ")

    response = requests.post(
        f"{BASE_URL}/videos/generations",
        headers=HEADERS,
        json={
            "model": VIDEO_MODEL,
            "prompt": description,
            "duration_seconds": 4,
            "aspect_ratio": "9:16"
        },
        timeout=150
    )

    if response.status_code != 200:
        data = response.json()
        error = data.get("error", {})
        print(
            f"Erreur HTTP {response.status_code} | "
            f"error_code : {error.get('error_code', 'inconnu')} | "
            f"{error.get('message', 'Erreur inconnue')}"
        )
        return

    data = response.json()

    video_url = data["data"][0]["url"]

    video = requests.get(video_url, timeout=150)

    with open("video.mp4", "wb") as fichier:
        fichier.write(video.content)

    print("Vidéo enregistrée : video.mp4")


# PROGRAMME PRINCIPAL

etapes = [chat, image, video]

position = 0

while True:

    print(f"\n=== Étape {position + 1} ===")

    etapes[position]()

    if position == 0:
        choix = input(
            "\nRester sur cette étape (r) ou passer à la suivante (s) ? "
        ).lower()

        if choix == "s":
            position = 1

    elif position == 1:
        choix = input(
            "\nRevenir en arrière (b), rester (r) ou passer à la suivante (s) ? "
        ).lower()

        if choix == "b":
            position = 0
        elif choix == "s":
            position = 2

    else:
        choix = input(
            "\nRevenir en arrière (b), rester (r) ou quitter (q) ? "
        ).lower()

        if choix == "b":
            position = 1
        elif choix == "q":
            print("Au revoir.")
            break