# ?? Review Coupon Webhook Server

Flask server, který propojuje Shopify, Klaviyo a zákaznické recenze.  
Automaticky přidá tag zákazníkovi v Shopify a vytvoří jednorázový slevový kupón po recenzi produktu.

---

## ?? Funkce

- Ověří, jestli zákazník už recenzoval konkrétní produkt
- Přidá tag `review_PRODUCTID` do zákaznického profilu v Shopify
- Vytvoří 5% slevu na daný produkt, platnou jen pro tohoto zákazníka a jen 1×
- Uloží slevový kód do profilu zákazníka v Klaviyo (`last_review_coupon`)

---

## ?? Instalace (lokálně)

```bash
git clone https://github.com/tvojeorg/review-coupon-server.git
cd review-coupon-server

# Vytvoř si .env soubor
cp .env.example .env

# Doplň API klíče a Shopify store URL do .env

# Instalace závislostí
pip install -r requirements.txt

# Spuštění serveru
flask run --host=0.0.0.0 --port=5000
