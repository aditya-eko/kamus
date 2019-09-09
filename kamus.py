mahasiwa={}

mahasiwa["nama"]="eko agus susanto"
mahasiwa["nip"]=1234
mahasiwa["asal"]="brebes"
mahasiwa["fakultas"]="teknik informasi"

# mengakses dictionary
print(mahasiwa)
print(mahasiwa.items())
print(mahasiwa.get("nama"))
print(mahasiwa["asal"])
print(mahasiwa["fakultas"])

# merubah item pada dictionary
mahasiwa["nama"]="eko agus aditya"
print(mahasiwa.items())
mahasiwa["asal"]="jogjakarta"



#menghapus item mahasiswa
mahasiwa.pop("asal")   #pop di gunakan untuk menghapus isi list dengan menambahkan parameter key
print(mahasiwa.items())
mahasiwa.popitem()   #popitem yaitu menghapus item secara acak defaultnya adalah di belakang
print(mahasiwa.items())

del mahasiwa["nama"]


print(mahasiwa)