# archivo: dividir_numeros.py
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except TypeError:
        return "Error: asegúrate de que ambos números sean válidos."
    except ZeroDivisionError:
        return "Error: no se puede dividir por cero."

def main():
    a = input("Ingrese el primer número: ")
    b = input("Ingrese el segundo número: ")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Error: asegúrate de que ambos números sean válidos.")
        return

    resultado = dividir(a, b)
    print(resultado)

if __name__ == "__main__":
    main()
#Maryuri Salazar,Juan Castrillon y Joan Infante




