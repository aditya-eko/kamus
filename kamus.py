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
