# -*- coding: utf-8 -*-
"""bisection.ipynb

# Impor library numpy untuk operasi numerik
import numpy as np
# Definisikan fungsi bisection untuk mencari akar dari fungsi f dalam interval [a, b]
def bisection(f, a, b, tol):
    # Memeriksa apakah f(a) dan f(b) memiliki tanda yang sama; jika iya, metode tidak dapat digunakan
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "tidak bisa")
    # Hitung titik tengah dari interval [a, b]
    m = (a + b)/2
    # Memeriksa apakah nilai fungsi di titik tengah cukup dekat ke nol (sesuai toleransi)
    if np.abs(f(m)) < tol:
        return m  # Kembalikan titik tengah sebagai perkiraan akar jika sudah memenuhi toleransi
    # Jika f(a) dan f(m) memiliki tanda yang sama, akar berada di interval [m, b]
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection(f, m, b, tol) # Rekursi dengan [m, b] sebagai interval baru
         # Jika f(b) dan f(m) memiliki tanda yang sama, akar berada di interval [a, m]
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisection(f, a, m, tol)# Rekursi dengan [a, m] sebagai interval baru

# Definisikan fungsi f(x) = x^2 - 2 yang ingin kita cari akarnya
f = lambda x: x**2 - 2

# Gunakan fungsi bisection untuk mendekati akar dari f dalam interval [0, 2] dengan toleransi 0.1
r1 = bisection(f, 0, 2, 0.1)
print("r1 =", r1)# Cetak hasil untuk toleransi 0.1
# Gunakan fungsi bisection untuk mendekati akar dari f dalam interval [0, 2] dengan toleransi 0.01
r01 = bisection(f, 0, 2, 0.01)
print("r01 =", r01)# Cetak hasil untuk toleransi 0.01

# Evaluasi fungsi pada perkiraan akar yang ditemukan dengan toleransi 0.1
print("f(r1) =", f(r1))
# Evaluasi fungsi pada perkiraan akar yang ditemukan dengan toleransi 0.01
print("f(r01) =", f(r01))