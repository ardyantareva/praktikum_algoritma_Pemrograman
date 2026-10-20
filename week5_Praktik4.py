#latihan Looping akumulator dan pencacah

TARGET  = 50
HARI = 10

total = 0 # akumulator
di_bawah = 0 # pencacah

for hari in range (1,HARI + 1) :
    Produksi = int(input(f"produksi hari ke-{hari}: "))
    total = total + Produksi 
    if Produksi < TARGET :
        di_bawah = di_bawah + 1

print("total produksi", total)
print("Rata rata per hari", total/HARI)
print("hari di bawah target :", di_bawah)