from clases.avanzadas import OperacionesAvanzadas

def menu():
    print("\n=== Calculadora Avanzada Xd")
    print("1) Potencia (base ^ exponente)")
    print("0) Salir")


def leer_float(msg):
    while True:
        try:
            return float(input(msg))
        except Exception:
            print("Entrada inválida. Intenta de nuevo.")


def main():
    calc = OperacionesAvanzadas()

    while True:
        menu()
        opcion = input("Elige una opción: ").strip()


        if opcion == "1":
            base = leer_float("Base: ")
            exponente = leer_float("Exponente: ")
            resultado = calc.potencia(base, exponente)  
            print(f"Resultado: {resultado}")

        elif opcion == "0":
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
