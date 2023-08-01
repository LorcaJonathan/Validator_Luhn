def luhn_validador(numero_tarjeta):
    reversed_num = numero_tarjeta[::-1]
    digitos = [int(digito) for digito in reversed_num]

    for i in range(1, len(digitos), 2):
        digitos[i] *= 2
        if digitos[i] > 9:
            digitos[i] -= 9

    suma_digitos = sum(digitos)

    return suma_digitos % 10 == 0

def main():
    while True:
        try:
            numero_tarjeta = input("Ingresa el número de tarjeta de crédito (Ctrl+D para salir): ")
            if not numero_tarjeta:
                print("Adiós.")
                break

            numero_tarjeta = numero_tarjeta.replace(" ", "")  # Eliminar espacios en blanco si los hubiera

            if not numero_tarjeta.isdigit():
                print("Por favor, introduce solo números enteros.")
                continue

            if luhn_validador(numero_tarjeta):
                print("El número de tarjeta es válido.")
            else:
                print("El número de tarjeta NO es válido.")

            while True:
                opcion = input("¿Quieres introducir otro número? (s/n): ").lower()
                if opcion == 's':
                    break
                elif opcion == 'n':
                    print("Adiós.")
                    return
                else:
                    print("Opción inválida. Introduce 's' para sí o 'n' para no.")

        except EOFError:
            print("\nAdiós.")
            break
        except KeyboardInterrupt:
            print("\nAdiós.")
            break

if __name__ == "__main__":
    main()
