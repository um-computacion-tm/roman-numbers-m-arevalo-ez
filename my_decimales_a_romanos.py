def decimal_to_roman(decimal):

    romano = ''
    if decimal >= 1000:
        romano += 'M' * (decimal // 1000)
        decimal %= 1000
    if decimal >= 900:
        romano += 'CM'
        decimal -= 900
    if decimal >= 500:
        romano += 'D'
        decimal -= 500
    if decimal >= 400:
        romano += 'CD'
        decimal -= 400
    if decimal >= 100:
        romano += 'C' * (decimal // 100)
        decimal %= 100
    if decimal >= 90:
        romano += 'XC'
        decimal -= 90
    if decimal >= 50:
        romano += 'L'
        decimal -= 50
    if decimal >= 40:
        romano += 'XL'
        decimal -= 40
    if decimal >= 10:
        romano += 'X' * (decimal // 10)
        decimal %= 10
    if decimal >= 9:
        romano += 'IX'
        decimal -= 9
    if decimal >= 5:
        romano += 'V'
        decimal -= 5
    if decimal >= 4:
        romano += 'IV'
        decimal -= 4
    if decimal >= 1:
        romano += 'I' * decimal
    return romano

if __name__ == "__main__":
    input()
