while True: # проверка условий ввода
    try:
        numbers = input('Введите числа через пробел:   ')
        number_user = int(input('Введите любое число:  '))
        number_list = numbers.split() # преобразование строки в список
        s = ''
        a = s.join(number_list) #возврат в строку без пробелов, для проверки на недопустимые знаки

        if " " not in numbers: #проверка на пробелы
            print("\n введите числа через пробел!")
            continue
        elif a.isdigit():# проверка на цифры
            break
        else:
            print('Вводить нужно только цифры')
            continue
    except ValueError:
        print("Нужно ввести число!")


#Преобразование списока строк в список чисел
number_list = [int(item) for item in number_list]


def merge_sort(L):
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
number_list = merge_sort(number_list)
print(number_list)


def binary_search(number_list, number_user, left, right):
     if number_list[left]>number_user:  # если введенное число меньше первого элемента
         return False  # значит элемент отсутствует

     middle = (right + left) // 2  # находим середину
     if number_list[middle] >= number_user:  # если элемент в середине,
         return middle  # возвращаем этот индекс
     elif number_user < number_list[middle]:  # если элемент меньше элемента в середине
         #рекурсивно ищем в левой половине
         return binary_search(number_list, number_user, left, middle - 1)
     else: # иначе в правой
         return binary_search(number_list, number_user, middle + 1, right)


try:
    print("Позиция элемента меньше введенного числа:", binary_search(number_list, number_user, -1,  len(number_list)))
except IndexError:
    print('Число больше всех введенных чисел')
