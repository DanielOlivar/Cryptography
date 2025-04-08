#Becerril Olivar Axel Daniel

import fileinput 

lines = [] 
for line in fileinput.input():
    lines.append(line.strip())

total=0
decimal=False

for numStr in lines:
    if "." in numStr:
        numero=float(numStr)
        decimal=True
    else: 
        numero=int(numStr)
    total+=numero

if decimal: print(total)
else: print(int(total))