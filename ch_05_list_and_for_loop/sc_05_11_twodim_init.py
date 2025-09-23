#  file: sc_05_11_twodim_init.py
# Initialisering av en to-dimensjonal liste (matrise) med løkker og med comprehension

NUM_ROWS = 3
NUM_COLS = 3
matrix = []
for i in range(NUM_ROWS):
    row = [] # begynner med en tom rad for hvert rad-nivå
    for j in range(NUM_COLS):
        value = i * NUM_COLS + j + 1
        row.append(value) # Fyller med tall fra 1 til 9
    matrix.append(row)
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# samme med comprehension
matrix = [[i * NUM_COLS + j + 1 for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
