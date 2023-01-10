#Calculadora

from operações import *
from linguas import MSG
from config import *
from calculadora import Calculadora

x = int(input(MSG['PT']['xVal']))
y = int(input(MSG['PT']['yVal']))

calc = Calculadora

print(calc.soma(x, y))