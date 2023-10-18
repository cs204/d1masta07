MENU = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}


total = 0
while True:
    try:
        user_input = input("Блюдо: ")
        try:
            total = MENU[user_input]
        except KeyError as ke:
            pass
        except KeyboardInterrupt as ki:
            break
    except:
        break
print(f"\nСумма: {total:.2f}")