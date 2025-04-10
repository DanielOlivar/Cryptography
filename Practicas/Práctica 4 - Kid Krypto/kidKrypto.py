# Practical Session 4 - Kid Krypto
# Alumno: Becerril Olivar Axel Daniel
# Materia Criptografía
# Fecha de entrega 19 de abril de 2025

import fileinput  
lines = []

for line in fileinput.input():
    lines.append(line.strip())

opcUsu=lines[0].strip() 

num1=int(lines[1].strip()) 
num2=int(lines[2].strip()) 
num3=int(lines[3].strip()) 
num4=int(lines[4].strip()) #B

mensaje=int(lines[5].strip()) 


M=(num1*num2)-1
e=(num3*M)+num1
d=(num4*M)+num2
n=((e*d)-1)/M


if opcUsu=="E":
    y=int((mensaje*e)%n)
    print(y)


if opcUsu=="D":
    z=int((mensaje*d)%n)
    print(y)






