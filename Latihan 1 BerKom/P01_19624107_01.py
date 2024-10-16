R1 = int(input("Masukkan nilai resistor pertama: "))
R2 = int(input("Masukkan nilai resistor kedua : "))
R3 = int(input("Masukkan nilai resistor ketiga: "))

Total = 1/(1/R1 + 1/R2 + 1/R3)

print(f"Total hambatan rangkaian adalah {Total} ohm.")