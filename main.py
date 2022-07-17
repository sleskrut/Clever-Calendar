# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print('Hello world')
print('Добро пожаловать в умный календарь')
s0 = ' '  # Далее объявляются ключевые массивы
Word = 'None'
List_of_words = list()
List_of_Doing = ['', '', '', '', '', '']
Days = ['Сегодня', 'Завтра', 'Послезавтра', 'Понедельник', 'Понедельника', 'Понедельнику', 'Понедельником',
        'Понедельнике', 'Понедельники', 'Понедельников', 'Понедельникам', 'Понедельниками', 'Понедельниках', 'Вторник',
        'Вторника', 'Вторнику', 'Вторником', 'Вторнике', 'Вторники', 'Вторников', 'Вторнику', 'Вторниками', 'Вторниках',
        'Среда', 'Среды', 'Среде', 'Среду', 'Средой', 'Сред', 'Средам', 'Средами', 'Средах', 'Четверг', 'Четверга',
        'Четвергу', 'Четвергом', 'Четверге', 'Четверги', 'Четвергов', 'Четвергам', 'Четвергами', 'Четвергах', 'Пятница',
        'Пятниц', 'Пятнице', 'Пятницу', 'Пятницой', 'Пятницы', 'Пятницам', 'Пятницами', 'Пятницах', 'Суббота',
        'Субботы', 'Субботе', 'Субботу', 'Субботой', 'Суббот', 'Субботам', 'Субботами', 'Субботах', 'Вокресенье',
        'Вокресенья', 'Вокресенью', 'Вокресеньем', 'Вокресений', 'Вокресеньям', 'Вокресеньями', 'Вокресеньях']
Years = ['день', 'дня', 'дню', 'днём', 'дне', 'дни', 'дней', 'дням', 'днями', 'днях', 'неделя', 'недели', 'неделе', 'неделю', 'неделей', 'недель', 'неделям', 'неделями', 'неделях', 'месяц', 'месяца', 'месяцу', 'месяцем', 'месяце', 'месяцы', 'месяцев', 'месяцы', 'месяцами', 'месяцах', 'год', 'года', 'году', 'годом', 'годе', 'годы', 'лет']
Months = ['январь', 'января', 'январю', 'январём', 'январе', 'февраль', 'март', 'марта', 'марту', 'мартом', 'марте', 'апрель', 'апреля', 'апрелю', 'апрелем', 'апрелуи', 'май', 'мая', 'маю', 'маем', 'мае', 'июнь', 'июня', 'июню', 'июнем', 'июне', 'июль', 'июля', 'июлю', 'июлем', 'июле', 'август', 'августа', 'августу', 'августом', 'августе', 'сентябрь', 'сентября', 'сентябрю', 'сентябрём', 'сентябре', 'октябрь', 'октября', 'октябрю', 'октябрём', 'октябре', 'ноябрь', 'ноября', 'ноябрю', 'ноябрём', 'ноябре', 'декабрь', 'декабря', 'декабрю', 'декабрём', 'декабре']

def cover_string(A):  # Функция собирает отдельные элементы обратно в строку
    S = ' '
    for i in range(0, len(A), 1):
        if A[i] != ' ':
            S = S + A[i]
            S = S + ' '
    return S

def low(s): # Понижение регистра всех букв
    for i in range(0, len(s), 1):
        s[i] = s[i].lower()
    return s


low(Days)


def inf(s, moment_word):
    for i in range(0, len(s), 1):
        if s[i] == moment_word:
            s[i] = ''
    p = cover_string(s)
    return p


# def inf_is_data(A):


def deсover_string(s):
    A = list()
    j = 0
    x = len(s)
    A.append(' ')  # Функция разбивает предложение на слова
    for i in range(0, x, 1):
        if s[i] != ' ':
            A[j] = A[j] + s[i]  # Заполнение j-го элемента массива слов
        else:

            q=A[j].split()  # Переход к следующему элементу массива слов
            A[j] = ''.join(q)

            j = j + 1
            A.append(' ')

    q = A[j].split()
    A[j] = ''.join(q)
    return A  # Массив из слов (от пробела до пробела или конца функции)

