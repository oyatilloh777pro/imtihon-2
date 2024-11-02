# - **Nazariy vazifalar (40 ball)**
# 1. For va while orasidagi farq nimada?
# Javob: For — sikl operatori bajariladigan qadamlar soni aniq bo’lganda ishlatiladi.
# While — sikl operatori bajariladigan qadamlar soni aniq bo’lmaganda va shartni avval tekshirish zarur bo’lganda ishlatiladi.

# 2. List ma’lumot turlarining qanday metodlari mavjud?
# Javob: remove, insert, sort, sorted, append, extend, pop, reverse.

# 3. List va tuple ma’lumot turlarini orasidagi 3ta farqni yozing
# Javob: 1-farq: Qavslarida farq list[], tuple().
# 2-farq: list o'zgaradi,tuple o'zgarmaydi.
# 3-farq:

# 4. Dict qanday ma’lumot turi hisoblanadi? Uning boshqa ma’lumot turlaridan qanday farqlari bor?
# Javob: dict ning kalitlari o‘zgarmas (immutable) bo‘lishi kerak. Odatda, sonlar, qatorlar (strings), va turilar (tuples) kalit sifatida ishlatilishi mumkin.
#  Ammo ro‘yxatlar (lists) yoki boshqa o‘zgaruvchan (mutable) ma’lumot turlari kalit sifatida ishlatilmaydi.
# Farqi: Boshqa ma'lumotlarda kalitlar o'zgaradi.

# - **Amaliy vazifalar (60 ball)**
# 1. Foydalanuvchidan matn kiritishini so'rang va o'sha matnda nechta harf, raqam, bo’shliq(probel) ishlatilganligini hisoblab chiqaring.
#     input: Bir yilda 365 kun mavjud
#     output: Harflar: 17, Raqamlar: 3, Probellar: 4 
# Kod: 

# savol = input("So'z kiriting: ")

# def count_elements(text):
#     asd = sum(c.isalpha() for c in text)
#     dig = sum(c.isdigit() for c in text)
#     asp = sum(c.isspace() for c in text)
#     return asd, dig, asp

# input_text = "Bir yilda 365 kun mavjud"

# asd, dig, asp = count_elements(input_text)
# print(asd, dig, asp)


# 2. Foydalanuvchidan bir son kiritishini so'rang va 1 dan o'sha songacha juft sonlar yi'g'indisini va toq sonlar yig'indisini hisoblab chiqaring.
#     input: 15
#     output: Juftlar: 36, Toqlar: 54
# Kod:
# def sonlar_yigindisi():
#     n = int(input("Bir son kiriting: "))
#     juftlar = sum(x for x in range(1, n+1) if x % 2 == 0)
#     toqlar = sum(x for x in range(1, n+1) if x % 2 != 0)
#     print(f"Juftlar yig'indisi: {juftlar}")
#     print(f"Toqlar yig'indisi: {toqlar}")

# sonlar_yigindisi()

# 3. Harfni top o'yini. Kompyuter random moduli orqali ingliz alifbosidagi bir harfni tanlaydi, foydalanuvchidan bir harf kiritishini so'rang va 5ta urinishda o'sha harfni topish o'yini dasturini yarating. 
# Agar harf topilsa uni nechta urinishda topilgani ham chiqarilsin. Harf katta yoki kichik bo'lsa ham topgan hisoblansin. 
#     Random: h
#     input: h
#     output: Barakalla, siz 3ta urinishda topdingiz
# Kod:
# def toqlar_yigindisi(n):
#     toqlar = sum(x for x in range(1, n+1) if x % 2 != 0)
#     print(f"Toq sonlar yig'indisi: {toqlar}")

# toqlar_yigindisi(15)


# 4. 1 dan 100 gacha bo'lgan sonlarni if orqali tekshirib toqlarni toq_sonlar degan listga, juftlarni juft_sonlar degan listga qo'shib oxirida ekranga qaytaradigan funksiya yozing.
# Kod:   
# def sonlarni_tekshir():
#     toq_sonlar = []
#     juft_sonlar = []
    
#     for son in range(1, 101):
#         if son % 2 == 0:
#             juft_sonlar.append(son)
#         else:
#             toq_sonlar.append(son)
    
#     return toq_sonlar, juft_sonlar

# toq_sonlar, juft_sonlar = sonlarni_tekshir()
# print("Toq sonlar:", toq_sonlar)
# print("Juft sonlar:", juft_sonlar)


# 5. Foydalanuvchidan biror son kiritishini so'rang va shu songacha bo'lgan barcha toq sonlarni yig'indisini qaytaradigan funksiya yarating.
# Kod:
# def toq_sonlar_yigindisi():
#     son = int(input("Iltimos, biror musbat son kiriting: "))
#     yigindi = 0
    
#     for i in range(1, son + 1):
#         if i % 2 != 0:
#             yigindi += i
    
#     return yigindi

# yigindi = toq_sonlar_yigindisi()
# print("Toq sonlar yig'indisi:", yigindi)


# 6. Foydalanuvchidan x va y sonlarini kiritishni so'rang, x dan y gacha bo'lgan juft sonlar yig'indisini ekranga chiqaring.

# def juft_sonlar_yigindisi():
#     x = int(input("Iltimos, x sonini kiriting: "))
#     y = int(input("Iltimos, y sonini kiriting: "))
    
#     yigindi = 0
    
#     for i in range(x, y + 1):
#         if i % 2 == 0:
#             yigindi += i
    
#     print("x dan y gacha bo'lgan juft sonlar yig'indisi:", yigindi)


# juft_sonlar_yigindisi()


