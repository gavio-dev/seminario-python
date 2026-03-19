'''Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
finalizar.'''

numero= int(input('ingrese un numero'))

multiplos = []
resto = []

for i in range(1,numero+1):
    if i%5==0 :
        multiplos.append(i)
    else:
        resto.append(i)
    
print('multiplos de 5',multiplos)
print('resto de numeros',resto)
        
 
