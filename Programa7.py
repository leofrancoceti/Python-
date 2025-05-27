# Clase 4
# 27/05/25
# Menu de opciones de cine con while

# Clase 3
# 26/05/25
# IF, ELSEIF, ELSE

print("Bienvenido al Cine Franco \nPelículas disponibles:")
Flag = True
while Flag:
    print("1: Volver al Futuro")
    print("2: Hombres de Honor")
    print("3: Titanic")
    print("4: Avengers")
    print("5: Salir")
    opc = int(input("Seleccione una película (1-5): "))

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

    cantidad_entradas = int(input("¿Cuántas entradas necesitas? "))
    total = precio_entrada * cantidad_entradas

    print("\nResumen de compra:")
    print(f"Película: {nombre_pelicula}")
    

    Flag = int(input("¿Desea comprar otra entrada? (1: Sí, 0: No): "))
    if Flag == 1:
        print(f"Cantidad de entradas: {cantidad_entradas}")
        print(f"Total a pagar: ${total:.2f}")
    else:
        print("Gracias por su compra")
    
