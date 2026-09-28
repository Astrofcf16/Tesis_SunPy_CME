from math import sin, pi
a, b = map(float, input('Ingrese a y b: ').split())
theta = float(input('Ingrese el valor del angulo: '))
area = 0.5*a*b*sin(theta*pi/180.)
print('El area es: ', area)
