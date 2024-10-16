Keberangkatan = int(input("Jam Keberangkatan Nona Deb: "))
Kepulangan = int(input("Jam Kepulangan Nona Deb: "))

biaya = 0
bus_keberangkatan = ""
bus_kepulangan = ""

if (6 <= Keberangkatan <= 8 or 15 <= Keberangkatan <= 17):
    biaya += 0
    bus_keberangkatan = "Bus Universitas"
elif (7 <= Keberangkatan <= 18):
        biaya += 5000
        bus_keberangkatan = "Bus Kota"
elif (0 <= Keberangkatan <= 24):
            biaya += 10000
            bus_keberangkatan = "Travel"

if (6 <= Kepulangan <= 8 or 15 <= Kepulangan <= 17):
    biaya += 0
    bus_kepulangan = "Bus Universitas"
elif (7 <= Kepulangan <= 18):
        biaya += 5000
        bus_kepulangan = "Bus Kota"
elif (0 <= Kepulangan <= 24):
            biaya += 10000
            bus_kepulangan = "Travel"
print(f"Nona Deb berangkat naik {bus_keberangkatan} dan pulang naik {bus_kepulangan} dengan total biaya {biaya}.")

