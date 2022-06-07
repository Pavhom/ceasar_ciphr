print('Привет, шпион!')


# ввод и проверка направления
direction = int(input('Для шифрования введи "1" или дешифрования "2": '))
while direction != 1 and direction != 2:
    direction = int(input('ОШИБКА ВВОДА. Для шифрования введи "1", для дешифрования "2": '))

# ввод и проверка языка
lang = input('Для выбора языка введи "en" или "ru": ').lower()
while lang != 'en' and lang != 'ru':
    lang = input('ОШИБКА ВВОДА. Для английского введи "en", для русского "ru": ').lower()


# ввод и проверка шага шифрования
def rot_n_check(rot_n):
    flag = False
    while flag == False:
        if lang == 'ru':
            if  0 < rot_n < 32:
                falg = True
                return rot_n
            else:
                rot_n = input('ОШИБКА ВВОДА. Для "ru" нужно ввести шаг от 1 до 32: ')
        elif lang == 'en':
            if 0 < rot_n < 26:
                flag = True
                return rot_n
            else:
                rot_n = input('ОШИБКА ВВОДА. Для "en" нужно ввести шаг от 1 до 26: ')


rot_n = int(input('Укажи шаг сдвига от 1 до 26 для "en" и от 1 до 32 для "ru": '))
rot_n_check(rot_n)


#ввод сообщения
message = input('Введите ваше сообщение: ')


# функция для шифрования RU
def cipher_ru(message, rot_n):
    result = ''
    for i in range(len(message)):
        if message[i].isalpha() and message[i].islower():
            order = ord(message[i]) + rot_n
            if order > 1103:
                order = (1071 + order) - 1103
            result += chr(order)
        elif message[i].isalpha() and message[i].isupper():
            order = ord(message[i]) + rot_n
            if order > 1071:
                order = (1039 + order) - 1071
            result += chr(order)
        else:
            result += message[i]
    return result


# функция для дешифрования RU
def de_cipher_ru(message, rot_n):
    result = ''
    for i in range(len(message)):
        if message[i].isalpha() and message[i].islower():
            order = ord(message[i]) - rot_n
            if order < 1072:
                order = 1103 - (1071 - order)
            result += chr(order)
        elif message[i].isalpha() and message[i].isupper():
            order = ord(message[i]) - rot_n
            if order < 1040:
                order = 1071 - (1039 - order)
            result += chr(order)
        else:
            result += message[i]
    return result


# функция для шифрования EN
def cipher(message, rot_n):
    result = ''
    for i in range(len(message)):
        if message[i].isalpha() and message[i].islower():
            order = ord(message[i]) + rot_n
            if order > 122:
                order = (96 + order) - 122
            result += chr(order)
        elif message[i].isalpha() and message[i].isupper():
            order = ord(message[i]) + rot_n
            if order > 90:
                order = (64 + order) - 90
            result += chr(order)
        else:
            result += message[i]
    return result


# функция для дешифрования EN
def de_cipher(message, rot_n):
    result = ''
    for i in range(len(message)):
        if message[i].isalpha() and message[i].islower():
            order = ord(message[i]) - rot_n
            if order < 97:
                order = 122 - (96 - order)
            result += chr(order)
        elif message[i].isalpha() and message[i].isupper():
            order = ord(message[i]) - rot_n
            if order < 65:
                order = 90 - (64 - order)
            result += chr(order)
        else:
            result += message[i]
    return result


# вывод результата
if direction == 1 and lang == 'en':
    print('Результат: ', cipher(message, rot_n), end='')
elif direction == 1 and lang == 'ru':
    print('Результат: ', cipher_ru(message, rot_n), end='')
elif direction == 2 and lang == 'en':
    print('Результат: ', de_cipher(message, rot_n), end='')
elif direction == 2 and lang == 'ru':
    print('Результат: ', de_cipher_ru(message, rot_n), end='')
