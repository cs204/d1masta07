MONTHS = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август",
          "сентябрь", "октябрь", "ноябрь", "декабрь"]
MAX_DAYS = 31


while True:
    try:
        date = input("Дата: ")
        date = date.replace(" ", ".")
        dd, mm, yyyy = date.split(".")
        if int(dd) < 0 or int(dd) > 31:
            raise ValueError
        mm = mm if mm.isdigit() else str(MONTHS.index(mm) + 1)
        if int(mm) < 0 or int(mm) > len(MONTHS):
            raise ValueError
        if int(yyyy) < 0:
            raise ValueError
        print(f"{yyyy}-{mm.zfill(2)}-{dd.zfill(2)}")
        break
    except ValueError:
        continue
    except EOFError:
        break
    except KeyboardInterrupt:
        break
