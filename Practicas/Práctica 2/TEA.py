# Practical Session 2 - Tiny Encryption Algorithm 
# Alumno: Becerril Olivar Axel Daniel
# Materia Criptografía
# Fecha de entrega 28 de marzo de 2025

def encrypt(v, k):
    delta = 0x9e3779b9
    n = 32
    suma = 0
    v0, v1 = v
    k0, k1, k2, k3 = k

    for _ in range(n):
        suma = (suma + delta) & 0xFFFFFFFF
        v0 = (v0 + (((v1 << 4) + k0) ^ (v1 + suma) ^ ((v1 >> 5) + k1))) & 0xFFFFFFFF
        v1 = (v1 + (((v0 << 4) + k2) ^ (v0 + suma) ^ ((v0 >> 5) + k3))) & 0xFFFFFFFF

    return [v0, v1]

def decrypt(v, k):
    delta = 0x9e3779b9
    n = 32
    suma = (n * delta) & 0xFFFFFFFF
    v0, v1 = v
    k0, k1, k2, k3 = k

    for _ in range(n):
        v1 = (v1 - (((v0 << 4) + k2) ^ (v0 + suma) ^ ((v0 >> 5) + k3))) & 0xFFFFFFFF
        v0 = (v0 - (((v1 << 4) + k0) ^ (v1 + suma) ^ ((v1 >> 5) + k1))) & 0xFFFFFFFF
        suma = (suma - delta) & 0xFFFFFFFF

    return [v0, v1]

def respuesta(valor):
    return ",".join(f"0x{val:08X}" for val in valor)

def main():
    modo = input().strip().upper()
    plaintext = [int(x, 16) for x in input().strip().split(",")]
    key = [int(x, 16) for x in input().strip().split(",")]

    if modo == "E":
        resultado = encrypt(plaintext, key)
    elif modo == "D":
        resultado = decrypt(plaintext, key)
    else:
        raise ValueError("Modo inválido. Usa 'E' para cifrar o 'D' para descifrar.")

    print(respuesta(resultado))

if __name__ == "__main__":
    main()



