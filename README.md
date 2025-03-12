IP Logger - Webhook Discord
Ce projet est un script Python qui enregistre les adresses IP et les informations de l'agent utilisateur (User-Agent) des visiteurs d'une application ou d'un site web. Lorsque ces informations sont collectées, elles sont envoyées à un webhook Discord pour permettre à l'administrateur de suivre les connexions en temps réel.

Fonctionnalités
Enregistrement de l'IP et de l'User-Agent : Le script extrait l'adresse IP de l'utilisateur ainsi que son User-Agent depuis l'en-tête de la requête HTTP.
Envoi à un Webhook Discord : Les informations collectées sont envoyées à un canal Discord via un webhook pour un suivi facile.
Réponse HTTP : Le script renvoie une réponse JSON pour informer l'utilisateur que l'IP a bien été enregistrée.
Prérequis
Avant d'utiliser ce script, assurez-vous d'avoir installé les dépendances nécessaires :

Python 3.7 ou supérieur
La bibliothèque requests pour envoyer des requêtes HTTP à Discord.
Installation
Clonez le projet ou téléchargez-le dans le répertoire de votre choix :

bash
Copier
Modifier
git clone https://github.com/ton-utilisateur/ton-projet.git
Installez les dépendances : Assurez-vous d'avoir un environnement Python avec la bibliothèque requests installée. Utilisez pip pour installer les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
Configuration du webhook Discord :

Créez un webhook dans le canal Discord où vous souhaitez recevoir les notifications (suivez ce guide Discord : Créer un Webhook).
Copiez l'URL du webhook et remplacez la valeur de WEBHOOK_URL dans le script avec votre propre URL.
python
Copier
Modifier
WEBHOOK_URL = "votre_url_de_webhook"
Comment ça marche
Fonction principale : Le script écoute les requêtes HTTP. Lorsqu'une requête est reçue, il récupère les informations suivantes :

L'adresse IP de l'utilisateur (en utilisant l'en-tête x-forwarded-for).
Le User-Agent de l'utilisateur (en utilisant l'en-tête user-agent).
Envoi à Discord : Les informations sont envoyées à un webhook Discord. Le message envoyé à Discord contient l'IP et l'User-Agent du client. Un exemple de message envoyé :

markdown
Copier
Modifier
**Nouvelle IP détectée !**
- **IP**: xxx.xxx.x.x
- **User-Agent**: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Réponse HTTP : Une fois que l'IP et l'User-Agent sont envoyés à Discord, une réponse JSON est envoyée au client pour indiquer que l'IP a bien été enregistrée :

json
Copier
Modifier
{
  "message": "IP logged successfully."
}
Gestion des erreurs : Si une erreur se produit, comme un problème avec le webhook, une réponse d'erreur est renvoyée et un message d'erreur est également envoyé à Discord.

Exemple d'utilisation
Pour tester ce script localement, vous pouvez exécuter un serveur Python avec Flask ou FastAPI, ou l'utiliser sur des plateformes comme Vercel pour déployer la fonction en ligne.

Exemple avec FastAPI (Local) :
python
Copier
Modifier
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

WEBHOOK_URL = "votre_url_de_webhook"

@app.post("/log-ip")
async def log_ip(request: Request):
    headers = request.headers
    client_ip = headers.get('x-forwarded-for', 'IP not found')
    user_agent = headers.get('user-agent', 'User-Agent not found')

    requests.post(WEBHOOK_URL, json={
        "username": "IP Logger",
        "content": f"**Nouvelle IP détectée !**\n- **IP:** {client_ip}\n- **User-Agent:** {user_agent}"
    })

    return {"message": "IP logged successfully."}
Exemple avec Vercel (Serveurless) :
Déployez sur Vercel en suivant les étapes décrites précédemment.
La fonction s'exécutera à chaque fois qu'une requête HTTP sera envoyée à l'URL de votre fonction déployée.
Structure du projet
Voici la structure du projet recommandée pour une utilisation avec Vercel :

bash
Copier
Modifier
├── api
│   └── handler.py           # Script Python avec la logique du logger
├── requirements.txt         # Liste des dépendances Python
└── vercel.json              # Configuration pour déployer sur Vercel
Fichier requirements.txt
Ce fichier contient la liste des bibliothèques Python nécessaires à l'exécution du script.

nginx
Copier
Modifier
requests
Déploiement sur Vercel
Créez un compte sur Vercel.

Connectez votre projet à Vercel en utilisant la commande suivante dans votre terminal :

bash
Copier
Modifier
vercel
Déployez le projet :

bash
Copier
Modifier
vercel --prod
Le webhook sera automatiquement appelé à chaque fois qu'une requête HTTP est envoyée à l'URL de votre fonction Vercel.

Notes
Ce script ne gère pas le cas où plusieurs adresses IP sont envoyées dans l'en-tête x-forwarded-for. Il ne prend que la première adresse IP de la liste.
Le script est principalement conçu pour une utilisation en tant que fonction serverless sur des plateformes comme Vercel. Il peut être utilisé sur d'autres plateformes serverless, mais la configuration du déploiement peut différer.
