# ?? Review Coupon Webhook Server

Flask server, kter� propojuje Shopify, Klaviyo a z�kaznick� recenze.  
Automaticky p�id� tag z�kazn�kovi v Shopify a vytvo�� jednor�zov� slevov� kup�n po recenzi produktu.

---

## ?? Funkce

- Ov���, jestli z�kazn�k u� recenzoval konkr�tn� produkt
- P�id� tag `review_PRODUCTID` do z�kaznick�ho profilu v Shopify
- Vytvo�� 5% slevu na dan� produkt, platnou jen pro tohoto z�kazn�ka a jen 1�
- Ulo�� slevov� k�d do profilu z�kazn�ka v Klaviyo (`last_review_coupon`)

---

## ?? Instalace (lok�ln�)

```bash
git clone https://github.com/tvojeorg/review-coupon-server.git
cd review-coupon-server

# Vytvo� si .env soubor
cp .env.example .env

# Dopl� API kl��e a Shopify store URL do .env

# Instalace z�vislost�
pip install -r requirements.txt

# Spu�t�n� serveru
flask run --host=0.0.0.0 --port=5000
