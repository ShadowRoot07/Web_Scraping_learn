from bs4 import BeautifulSoup
import csv
import re # Expresiones regulares para limpieza avanzada

# 1. HTML con una tabla compleja y sucia
html_tabla = """
<table>
    <thead>
        <tr><th>Producto</th><th>Costo Unitario</th><th>Ultima Compra</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>   ABONO DE CRECIMIENTO - 5KG   </td>
            <td>$45,99</td>
            <td>05/Mar/2026</td>
        </tr>
        <tr>
            <td>pala de TRABAJO (reforzada)</td>
            <td>$120,00</td>
            <td>01/Feb/2026</td>
        </tr>
        <tr>
            <td>manguera RIEGO 20m</td>
            <td>$15,50</td>
            <td>20/Jan/2026</td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html_tabla, 'html.parser')
filas = soup.find('tbody').find_all('tr')

productos_limpios = []

for fila in filas:
    celdas = fila.find_all('td')
    
    # --- LIMPIEZA 1: El Nombre (Normalización) ---
    # Lo pasamos a minúsculas y luego ponemos la primera en mayúscula (capitalize)
    nombre_sucio = celdas[0].text.strip()
    nombre_limpio = nombre_sucio.lower().capitalize()
    
    # --- LIMPIEZA 2: El Precio (Conversión a Float) ---
    # El servidor nos da comas, pero Python/SQL necesitan puntos
    precio_raw = celdas[1].text
    precio_limpio = precio_raw.replace('$', '').replace(',', '.')
    precio_final = float(precio_limpio)
    
    # --- LIMPIEZA 3: La Fecha (Formato ISO para SQL) ---
    # '05/Mar/2026' -> '2026-03-05'
    fecha_raw = celdas[2].text
    partes = fecha_raw.split('/')
    meses = {'Jan': '01', 'Feb': '02', 'Mar': '03'} # Mapeo de meses
    fecha_iso = f"{partes[2]}-{meses[partes[1]]}-{partes[0].zfill(2)}"

    productos_limpios.append({
        "nombre": nombre_limpio,
        "precio": precio_final,
        "fecha": fecha_iso
    })

# Guardar en CSV simulando una tabla de base de datos
with open("suministros_ready.csv", "w", newline='') as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "fecha"])
    escritor.writeheader()
    escritor.writerows(productos_limpios)

print("¡Tabla procesada y normalizada con éxito!")

