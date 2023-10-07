cumle = input("Cümləni daxil edin: ")

rekem_sayisi = 0
for i in cumle:
    if i.isdigit():
        rekem_sayisi += 1

print("Cümlədəki rəqəmlərin sayı:", rekem_sayisi)

##================================================ isdigit() metodu ===================================================#
## Əgər daxil olunan ifadə rəqəmdirsə True əks halda False qaytarır
# metin = "12345"
# sonuc = metin.isdigit()
# print(sonuc)  # True

# metin = "abc123"
# sonuc = metin.isdigit()
# print(sonuc)  # False
##=====================================================================================================================#