''' Escribe un programa que solicite al usuario una cantidad de segundos y muestre
cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
hora, 1 minuto y 1 segundo.'''

segundos = float(input('Ingrese la cantidad de segundos'))
print(segundos,' equivalen a ',segundos/60,' minutos')
print(segundos,' equivalen a ',segundos/3600,' minutos')
