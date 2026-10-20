#looping masukan penanda dan data kosong
total = 0
banyak = 0
#
durasi = int(input("Waktu proses (menit, -1)"))
while durasi != -1 :
    total = total + durasi
    banyak = banyak + 1 
    durasi = int(input("Waktu proses" 
    "menit, -1 selesai) : "))

if banyak == 0 :
    print("belum ada data yang dimasukan")
else : 
    print("Banyak data", banyak)
    print("Rata rata =", round (total / banyak,2), "menit")

#Waktu proses (menit, -1)10 (TRUE)
#Waktu prosesmenit, -1 selesai) : 15 (TRUE)
#Waktu prosesmenit, -1 selesai) : -1 (FALSE) karena ditandai -1 itu false di while
#Banyak data 2 (menghitung berdasarkan True)
#Rata rata = 12.5 menit (hasil dari pembagian 10+15= 25 : 2 = 12,5 menit)