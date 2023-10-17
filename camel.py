user_input = input("Верблюжий стиль: ")
snake_case = ""
for letter in user_input :
    if letter.islower():
        snake_case += letter
    else :
        snake_case += f"_{letter.lower()}"
print(snake_case)