def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

def calculadora():
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Seleccione la operación (1/2/3/4): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("El resultado de la suma es:", suma(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es:", resta(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("El resultado de la división es:", division(num1, num2))
    else:
        print("Opción no válida")

calculadora()