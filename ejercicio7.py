'''Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
espacios. Las palabras cortas deben ser excluidas del resultado final.'''

lista = []
while True:
    lista.append(input('Ingrese una palabra '))
    if lista[-1]=='0':
        break
        
resultado =''

for i in lista:
    if len(i)>3:
        resultado +=i + ' '

print(resultado)

    