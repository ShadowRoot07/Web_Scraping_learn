import requests
import urllib3

# Esto silencia las advertencias si usamos verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    print("Intentando conectar con la API...")
    # Agregamos verify=False por si tus certificados siguen fallando
    res = requests.get(url, headers=headers, verify=True, timeout=10)
    res.raise_for_status() # Lanza error si la respuesta es mala
    
    datos = res.json()
    print(f"¡Logrado! El Bitcoin está a: {datos['bpi']['USD']['rate']} USD")

except requests.exceptions.SSLError:
    print("Error de SSL detectado. Reintentando sin verificación...")
    res = requests.get(url, headers=headers, verify=False)
    print(f"Conectado (sin SSL): {res.json()['bpi']['USD']['rate']} USD")
except Exception as e:
    print(f"Hubo otro error: {e}")

