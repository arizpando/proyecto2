import math
print ('Hallar volumen,área total y la diagonal de un prisma rectangular')
base = float(input('base= '))
ancho = float(input('ancho= '))
altura = float(input('altura= '))
volumen = base*ancho*altura
area = (((base*altura)*4)+((base*ancho)*2))
diagonalBase = math.sqrt((base**2)*(ancho**2))
diagonal= math.sqrt((diagonalBase**2)*(altura**2))
print('volumen= ',volumen)
print('area= ',area)
print('diagonal= ',round(diagonal, 3))
