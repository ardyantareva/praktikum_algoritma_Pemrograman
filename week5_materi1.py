#array adalah pendekatan dalam memberikan assign lebih dari satu nilai, kedalam satu variabel
#keywoards : Lebih dari satu nilai, satu variabel
#biasanya menulis :
# angka1 = 1
# angka2 = 2
# angka3 = 3
# angka4 = 4
# angka5 = 5

#dapat dipermudah dengan cara array sebagai berikut 

angka = [1,2,3,4,5]
print(angka)

#jika akan menampilakn angka terentu dapat digunakan sebagai berikut :
print(angka[0])
print()
print(angka[2])
#rumus nya ketika menginput 0 maka akan muncul angka 1 pada output seterusnya pada angka
#dalam aray dimulai dari 0 akan menyesuaikan indeks yang telah di input dalam contoh di atas terdapat 4 indeks
#terdapat fungsi append untuk mendambahkan indeks pada paling akhir

angka =[1,2,3,4,5,7]
angka.append(6) #nilai
print(angka[6]) #indeks
#berlaku tidak hanya angka saja contoh 

buah =["apel", "mangga", "semangka", "pisang", "buah naga", "Jeruk", "Jambu"]
buah.append("pir")
buah.append("Anggur")
buah.append("melon")
print(buah[9])

#pengulangan untuk array
for item in buah:
    print(item)
