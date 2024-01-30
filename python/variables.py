# Variables
my_string_var = "Mi variable"
print(my_string_var)

my_int_var = 5
print(my_int_var)

my_bool_var = False
print(my_bool_var)

#Concatenación
print(my_bool_var, my_int_var, my_string_var)
print("Este es el valor de:", my_bool_var)

#Cambio de type
my_int_to_str = str(my_int_var)
print(my_int_to_str)
print(type(my_int_to_str))

#Funciones del sistema
print(len(my_string_var))

#Variables en una sola línea
name, surname, alias, age = "Inn", "KK", "Lin", 34
print("Me llamo:", name, surname, "Mi edad es:", age, "y mi alias es:", alias)

#Inputs

name = input('Cual es tu nombre?')
age = input('Cuantos años tienes?')

print(name)
print(age)

#Consultar el tipo de dato
print(type("Soy un dato str")) # Tipo 'str'
print(type(5)) # Tipo 'int'
print(type(1.5)) # Tipo 'float'
print(type(3 + 1j)) # Tipo 'complex'
print(type(True)) # Tipo 'bool'
print(type(print("Mi cadena de Texto"))) # Tipo 'NoneType'