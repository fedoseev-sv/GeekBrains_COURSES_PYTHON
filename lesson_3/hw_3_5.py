# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

indexList = []
while True:
    args = input("Введите числа через пробел (для выхода из программы введите 'q'): ").split()

    if args[0] == "q":
        break
    else:
        for el in args:
            indexList.append(float(el))
        print(sum(indexList))


print("Программа звершила работу")
