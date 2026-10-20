# penggunaan bertingkat

umur = int(input("Masukkan umur Anda: "))
kartu_pelajar = str(input("Punya kartu pelajar? (ya/tidak) "))
kode_voucher = str(input("Masukkan kode voucher: "))
harga_tiket = 75000

if umur >=17:
    print("umur anda memenuhi untuk menonton bioskop")
    if kartu_pelajar == "ya":
        print("anda mendapatkan diskon tiket bioskop")
        if kode_voucher == "DISKON50" or kode_voucher == "teluasoy":
            print("anda mendapatkan tambahan diskon Rp.10000 untuk tiket bioskop")
            if kode_voucher == "DISKON50" or kode_voucher == "teluasoy":
                harga_tiket = harga_tiket - 10000
                print("harga Tiket bioskop anda menjadi Rp.", harga_tiket)
            else:
                print("anda tidak mendapatkan tambahan diskon")
                print("harga tiker biskop anda Rp.", harga_tiket)
        else :
            print("anda tidak mendapatkan tambahan diskon untuk tiket bioskop")
    else:
        print("anda tidak mendapatkan diskon tiket bioskop")
else:
    print("umur anda tidak memenuhi untuk menonton bioskop")

