# Variables 
my_string_variable = "my string variable"
print(my_string_variable)

my_int_variable = 5 
print (my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenacion de variables en un print
print(type(print("mi cadena de texto🥹😍😎🥳"))) # tipo o class 'NoneType'
print("Este es el valor de:",my_bool_variable)

# Funciones del sistema 
print(len(my_string_variable))

# Variables en una sola linea.
name, surname, alias, age="Israel", "Amaya", "Mairo", 21
print("Me llamo:",name, surname,"Tengo", age, "years old", "Y mi alias es:", alias)

# Inputs 

#name = input("What is your name: ")
#age= input("How old are you? ")

print(name)
print(age)

# Cambiamos su tipo 

name = 20
age = "Israel" 
print(name)
print(age)

# forzamos el tipo
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
address = 1+ 5j
print (type(address))  