def find_word_data(s, etalon):
    x = 0
    for j in range(0, len(s), 1):  # Находим ключевые слова (сегодня, завтра, через 3 дня и т. п)
        for i in range(0, len(etalon), 1):
            if s[j] == etalon[i]:
                x += 1
                word = etalon[i]

    if x >= 2:
        print('Ошибка даты. В предложении 2 и более слов, обозначающих дату. Введите предложение с одним таким словом')
        word = ''
    if x == 0:
        print('Не найдено слова, обозначающего дату')
        word = ''
    return word


def find_month(s, etalon):
    C = ['', '', '']
    x = 0
    for j in range(0, len(s), 1):  # Находим ключевые слова (сегодня, завтра, через 3 дня и т. п)
        for i in range(0, len(etalon), 1):
            if s[j] == etalon[i]:
                x += 1
                word = etalon[i]
                y = j

    if x >= 2:
        print('Ошибка даты. В предложении 2 и более слов, обозначающих дату. Введите предложение с одним таким словом')
        word = ''
    if x == 0:
        print('Не найдено слова, обозначающего дату')
        word = ''
    C[1] = word
    C[0] = C[2] = ''
    if x == 1:
        if (y != 0) and (s[y - 1].isnumeric() == True) and (len(s[y - 1]) <= 2):
            C[2] = s[y - 1]
        if (y != len(s) - 1) and (s[y + 1].isnumeric() == True) and (len(s[y + 1]) == 4):
            C[0] = s[y + 1]

    return C


def find_data(A):
    C = ['', '', '']
    for i in range(0, len(A), 1):  # Находим дату (типа 21.10 или 21.10.22)
        B = A[i]
        x = 0
        for j in range(0, len(B), 1):
            if B[j] == '.':
                x = 1
        for j in range(0, len(B), 1):
            if (B[j] != '.') and (B[j].isnumeric() == False):  # Проверка: является ли символ (строка) числом
                x = 0
        if x == 1:
            if len(B) == 5:
                if B[2] == '.':
                    C[2] = B[0] + B[1]
                    C[1] = B[3] + B[4]
            if len(B) == 10:
                if B[2] == '.':
                    C[2] = B[0] + B[1]
                    C[1] = B[3] + B[4]
                if B[5] == '.':
                    C[0] = B[6] + B[7] + B[8] + B[9]
            if len(B) == 8:
                if B[2] == '.':
                    C[2] = B[0] + B[1]
                    C[1] = B[3] + B[4]
                if B[5] == '.':
                    C[0] = '20'  # Дописать функцию добавления текущего века
                    C[0] = C[0] + B[6] + B[7]

                else:
                    print('Ошибка в дате')
            if (C[0] == '') and (C[1] == '') and (C[2] == ''):
                print('Ошибка в дате или дата не введена')
            return C


def find_time(A):
    C = ['', '', '']
    for i in range(0, len(A), 1):  # Находим время (типа 21:10 или 10:22)
        B = A[i]
        x = 0
        for j in range(0, len(B), 1):
            if B[j] == ':':
                x = 1
        for j in range(0, len(B), 1):
            if (B[j] != ':') and (B[j].isnumeric() == False):  # Проверка: является ли символ (строка) числом
                x = 0
        if x == 1:
            if len(B) == 5:
                if B[2] == ':':
                    C[0] = B[0] + B[1]
                    C[1] = B[3] + B[4]
                    C[2] = True
                else:
                    print('Неправильно указан формат времени')
            if (C[0] == '') and (C[1] == ''):
                print('Неправильно указан формат времени')
            return C
    return C


def FIND(s, M):
    A = deсover_string(s)
    Word = find_word_data(A, Days)
    M[2] = Word
    if M[2] == '':
        C = find_month(A, Months)
        M[0] = C[0]
        M[1] = C[1]
        M[2] = C[2]

    if M[0] == M[1] == M[2] == '':
        C = find_data(A)
        M[0] = C[0]
        M[1] = C[1]
        M[2] = C[2]
    print(A)
    C = find_time(A)
    if C[0] != '':
        M[3] = C[0]
        M[4] = C[1]
    return M


s0 = 'полить цветы 21.12.20 в 10:45'
print(s0)
# A = ['Пойти', 'гулять', '10', 'декабря', '2023', 'завтра', '10:56', '21.12.23']
G = FIND(s0, List_of_Doing)
print(G)
# See PyCharm help at https://www.jetbrains.cm/help/pycharm/
# quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
