# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def userInformation(name, surename, year, city, email, phone):
    print(f"Все работает хорошо! Приняты следующие параметры: \n"
          f"Имя: {name}\n"
          f"Фамилия: {surename}\n"
          f"Год рождения: {year}\n"
          f"Город: {city}\n"
          f"Почта: {email}\n"
          f"Телефон: {phone}")


args = input("Введите имя, фамилию, год рождения, город проживания, email и телефон через пробел: ").split()

user = {
    'name': args[0],
    'surename': args[1],
    'year': args[2],
    'city': args[3],
    'email': args[4],
    'phone': args[5]
}

userInformation(**user)
