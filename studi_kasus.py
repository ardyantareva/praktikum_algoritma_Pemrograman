total = 0
lulus = 0
remedial = 0
tidak_lulus = 0
tertinggi = 0
terendah = 100  


jumlah = int(input("Jumlah mahasiswa: "))


for i in range(1, jumlah + 1):
    nilai = int(input(f"Nilai mahasiswa ke-{i}: "))

   
    while nilai < 0 or nilai > 100:
        print("Nilai harus 0-100, coba lagi")
        nilai = int(input(f"Nilai mahasiswa ke-{i}: "))

   
    if nilai >= 60:
        if nilai >= 85:
            kategori = "Lulus Sangat Baik"
        else:
            kategori = "Lulus"
        lulus += 1
    else:
        if nilai >= 40:
            kategori = "Remedial"
            remedial += 1
        else:
            kategori = "Tidak Lulus"
            tidak_lulus += 1

   
    print(f"Kategori: {kategori}")
    total += nilai

    if nilai > tertinggi:
        tertinggi = nilai
    if nilai < terendah:
        terendah = nilai


rata_rata = total / jumlah if jumlah > 0 else 0

print()
print("=== REKAP KUIS ===")
print(f"Rata-rata   : {rata_rata}")
print(f"Tertinggi   : {tertinggi}")
print(f"Lulus       : {lulus}")
print(f"Remedial    : {remedial}")
print(f"Tidak lulus : {tidak_lulus}")
if jumlah > 0:
    print(f"Terendah    : {terendah}")  