def roman_to_decimal(numero_romano):

    decimal = 0
    i = 0
    while i < len(numero_romano):
        if numero_romano[i] == 'M':
            decimal += 1000
            i += 1
        elif numero_romano[i] == 'D':
            decimal += 500
            i += 1
        elif numero_romano[i] == 'C':
            if i + 1 < len(numero_romano) and numero_romano[i+1] == 'D':
                decimal += 400
                i += 2
            elif i + 1 < len(numero_romano) and numero_romano[i+1] == 'M':
                decimal += 900
                i += 2
            else:
                decimal += 100
                i += 1
        elif numero_romano[i] == 'L':
            decimal += 50
            i += 1
        elif numero_romano[i] == 'X':
            if i + 1 < len(numero_romano) and numero_romano[i+1] == 'L':
                decimal += 40
                i += 2
            elif i + 1 < len(numero_romano) and numero_romano[i+1] == 'C':
                decimal += 90
                i += 2
            else:
                decimal += 10
                i += 1
        elif numero_romano[i] == 'V':
            decimal += 5
            i += 1
        elif numero_romano[i] == 'I':
            if i + 1 < len(numero_romano) and numero_romano[i+1] == 'V':
                decimal += 4
                i += 2
            elif i + 1 < len(numero_romano) and numero_romano[i+1] == 'X':
                decimal += 9
                i += 2
            else:
                decimal += 1
                i += 1
    return decimal

if __name__ == "__main__":
    input()
