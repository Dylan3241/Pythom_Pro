#Esta libreria importa la libreria random
import random

#Variable, todos los caracteres que puede usar para la contraseña
password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#Esta le pregunta al usuario la cantidad de caracteres que quiera que tenga la contraseña
password_length = int(input("Escriba la longitud que quiera para la contraseña: "))

#Variable para que guarde la contraseña
password = ""

for i in range(password_length):
    
    password += random.choice(password_characters)


#Imprime la contraseña
print(f"Tu contraseña es {password}")



