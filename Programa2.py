#Clase 2
#24/05/25
#Programa de cine 

def calcular_costo_total():
    # Bienvenida
    print("Bienvenido al sistema de cálculo de costo de películas")
    
    # Solicitar datos al usuario
    nombre_pelicula = input("¿Qué película deseas ver? ")
    precio_entrada = float(input("Ingresa el precio de la entrada: $"))
    cantidad_entradas = int(input("¿Cuántas entradas necesitas? "))
    
    # Calcular total
    total = precio_entrada * cantidad_entradas
    
    # Mostrar resultados
    print("\nResumen de compra:")
    print(f"Película: {nombre_pelicula}")
    print(f"Precio por entrada: ${precio_entrada:.2f}")
    print(f"Cantidad de entradas: {cantidad_entradas}")
    print(f"Total a pagar: ${total:.2f}")

# Llamar a la función
calcular_costo_total()