import random
import array

longitud = 15

numero = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

simbolos = ['!', '"', '@', '&', '-', '#', '$', '%', '=', ':', ';', '?', ',', '.', '/', '|', '~', '>', '*', '(', ')', '<', '[', '`', '^', '_', '`', '{', '}']

listaCombinada = numero + mayusculas + minusculas + simbolos

rand_numero = random.choice(numero)
rand_mayuscula = random.choice(mayusculas)
rand_minuscula = random.choice(minusculas)
rand_simbolo = random.choice(simbolos)

passwordTemporal = rand_numero + rand_mayuscula + rand_minuscula + rand_simbolo

for x in range(longitud - 4):
    passwordTemporal = passwordTemporal + random.choice(listaCombinada)
    listaTempPassword = array.array('u', passwordTemporal)
    random.shuffle(listaTempPassword)

password = ""
for x in listaTempPassword:
    password = password + x

print(password)

