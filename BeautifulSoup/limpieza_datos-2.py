precio_sucio = "!!COSTO: 150,50_USD!!"

# Pista: Tienes que quitar los "!!", el "COSTO: ", el "_USD" 
# y cambiar la coma por un punto.
# Puedes encadenar: .replace().replace().replace()...

precio_limpio = precio_sucio.replace('!!', '').replace('COSTO: ', '').replace('_USD', '').replace(',', '.')

print(precio_limpio)

