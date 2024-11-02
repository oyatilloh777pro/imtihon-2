# Takrorlash uchun topshiriqlar

# 1. 1 dan 10 gacha sonlarni ekranga chiqaruvchi dastur yozing. Avval for keyin while yordamida yozing.

# for i in range(1, 11):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# 2. 1 dan 100 gacha sonlarni ichidan faqat 3 ga qoldiqsiz bo'linadigan sonlarni ekranga chiqaruvchi dastur yozing.

# for son in range(1, 101):
#     if son % 3 == 0:
#         print(son)


# 3. Foydalanuvchidan 3 ta son kiritishni so'rang, va kiritilgan sonlarning eng kattasini va eng kichigini ekranga chiqaring.

# dsa = float(input("1-sonni kiriting: "))
# asd = float(input("2-sonni kiriting: "))
# lum = float(input("3-sonni kiriting: "))

# eng_katta = max(dsa, asd, lum)
# eng_kichik = min(dsa, asd, lum)

# print("Eng katta son:", eng_katta)
# print("Eng kichik son:", eng_kichik)


# 4. dict yarating, key sifatida ismlari, value sifatida esa u haqida ma'lumotlarni yozing.
#    Foydalanuvchidan biror ism kiritishni so'rang, va shu ism haqida ma'lumotni ekranga chiqaring, agar bunday ism dict ni ichida yo'q bo'lsa "Bunday ism mavjud emas" degan xabarni chiqaring.

# ismlar = {
#     "Ulug": "Ulug - bu qahramon va donishmand inson. U halol va saxovatli.",
#     "abdulloh": "abdulloh - aqlli va mehnatkash qiz. Uning yaxshi o'rganish qobiliyati bor.",
#     "Bekzod": "Bekzod - sportchi va kuchli yigit. U doim maqsadga intiluvchan.",
#     "abdulasis": "abdulasis - ijodkor va musiqaga qiziqadigan qiz. Uning ovozi yoqimli."
# }

# foydalanuvchi_ismi = input("Ism kiriting: ")

# if foydalanuvchi_ismi in ismlar:
#     print(f"{foydalanuvchi_ismi} haqida ma'lumot: {ismlar[foydalanuvchi_ismi]}")
# else:
#     print("Bu ism yoq")


# 5. 4-savoldagi dict ga yangi ismlar va ma'lumotlarni qo'shing.
#    Foydalanuvchidan yangi ism kiritishni so'rang, va shu ism haqida ma'lumotni ekranga chiqaring, agar bunday ism dict ni ichida yo'q bo'lsa shu dict ga ism:malumot qilib qo'shib ketilsin.

yangi_dict = {
    "Ulug": "Ushbu ism arab tilidan kirgan bo'lib, 'olis', ya'ni 'baland' yoki 'yuksak' ma'nosini anglatadi.",
    "begi": "Arabcha kelib chiqishi bor, va 'chiroyli', 'ziynatli' degan ma'nolarni beradi."
}

def ism_kiritish(kirit_ism):
    if kirit_ism in yangi_dict:
        return (f"{kirit_ism} ism haqida ma'lumot: {yangi_dict[kirit_ism]}")
    else:
        yangi_dict[kirit_ism] = "Bu yangi ism, hozircha ma'lumot yo'q."
        return (f"Yangi ism {kirit_ism} qo'shildi, hozircha ma'lumot yo'q.")

ism_kiritish("ulug")

# 6. 2 ta funksiya tuzing, 1-funksiyada qanchadir sonlarni qabul qilib, ularning yig'indisini return qilsin. 
#    2-funksiyada esa qanchadir sonlarni qabul qilib, ularning ko'paytmasini return qilsin. (def sum(*sonlar):)

# To avoid conflict with built-in functions, I'll make sure to use a different approach for summing numbers
def yigindi(*sonlar):
    return sum(sonlar)  # built-in sum() is called on the passed arguments

def product(*sonlar):
    result = 1
    for son in sonlar:
        result *= son
    return result

# Redefine t correctly
yigindi_example = yigindi(1, 2, 3, 4)
product_example = product(1, 2, 3, 4)

yigindi_example, product_example
