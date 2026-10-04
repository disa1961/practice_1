from datetime import date
def century_message(name: str, age: int, current_year: int) -> str:
    years_to_100 = 100 - age
    year_100 = current_year + years_to_100

    return f"{name}, тебе исполнится 100 лет в {year_100} году"
if __name__=="__main__":
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст: "))
    current_year = date.today().year
    message = century_message(name, age, current_year)
    print(message)
