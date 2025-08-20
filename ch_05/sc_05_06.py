# file: sc_05_06.py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
value = matrix[1][2]  # Henter verdien i rad 1, kolonne 2
print(value)  # Skriver ut verdien, som er 6

first_row = matrix[0]  # Henter den første raden
print(first_row)  # Skriver ut den første raden, som er [1, 2, 3]

# for løkke for å skrive ut alle verdier i matrisen
for row in matrix:  
    for value in row:
        print(value, end=' ')  # Skriver ut verdiene i samme rad
    print()  # Går til neste linje etter hver rad

# for løkke for å skrive ut alle verdier i matrisen med indekser
for i in range(len(matrix)):    
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}", end=' ')
    print()  # Går til neste linje etter hver rad

# endre en verdi i matrisen
matrix[0][0] = 10  # Endrer verdien i rad 0, kolonne 0
print("Etter endring:", matrix)  # Skriver ut matrisen etter endringen

# kopiere en to-dimensjonal liste på ulike måter
matrix_copy1 = matrix.copy()  # Kopierer referansen til den ytre listen
matrix_copy2 = [row.copy() for row in matrix]  # Kopierer hver rad individuelt
print("Kopiert matrise (referanse):", matrix_copy1)  # Skriver ut den kopierte referansen
print("Kopiert matrise (individuelle rader):", matrix_copy2)
