def analizar_texto(texto):
    caracteres = len(texto)
    palabras_lista = texto.split()
    palabras = len(palabras_lista)
    lineas = len(texto.splitlines()) if texto else 0
    espacios = texto.count(" ")
    vocales = sum(1 for letra in texto.lower() if letra in "aeiouáéíóú")
    palabra_mas_larga = max(palabras_lista, key=len) if palabras_lista else ""

    return {
        "caracteres": caracteres,
        "palabras": palabras,
        "lineas": lineas,
        "espacios": espacios,
        "vocales": vocales,
        "palabra_mas_larga": palabra_mas_larga,
        "mayusculas": texto.upper()
    }


def main():
    print("=== Analizador de texto ===")
    texto = input("Ingrese un texto: ").strip()

    if not texto:
        print("No se ingresó texto.")
        return

    resultado = analizar_texto(texto)

    print("\n=== Resultado ===")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
