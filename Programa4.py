# Clase 3
# 26/05/25
# IF, ELSEIF, ELSE

print("Bienvenido a FranCode \nCamisas disponibles:")

try:
    opc = int(input("1: Camisa Blanca \n2: Camisa Negra\n3: Camisa Azul\n4: Camisa Roja \nSeleccione una camisa: "))

    if opc == 1:
        nombre_camisa = "Camisa Blanca"
        precio_camisa = 60
    elif opc == 2:
        nombre_camisa = "Camisa Negra"
        precio_camisa = 70  
    elif opc == 3:
        nombre_camisa = "Camisa Azul"
        precio_camisa = 80
    elif opc == 4:
        nombre_camisa = "Camisa Roja"
        precio_camisa = 90
    else:
        print("Opción no válida. Por favor seleccione un número del 1 al 4.")
        exit()

except ValueError:
    print("Entrada inválida. Debe ingresar un número del 1 al 4.")
    exit()

# Validar cantidad de camisas
try:
    cantidad_camisas = int(input("¿Cuántas camisas necesitas? "))
except ValueError:
    print("Entrada inválida. Debe ingresar un número.")
    exit()

tamaño = input("¿Qué talla necesitas? (S, M, L, XL): ")

# Mostrar resumen
total = precio_camisa * cantidad_camisas

print("\nResumen de compra:")
print(f"Camisa: {nombre_camisa}")
print(f"Talla: {tamaño}")
print(f"Cantidad de camisas: {cantidad_camisas}")
print(f"Total a pagar: ${total:.2f}")
