nama = input("Masukkan nama anda: ")
umur =int(input("masukan umur anda:"))
tinggi_badan = float(input("masukan tinggi badan anda:"))
nilai = float(input("masukan nilai anda:"))
if nilai >=90:
  print("nilai anda A")
elif nilai >=70:
  print("nilai anda B") 
elif nilai >=50:
  print("nilai anda C")
elif nilai >=20:
    print("nilai anda D")
else:
    print("nilai anda E") 

print("halo", nama)
print("tahun depan usiamu adalah", umur + 1)
print("tinggi badanmu adalah", tinggi_badan, "cm")
print("nilai kamu adalah", nilai)

