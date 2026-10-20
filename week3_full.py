#variabel dan tipe data
#terdapat beberapa jenis variabel dan tipe data di python, yaitu:
#1.  string, yaitu variabel yang berisi teks atau karakter. Contohnya: nama = "David"
#2. integer, yaitu variabel yang berisi bilangan bulat. Contohnya: umur = 20
#3. float, yaitu variabel yang berisi bilangan desimal. contohnya: tinggi_badan = 168.5
#4. boolean, yaitu variabel yang berisi nilai True atau False. Contohnya: Mahasiswa = True

#contoh simuasi penggunaan variabel dan tipe data

nama = "david" #string
umur = 20 #integer
tinggi_badan = 168.5 #float
mahasiswa = True #boolean

print("selamat datang", nama, "umur anda adalah", umur, "tahun", "tinggi badan anda adalah", tinggi_badan, "cm", "status mahasiswa:", mahasiswa)
print(type(nama))
print(type(umur))
print(type(tinggi_badan))
print(type(mahasiswa))

#Percabangan pada python
#1. if statement, yaitu percabangan yang hanya memiliki satu kondisi.
#2. elif statement, yaitu percabangan yang memiliki beberapa kondisi.
#3. else statement, yaitu percabangan yang memiliki kondisi default jika semua kondisi sebelumnya tidak terpenuhi.

#contoh menggunaan percabangan pada python

nilai = int(input("masukan nilai anda: "))
if nilai >=60:
    print("LULUS")
    status = "LULUS"
else:
    print("TIDAK LULUS")
    status = "TIDAK LULUS"

    