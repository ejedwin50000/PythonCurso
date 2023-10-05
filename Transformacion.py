name = "Edwin"
print(type(name))
print("edwin")
name = 12
print(type(name))
name = True
print(type(name))
print("edwin" + "Diaz")
print(10 + 20)
# print("edwin " + 12) se genera un error porque no se puede concatenar un str con unint
print("Edwin " + "12")

age = 41
print("Mi edad es: " + str(age))
print(f"Mi edad es: {age}")

age = input("Escribe tu edad = ")
age = int(age)
age = age + 10
print(f"Tu edad en 10 años es {age}")

name = input("Cual es tu nombre ")
age = int(input("Digita tu edad "))

print(f"Hola  {name}  tu edad en 10 años es  {age + 10}")
