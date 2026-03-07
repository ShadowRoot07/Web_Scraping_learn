def limpiar_quimico(texto_sucio):
    # 1. El primer gran corte: usamos '--' para separar en 3 pedazos
    # Partes resultantes: [">>> nitrógeno...", " VOLUMEN: 5...", " PUREZA: 98.5%"]
    partes = texto_sucio.split('--')
    
    # --- PROCESANDO EL NOMBRE ---
    # Quitamos los '>>>', los paréntesis y los guiones bajos
    nombre_raw = partes[0].replace('>>>', '').replace('(Concentrado)', '').replace('_', ' ')
    nombre_final = nombre_raw.strip().capitalize()
    
    # --- PROCESANDO LOS LITROS ---
    # Quitamos 'VOLUMEN:' y 'LITROS', luego convertimos a entero
    litros_raw = partes[1].replace('VOLUMEN:', '').replace('LITROS', '')
    litros_final = int(litros_raw.strip())
    
    # --- PROCESANDO LA PUREZA ---
    # Quitamos 'PUREZA:' y el '%', luego convertimos a float
    pureza_raw = partes[2].replace('PUREZA:', '').replace('%', '')
    pureza_final = float(pureza_raw.strip())
    
    return nombre_final, litros_final, pureza_final

# Probamos:
texto = "   >>> nitrógeno_LÍQUIDO (Concentrado) -- VOLUMEN: 5 LITROS -- PUREZA: 98.5%   "
nombre, litros, pureza = limpiar_quimico(texto)

print(f"¡Mira qué limpio quedó, ShadowRoot!")
print(f"Nombre: {nombre}")  # Nitrógeno líquido
print(f"Litros: {litros}")  # 5
print(f"Pureza: {pureza}")  # 98.5

