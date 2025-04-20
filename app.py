from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import requests

# Načti proměnné z .env souboru
load_dotenv()

SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")  # Např. "mojefirma.myshopify.com"

app = Flask(__name__)

@app.route('/klaviyo-webhook', methods=['POST'])
def klaviyo_webhook():
    data = request.get_json()
    email = data.get('email')
    tag = data.get('tag')

    # Najdi zákazníka podle e-mailu
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    search_url = f"https://{SHOPIFY_STORE_URL}/admin/api/2023-10/customers/search.json?query=email:{email}"
    response = requests.get(search_url, headers=headers)
    customers = response.json().get('customers', [])

    if not customers:
        return jsonify({"error": "Zákazník nenalezen"}), 404

    customer_id = customers[0]['id']
    existing_tags = customers[0]['tags']
    all_tags = existing_tags.split(', ') if existing_tags else []
    
    if tag not in all_tags:
        all_tags.append(tag)

    # Aktualizuj zákazníka s novými tagy
    update_url = f"https://{SHOPIFY_STORE_URL}/admin/api/2023-10/customers/{customer_id}.json"
    payload = {
        "customer": {
            "id": customer_id,
            "tags": ", ".join(all_tags)
        }
    }
    update_response = requests.put(update_url, json=payload, headers=headers)
    return jsonify(update_response.json()), update_response.status_code

if __name__ == '__main__':
    app.run(debug=True)
