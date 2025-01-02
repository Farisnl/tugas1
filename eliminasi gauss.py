# -*- coding: utf-8 -*-
"""eliminasi gauss.ipynb

# Definisikan matriks sistem persamaan linear (SPL)
SPL = [[2, 3, -1, 5], [4, 4, -3, 3], [-2, 3, -1, 1]]
# Tampilkan matriks awal
print("Sistem Persamaan Linear matriks adalah", SPL)

# Mengeliminasi baris pertama dari baris kedua
# Melakukan operasi baris: SPL[1][i] = SPL[1][i] - (2 * SPL[0][i]) untuk i dari 0 hingga 3
for i in range(4):
    SPL[1][i] = SPL[1][i] - (2 * SPL[0][i])

# Cetak elemen-elemen di baris kedua setelah eliminasi
print("Elemen-elemen baris kedua setelah eliminasi baris pertama:")
print(SPL[1][0], SPL[1][1], SPL[1][2], SPL[1][3])

# Ulangi definisi matriks SPL untuk keperluan selanjutnya
SPL = [[2, 3, -1, 5], [4, 4, -3, 3], [-2, 3, -1, 1]]
print("Sistem Persamaan Linear matriks adalah", SPL)

# Eliminasi baris pertama dari baris kedua
for i in range(4):
    SPL[1][i] = SPL[1][i] - (2 * SPL[0][i])

# Eliminasi baris pertama dari baris ketiga
for i in range(4):
    SPL[2][i] = SPL[2][i] - (-1 * SPL[0][i])

# Mengeliminasi elemen-elemen baris kedua dari baris ketiga
for i in range(3):
    SPL[2][i + 1] = SPL[2][i + 1] - (-3 * SPL[1][i + 1])

# Cetak hasil akhir matriks setelah eliminasi
print("Matriks setelah eliminasi:")
for row in SPL:
    print(row)

# Cetak elemen tertentu dari matriks untuk pemeriksaan lebih lanjut
print("Elemen SPL[1][1] setelah eliminasi:", SPL[1][1])