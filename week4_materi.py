#percabangan bertingkat

umur = 17
kartu_pelajar = "tidak ada"

print("umur anda", umur , "tahun")

if umur >= 17 :
    print("Anda dapat menonton bioskop")
    if kartu_pelajar == "ada" :
        print("anda mendapatkan diskon tiket bioskop")

    else :
        print("anda tidak mendapatkan diskon tiket bioskop")

else : 
    print("anda tidak dapat menonton bioskop")


# perulangan for

#contoh 1
for angka in range(6):  #mulai dari 0 berhenti sebelum 5
    print(angka, end=" ")


for angka2 in range(1,6,2):  #mulai dari 1 berhenti sebelum 6, loncat 2
    print(angka2, end=" ")

#contoh 2
harga_satuan= 25000

for jumlah in range(1,4):
    total = harga_satuan * jumlah
    print(jumlah, "pcs =", total)


#perulangan while

hitung = 1
while hitung <= 5:
    print("hitungan ke-", hitung)
    hitung +=1
print("selesai")
