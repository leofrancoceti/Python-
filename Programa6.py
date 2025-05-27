# Clase 4
# 27/05/25
# Menu de opciones con camisa con while
print("Bienvenido a FranCode \nCamisas disponibles:")
Flag = True

while Flag:
    print("1: Camisa Cruz Azul")
    print("2: Camisa Chivas")
    print("3: Camisa Atlas")
    print("4: Camisa America")
    print("5: Camisa Pumas")
    print("6: Salir")
    
    opc = int(input("Seleccione una camisa (1-6): "))

    if opc == 1:
        nombre_camisa = "Camisa Cruz Azul"
        precio_camisa = 60
    elif opc == 2:
        nombre_camisa = "Camisa Chivas"
        precio_camisa = 70  
    elif opc == 3:
        nombre_camisa = "Camisa Atlas"
        precio_camisa = 80
    elif opc == 4:
        nombre_camisa = "Camisa America"
        precio_camisa = 90
    elif opc == 5:
        nombre_camisa = "Camisa Pumas"
        precio_camisa = 100
    elif opc == 6:
        print("Gracias por visitar FranCode.")
        break
    else:
        print("Opción no válida. Por favor seleccione un número del 1 al 6.")
        continue

    cantidad_camisas = int(input("¿Cuántas camisas necesitas? "))
    tamaño = input("¿Qué talla necesitas? (S, M, L, XL): ")

    total = precio_camisa * cantidad_camisas
    print("\nResumen de compra:")
    print(f"Camisa: {nombre_camisa}")
    print(f"Talla: {tamaño}")
    print(f"Cantidad de camisas: {cantidad_camisas}")
    print(f"Total a pagar: ${total:.2f}")

    Flag = int(input("¿Desea comprar otra camisa? (1: Sí, 0: No): "))
    
    if Flag == 0:
        print("Gracias por su compra")
        
