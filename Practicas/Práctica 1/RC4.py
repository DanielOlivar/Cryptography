# Practical Session 1 - RC4 
# Alumno: Becerril Olivar Axel Daniel
# Materia Criptografía
# Fecha de entrega 11 de marzo de 2025


def edo_inicial(clave): #Key-Scheduling algorithm (KSA) 
    estado = list(range(256))
    indice_clave = 0
    longitud_clave = len(clave)
    
    for i in range(256):
        indice_clave = (indice_clave + estado[i] + clave[i % longitud_clave]) % 256
        estado[i], estado[indice_clave] = estado[indice_clave], estado[i]
    
    return estado

def PRGA(estado, longitud): #Pseudo-random generation algorithm (PRGA)
    i = 0
    j = 0
    flujo_aleatorio = []
    
    for _ in range(longitud):
        i = (i + 1) % 256
        j = (j + estado[i]) % 256
        estado[i], estado[j] = estado[j], estado[i]
        valor_flujo = estado[(estado[i] + estado[j]) % 256]
        flujo_aleatorio.append(valor_flujo)
    
    return flujo_aleatorio

def cifrado_rc4(clave, mensaje): #Cifrado RC4
    clave = [ord(c) for c in clave]
    mensaje = [ord(c) for c in mensaje]
    
    estado_inicial = edo_inicial(clave)
    flujo_aleatorio = PRGA(estado_inicial, len(mensaje))
    
    mensaje_cifrado = [m ^ f for m, f in zip(mensaje, flujo_aleatorio)]
    
    return ''.join([format(c, '02X') for c in mensaje_cifrado])

def main():
    clave = input().strip()
    mensaje = input().strip()
    
    mensaje_cifrado = cifrado_rc4(clave, mensaje)
    
    print(mensaje_cifrado)

if __name__ == "__main__":
    main()
