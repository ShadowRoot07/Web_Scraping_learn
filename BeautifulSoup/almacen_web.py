# Esto es lo que suele escupir un scraper profesional
inventario_web = [
    {"item": "Abono", "info": {"precio": 25, "stock": 5}},
    {"item": "Semillas", "info": {"precio": 10, "stock": 50}},
    {"item": "Pala", "info": {"precio": 45, "stock": 12}}
]

# Tu misión: Imprimir solo "Semillas" y "Pala" usando un ciclo 'for' e 'if'

for x in inventario_web:
    if x["item"] == "Semillas" or x["item"] == "Pala":
        print(x)
