#belajar tentang inputan
#kombinasi inputan dengan while, if, break

print("======== PROGRAM LAMARAN PEKERJAAN BERDASARKAN GENDER ==========")

while True:
    nama = input("Masukkan nama (atau ketik 'selesai' untuk keluar): ")
    if nama.lower() == 'selesai':
        break

    gender = input("Masukkan Gender (L/P): ").upper()

    if gender == "L":
        posisi_valid = ["teknisi", "driver"]
        while True:
            posisi = input("Daftar Sebagai Teknisi atau Driver? ").strip().lower()
            if posisi in posisi_valid:
                print("Lamaran", nama, "sebagai", posisi.capitalize(), "Berhasil diterima.")
                break
            else:
                print("Posisi tidak tersedia! Pilih antara Teknisi atau Driver.")

    elif gender == "P":
        posisi_valid = ["admin", "resepsionis"]
        while True:
            posisi = input("Daftar Sebagai Admin atau Resepsionis? ").strip().lower()
            if posisi in posisi_valid:
                print("Lamaran", nama, "sebagai", posisi.capitalize(), "Berhasil diterima.")
                break
            else:
                print("Posisi tidak tersedia! Pilih antara Admin atau Resepsionis.")

    else:
        print("Gender Tidak Teridentifikasi")
        