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
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            break
            return
        except ValueError:
            print("Error: asegúrate de que ambos números sean válidos.")
    resultado = dividir(a, b)
    print(resultado)

if __name__ == "__main__":
    main()
#Maryuri Salazar,Juan Castrillon y Joan Infante   







