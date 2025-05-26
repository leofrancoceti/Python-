# Clase 3
# 26/05/25
# IF, ELSEIF, ELSE

print("Bienvenido al Cine Franco \nPelículas disponibles:")

try:
    opc = int(input("1: Volver al Futuro \n2: Hombres de Honor\n3: Titanic\n4: Avengers \nSeleccione una película: "))

    if opc == 1:
        nombre_pelicula = "Volver al Futuro"
        precio_entrada = 100
    elif opc == 2:
        nombre_pelicula = "Hombres de Honor"
        precio_entrada = 120
    elif opc == 3:
        nombre_pelicula = "Titanic"
        precio_entrada = 90
    elif opc == 4:
        nombre_pelicula = "Avengers"
        precio_entrada = 150
    else:
        print("Opción no válida. Por favor seleccione un número del 1 al 4.")
        exit()

except ValueError:
    print("Entrada inválida. Debe ingresar un número.")
    exit()

cantidad_entradas = int(input("¿Cuántas entradas necesitas? "))
total = precio_entrada * cantidad_entradas

print("\nResumen de compra:")
print(f"Película: {nombre_pelicula}")
print(f"Cantidad de entradas: {cantidad_entradas}")
print(f"Total a pagar: ${total:.2f}")
