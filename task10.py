
mahsulotlar = ["Olma", "Banan", "Uzum", "Anor"]
narxlar = [12000, 18000, 25000, 40000]

savatcha = []
narx = []

while True:
    print("""
======== M E N U =========
|1. Barcha mahsulotlarni ko'rish.
|2. Mahsulot sotib olish.
|3. Savatdagi mahsulotlarni ko'rish.
|4. Umumiy summani hisoblash.
|5. Xaridni yakunlash.
===========================
""")

    menu = int(input("Menuni kiriting -> "))

    if menu == 1:
        print("\nBarcha mahsulotlar:")

        for i in range(len(mahsulotlar)):
            print(f"{i}. {mahsulotlar[i]} - {narxlar[i]} so'm")

    elif menu == 2:
        print("\nMahsulotlar:")

        for i in range(len(mahsulotlar)):
            print(f"{i}. {mahsulotlar[i]} - {narxlar[i]} so'm")

        mahsulot = int(input("Olmoqchi bo'lgan mahsulot ID sini kiriting -> "))

        if mahsulot >= 0 and mahsulot < len(mahsulotlar):
            savatcha.append(mahsulotlar[mahsulot])
            narx.append(narxlar[mahsulot])

            print(f"{mahsulotlar[mahsulot]} savatchaga qo'shildi!")

        else:
            print("Bunday mahsulot mavjud emas!")

    elif menu == 3:
        print("\nSavatchadagi mahsulotlar:")

        if len(savatcha) == 0:
            print("Savatcha bo'sh!")
        else:
            for i in range(len(savatcha)):
                print(f"{i + 1}. {savatcha[i]} - {narx[i]} so'm")

    elif menu == 4:
        print(f"Umumiy summa: {sum(narx)} so'm")

    elif menu == 5:
        print(f"""
Xaridingiz uchun rahmat!

Sotib olingan mahsulotlar: {len(savatcha)} ta
Umumiy summa: {sum(narx)} so'm

Xayr!
""")
        break

    else:
        print("Siz noto'g'ri menu kiritdingiz!")
