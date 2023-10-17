COINS = [50 , 20 , 10 , 5]
PRISE = 50


total = 0
while total < PRISE :
    print(f"Нужная сумма: {PRISE - total}")
    user_input = int(input("Вставьте монету: "))
    total+= 0 if user_input not in COINS else user_input
print(f"Ваша сдача: {total - PRISE}")