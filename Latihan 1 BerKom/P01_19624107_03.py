# Input tanggal awal makan di resto
Tanggal = int(input("Tanggal awal makan di resto: "))

# Hitung total poin yang didapat
poin = 30 - Tanggal + 1

# Inisialisasi jumlah hadiah
poin_Ramen = 0
poin_Gyoza = 0
poin_Ocha = 0

# Tukar poin dengan hadiah, mulai dari hadiah terbesar (Ramen)
if poin >= 10:
    poin_Ramen = poin // 10
    poin = poin % 10  # Sisa poin setelah menukar dengan Ramen

if poin >= 5:
    poin_Gyoza = poin // 5
    poin = poin % 5  # Sisa poin setelah menukar dengan Gyoza

if poin >= 2:
    poin_Ocha = poin // 2
    poin = poin % 2  # Sisa poin setelah menukar dengan Ocha

# Cetak hasil, hanya jika lebih dari 0
hasil = []

if poin_Ramen > 0:
    hasil.append(f"{poin_Ramen} Ramen")
if poin_Gyoza > 0:
    hasil.append(f"{poin_Gyoza} Gyoza")
if poin_Ocha > 0:
    hasil.append(f"{poin_Ocha} Ocha")

# Gabungkan hasil dan cetak
if hasil:
    print(f"Nona Deb mendapat {', '.join(hasil)}.")
else:
    print("Poin tidak cukup untuk ditukarkan.")
