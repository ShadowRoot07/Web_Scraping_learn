import socket
import requests
import urllib3

# Silenciamos advertencias de certificados (ya que usaremos IPs directas)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def parche_dns_maestro():
    # Creamos un diccionario con las IPs de los sitios que usaremos
    MAPPING = {
        'api.coindesk.com': '184.72.104.138',
        'google.com': '142.250.64.206',
        'books.toscrape.com': '104.21.11.203' # IP aproximada de Cloudflare
    }
    
    old_getaddrinfo = socket.getaddrinfo

    def new_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        # Si el host está en nuestro mapa, usamos la IP directamente
        if host in MAPPING:
            return old_getaddrinfo(MAPPING[host], port, family, type, proto, flags)
        return old_getaddrinfo(host, port, family, type, proto, flags)
    
    socket.getaddrinfo = new_getaddrinfo

# --- Ejecución ---
parche_dns_maestro()

try:
    print("Probando conexión con el parche activo...")
    # Ahora puedes usar la URL normal, el parche se encarga del resto
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", verify=False, timeout=10)
    print(f"¡CONECTADO! Precio: {res.json()['bpi']['USD']['rate']} USD")
except Exception as e:
    print(f"Sigue fallando: {e}")

