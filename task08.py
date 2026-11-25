

balans = 1_000_000


while True:
    print("""=======MENU========
1. Balansni ko‘rish
2. Pul qo‘shish
3. Pul yechish
4. Chiqish
""")

    menu = int(input("Menuni kiriting -> "))

    if menu == 1:
        print(f"Sizning balansingiz: {balans}")

    elif menu == 2:
        money = int(input("Miqdorni kiriting -> "))
        balans += money
        print(f"""
----------------------
J/balans |   {balans}|
----------------------
qoshildi |   {money} |
----------------------


""")

    elif menu == 3:
        money = int(input("Yechmoqchi bolgan summani kiriting -> "))
        balans -= money
        print(f"""
----------------------
yechildi |   {money}|
----------------------
Y/balans |   {balans} |
----------------------
        
        
""")

    elif menu == 4:
        print("xayr!")
        break

    else:
        print("siz xato menu kiritingiz!")
