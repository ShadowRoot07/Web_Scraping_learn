from bs4 import BeautifulSoup
import csv

# 1. El HTML "sucio" que simula lo que obtendríamos con requests
html_sucio = """
<div class="producto">
    <h2 class="nombre">   Semillas de Tomate Cherry   </h2>
    <p class="precio">Precio: $12.50 USD</p>
    <span class="stock">Disponibilidad: 45 unidades en bodega</span>
</div>
<div class="producto">
    <h2 class="nombre"> Fertilizante Potasio+ </h2>
    <p class="precio">Precio: $30.00 USD</p>
    <span class="stock">Disponibilidad: AGOTADO</span>
</div>
"""

soup = BeautifulSoup(html_sucio, 'html.parser')
productos = soup.find_all('div', class_='producto')

# 2. Preparar el CSV
with open("inventario_limpio.csv", "w", newline='', encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(['Producto', 'Precio_Float', 'Stock_Int'])

    for p in productos:
        # --- LIMPIEZA DEL NOMBRE ---
        # .strip() elimina los espacios vacíos al inicio y al final
        nombre = p.find('h2').text.strip()

        # --- LIMPIEZA DEL PRECIO ---
        # Queremos solo el número (12.50) como float para poder hacer cálculos
        precio_raw = p.find('p', class_='precio').text
        # Reemplazamos lo que no queremos y limpiamos
        precio_limpio = precio_raw.replace('Precio: $', '').replace(' USD', '').strip()
        precio_final = float(precio_limpio)

        # --- LIMPIEZA DEL STOCK ---
        # Aquí la cosa se pone interesante. Queremos el número 45 o 0 si está agotado.
        stock_raw = p.find('span', class_='stock').text
        
        if "AGOTADO" in stock_raw:
            stock_final = 0
        else:
            # Extraemos solo los dígitos
            # '45 unidades...' -> nos quedamos con '45'
            stock_final = int(''.join(filter(str.isdigit, stock_raw)))

        # 3. Guardar los datos ya procesados
        print(f"Procesado: {nombre} | {precio_final} | {stock_final}")
        escritor.writerow([nombre, precio_final, stock_final])

print("\n¡Archivo CSV generado con datos listos para una base de datos!")

