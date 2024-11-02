for i in range(1, 101):
    if i % 5 != 0:
        print(i, end=", ")

ismlar = []
while True:
    ism = input("Ism kiriting (to'xtash uchun 'stop' deb yozing): ")
    if ism.lower() == 'stop':
        break
    ismlar.append(ism)

for ism in ismlar:
    print(ism)

footballers = {}
while True:
    ism = input("Futbolchi ismi (to'xtash uchun 'stop' deb yozing): ")
    if ism.lower() == 'stop':
        break
    gol = int(input(f"{ism} ning gollari sonini kiriting: "))
    footballers[ism] = gol

for ism, gol in footballers.items():
    print(f"{ism} - {gol} gol urgan.")
