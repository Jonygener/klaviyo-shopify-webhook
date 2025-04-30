# ?? Review Coupon Webhook Server

Flask server, který propojuje Shopify, Klaviyo a zákaznické recenze.  
Automaticky pøidá tag zákazníkovi v Shopify a vytvoøí jednorázový slevový kupón po recenzi produktu.

---

## ?? Funkce

- Ovìøí, jestli zákazník už recenzoval konkrétní produkt
- Pøidá tag `review_PRODUCTID` do zákaznického profilu v Shopify
- Vytvoøí 5% slevu na daný produkt, platnou jen pro tohoto zákazníka a jen 1×
- Uloží slevový kód do profilu zákazníka v Klaviyo (`last_review_coupon`)

---

## ?? Instalace (lokálnì)

```bash
git clone https://github.com/tvojeorg/review-coupon-server.git
cd review-coupon-server

# Vytvoø si .env soubor
cp .env.example .env

# Doplò API klíèe a Shopify store URL do .env

# Instalace závislostí
pip install -r requirements.txt

# Spuštìní serveru
flask run --host=0.0.0.0 --port=5000
