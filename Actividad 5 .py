# Solicitar datos del primer producto
nombre1 = input("Nombre del producto 1: ")
precio1 = float(input("Precio del producto 1: "))
cantidad1 = int(input("Cantidad del producto 1: "))
subtotal1 = precio1 * cantidad1

# Solicitar datos del segundo producto
nombre2 = input("Nombre del producto 2: ")
precio2 = float(input("Precio del producto 2: "))
cantidad2 = int(input("Cantidad del producto 2: "))
subtotal2 = precio2 * cantidad2

# Solicitar datos del tercer producto
nombre3 = input("Nombre del producto 3: ")
precio3 = float(input("Precio del producto 3: "))
cantidad3 = int(input("Cantidad del producto 3: "))
subtotal3 = precio3 * cantidad3

# Calcular subtotal general, IVA y total
subtotal_general = subtotal1 + subtotal2 + subtotal3
iva = subtotal_general * 0.16
total = subtotal_general + iva

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Subtotal: ${subtotal_general:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Total: ${total:.2f}")
