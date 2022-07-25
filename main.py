# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.


import calendar
import datetime
from datetime import timedelta


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

print('Hello world')
print()
print('Добро пожаловать в умный календарь')

today = datetime.datetime.today()
s0 = ' '  # Далее объявляются ключевые массивы
Word = 'None'
List_of_words = list()
List_of_Doing = ['', '', '', '', '', '', '', '', '', '']
Days = ['Позавчера', 'Вчера', 'Сегодня', 'Завтра', 'Послезавтра', 'Понедельник', 'Понедельника', 'Понедельнику',
        'Понедельником',
        'Понедельнике', 'Понедельники', 'Понедельников', 'Понедельникам', 'Понедельниками', 'Понедельниках', 'Вторник',
        'Вторника', 'Вторнику', 'Вторником', 'Вторнике', 'Вторники', 'Вторников', 'Вторнику', 'Вторниками', 'Вторниках',
        'Среда', 'Среды', 'Среде', 'Среду', 'Средой', 'Сред', 'Средам', 'Средами', 'Средах', 'Четверг', 'Четверга',
        'Четвергу', 'Четвергом', 'Четверге', 'Четверги', 'Четвергов', 'Четвергам', 'Четвергами', 'Четвергах', 'Пятница',
        'Пятниц', 'Пятнице', 'Пятницу', 'Пятницой', 'Пятницы', 'Пятницам', 'Пятницами', 'Пятницах', 'Суббота',
        'Субботы', 'Субботе', 'Субботу', 'Субботой', 'Суббот', 'Субботам', 'Субботами', 'Субботах', 'Вокресенье',
        'Вокресенья', 'Вокресенью', 'Вокресеньем', 'Вокресений', 'Вокресеньям', 'Вокресеньями', 'Вокресеньях']
Years = ['минута', 'минуты', 'минуту', 'минуте', 'минутой', 'минуте', 'минут', 'минутам', 'минутами', 'минутах', 'час',
         'часа', 'часу', 'часом', 'часе', 'часы', 'часов', 'часам', 'часами', 'часах', 'день', 'дня', 'дню', 'днём',
         'дне', 'дни', 'дней', 'дням', 'днями', 'днях', 'неделя', 'недели', 'неделе',
         'неделю', 'неделей', 'недель', 'неделям', 'неделями', 'неделях', 'месяц', 'месяца', 'месяцу', 'месяцем',
         'месяце', 'месяцы', 'месяцев', 'месяцы', 'месяцами', 'месяцах', 'год', 'года', 'году', 'годом', 'годе', 'годы',
         'лет']
Months = ['январь', 'января', 'январю', 'январём', 'январе', 'февраль', 'февраля', 'февралю', 'февралём', 'феврале',
          'март', 'марта', 'марту', 'мартом', 'марте',
          'апрель', 'апреля', 'апрелю', 'апрелем', 'апрелуи', 'май', 'мая', 'маю', 'маем', 'мае', 'июнь', 'июня',
          'июню', 'июнем', 'июне', 'июль', 'июля', 'июлю', 'июлем', 'июле', 'август', 'августа', 'августу', 'августом',
          'августе', 'сентябрь', 'сентября', 'сентябрю', 'сентябрём', 'сентябре', 'октябрь', 'октября', 'октябрю',
          'октябрём', 'октябре', 'ноябрь', 'ноября', 'ноябрю', 'ноябрём', 'ноябре', 'декабрь', 'декабря', 'декабрю',
          'декабрём', 'декабре']
Predlogs = ['в', 'на', 'к', 'с']
Every = ['каждый', 'каждого', 'каждому', 'каждым', 'каждом', 'каждая', 'каждой', 'каждую', 'каждое', 'каждые', 'каждых',
         'каждым', 'каждыми']
Week0 = ['пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос']
WEEK = ['неделя', 'недели', 'неделе',
        'неделю', 'неделей', 'недель', 'неделям', 'неделями', 'неделях']
Days0 = ['день', 'дня', 'дню', 'днём', 'дне', 'дни', 'дней', 'дням', 'днями', 'днях']
May0 = ['май', 'мая', 'маю', 'маем', 'мае']
Next = ['следующий', 'следующего', 'следующиму', 'следующим', 'следующей', 'следующая', 'следующей', 'следующую',
        'следующее', 'следующем']
Weekend = ['выходные', 'выходных', 'выходным', 'выходными']
Morning = ['утро', 'утра', 'утру', 'утром', 'утре']
Noon = ['полдень', 'полудня', 'полудню', 'полудни', 'полуней', 'полденем']
Evening = ['вечер', 'вечера', 'вечеру', 'вечером', 'вечере']
Night = ['ночь', 'ночи', 'ночью']
Month0 = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


def destroy_mistake(A):
    for i in range(0, len(A), 1):
        if (len(A[i]) == 1) and (A[i] != ' ') and (A[i] != '-') and (i != 9):
            A[i] = '0' + A[i]
    return A
def month_in_date(s):
    if (s.isnumeric() == False) and (s != ' '):
        if s in May0:
            s = 'май'
        s = s[0:3]
        match s:
            case 'янв':
                s = '01',
            case 'фев':
                s = '02',
            case 'мар':
                s = '03',
            case 'апр':
                s = '04',
            case 'май':
                s = '05',
            case 'июн':
                s = '06',
            case 'июл':
                s = '07',
            case 'авг':
                s = '08',
            case 'сен':
                s = '09',
            case 'окт':
                s = '10',
            case 'ноя':
                s = '11',
            case 'дек':
                s = '12'
        tuple_in_str_char(s)
    return s


def plus_minute(n, k):
    if n == None:
        n = datetime.datetime.today()
    p = n + timedelta(minutes=k)
    return p


def plus_hour(n, k):
    if n == None:
        n = datetime.datetime.today()
    p = n + timedelta(hours=k)
    return p


def plus_day(n, k):
    if n == None:
        n = datetime.datetime.today()
    p = n + timedelta(days=k)
    return p


def plus_week(n, k):
    if n == None:
        n = datetime.datetime.today()
    p = n + timedelta(weeks=k)
    return p


def plus_month(n, k):
    if n == None:
        n = datetime.datetime.today()
    date = n
    for i in range(0, k, 1):
        days_in_month = calendar.monthrange(date.year, date.month)[1]
        date += timedelta(days=days_in_month)
    return date


def plus_year(n, k):
    if n == None:
        n = datetime.datetime.today()
    date = n
    for j in range(0, k, 1):
        for i in range(0, 12, 1):
            days_in_month = calendar.monthrange(date.year, date.month)[1]
            date += timedelta(days=days_in_month)
    return date


def tuple_in_str(M):
    for i in range(0, len(M), 1):
        if type(M[i]) == tuple:
            M[i] = list(M[i])
            p = M[i]
            M[i] = p[0]
    return M


def tuple_in_str_char(m):
    if type(m) == tuple:
        m = list(m)
        p = m
        m = p[0]
    return m


def weekday_of_today(A):
    k = datetime.datetime.today()
    x = k.weekday()
    match A[6]:
        case 'сег':
            A[2] = '+0',
        case 'зав':
            A[2] = '+1',  # Возвращает + день
        case 'пос':
            A[2] = '+2'
    match A[6]:
        case 'пон':
            y = 0,
        case 'вто':
            y = 1,
        case 'сре':
            y = 2,
        case 'чет':
            y = 3,
        case 'пят':
            y = 4,
        case 'суб':
            y = 5,
        case 'вос':
            y = 6
    if (A[6] != 'сег') and (A[6] != 'зав') and (A[6] != 'пос'):
        y = tuple_in_str_char(y)
        n = 0
        if x == y:
            n = 7
        while x != y:
            k = plus_day(k, 1)  # Возвращает в массив день недели после прибавления дней
            x = k.weekday()
            n = n + 1
        A[2] = '+' + str(n)

    return A


def weekday_of_massived_data(A):
    match A[6]:
        case '0':
            y = 'пн',
        case '1':
            y = 'вт',
        case '2':
            y = 'ср',
        case '3':
            y = 'чт',
        case '4':
            y = 'пт',
        case '5':
            y = 'сб',
        case '6':
            y = 'вс'
    y = tuple_in_str_char(y)  # Возвращает в массив день недели
    A[6] = y
    return A



def format_data_in_massiv(n):
    A = ['', '', '', '', '', '']
    A[0] = n.year
    A[1] = n.month
    A[2] = n.day
    A[3] = n.hour
    A[4] = n.minute
    A[5] = n.weekday()
    for i in range(0, len(A), 1):
        A[i] = str(A[i])
    if len(A[1]) == 1:
        A[1] = '0' + A[1]
    if len(A[2]) == 1:
        A[2] = '0' + A[2]
    if len(A[3]) == 1:
        A[3] = '0' + A[3]
    if len(A[4]) == 1:
        A[4] = '0' + A[4]  # Переводит значения типа дата в массив
    return A


Today = format_data_in_massiv(today)


def format_massiv_in_data(A):
    if (A[2] != '+0') and (A[2] != '+1') and (A[2] != '+1'):
        k = datetime.datetime(int(A[0]), int(A[1]), int(A[2]), int(A[3]), int(A[4]))
    if A[2] == '+0':
        k = datetime.datetime.today()
    if A[2] == '+1':
        k = datetime.datetime.today()
        k = plus_day(k, 1)
    if A[2] == '+2':
        k = datetime.datetime.today()
        k = plus_day(k, 2)  # Переводит значения массива в тип дата
    return k


def cover_string(A):  # Функция собирает отдельные элементы обратно в строку
    S = ' '
    for i in range(0, len(A), 1):
        if A[i] != ' ':
            S = S + A[i]
            S = S + ' '
    return S


def low(s):  # Понижение регистра всех букв
    for i in range(0, len(s), 1):
        s[i] = s[i].lower()
    return s


low(Days)


def inf(A):
    p = ''
    for i in range(0, len(A), 1):
        if (A[i] not in Days) and (A[i] not in Years) and (A[i] not in Months) and (A[i] not in Every) and (
                A[i].isnumeric() == False) and (
                A[i] != 'через') and (A[i] not in Next) and (A[i] not in Morning) and (A[i] not in Noon) and (
                A[i] not in Evening) and (A[i] not in Night):
            B = A[i]
            if len(B) >= 3:
                if (B[2] != '.') and (B[2] != ':') and (B[1] != ':'):
                    p = p + B
                    p = p + ' '
            elif (A[i] in Predlogs) and (i != len(A) - 1):
                if (A[i + 1] not in Days) and (A[i + 1] not in Years) and (A[i + 1] not in Months) and (
                        A[i + 1].isnumeric() == False):
                    B = A[i + 1]
                    C = A[i]
                    if len(B) >= 3:
                        if (B[2] != '.') and (B[2] != ':') and (B[1] != ':'):
                            p = p + C
                            p = p + ' '  # Вычленяет информацию о задаче

    p = p.strip()
    return p


def deсover_string(s):
    A = list()
    j = 0
    x = len(s)
    A.append(' ')  # Функция разбивает предложение на слова
    for i in range(0, x, 1):
        if s[i] != ' ':
            A[j] = A[j] + s[i]  # Заполнение j-го элемента массива слов
        else:

            q = A[j].split()  # Переход к следующему элементу массива слов
            A[j] = ''.join(q)

            j = j + 1
            A.append(' ')

    q = A[j].split()
    A[j] = ''.join(q)
    return A  # Массив из слов (от пробела до пробела или конца функции)


def find_through_every(A, M):  # Находит слова типа "через неделю", "через 3 дня" и т.д
    y = -1
    for i in range(0, len(A), 1):
        if (A[i] == 'через') or (A[i] in Every):
            y = i
    if y != -1:
        if y <= len(A) - 3:
            ch1 = A[y + 1]
            ch2 = A[y + 2]
            if ch1.isnumeric() == True:
                if ch2 in Years:
                    match ch2[0]:
                        case 'ч':
                            M[3] = '+' + A[y + 1]
                            M[8] = 'час',
                        case 'д':
                            M[2] = '+' + A[y + 1]
                            M[8] = 'ден',
                        case 'н':
                            M[2] = '+' + str(7 * int(A[y + 1]))
                            M[8] = 'нед',
                        case 'м':
                            if ch2[1] == 'е':
                                M[1] = '+' + A[y + 1]
                                M[8] = 'мес'
                            if ch2[1] == 'и':
                                M[4] = '+' + A[y + 1]
                                M[8] = 'мин',
                        case 'г':
                            M[0] = '+' + A[y + 1]
                            M[8] = 'год',
                        case 'л':
                            M[0] = '+' + A[y + 1]
                            M[8] = 'лет'
        if y == len(A) - 2:
            ch2 = A[y + 1]
            if ch2 in Years:
                match ch2[0]:
                    case 'ч':
                        M[3] = '+1',
                    case 'д':
                        M[2] = '+1',
                    case 'н':
                        M[2] = '+7',
                    case 'м':
                        if ch2[1] == 'е':
                            M[1] = '+1'
                        if ch2[1] == 'и':
                            M[4] = '+1',
                    case 'г':
                        M[0] = '+1',
                    case 'л':
                        M[0] = '+1',
                    case _:
                        print('Не найдено слова "через" или люобй падежной формы (или рода) слова "каждый"')
        tuple_in_str(M)

        for i in range(0, len(A), 1):
            if A[i] in Every:
                M[7] = 'повтор'
                if (y <= len(A) - 4) and (A[i + 1].isnumeric() == True):
                    M[9] = A[i + 2]
                    M[8] = A[i + 3]
                    G = M[8]
                    M[8] = G[0:3]
                    if G[0] == 'г':
                        M[8] = 'лет'
                    if G[0] == 'д':
                        M[8] = 'дней'
                    if G[0] == 'н':
                        M[8] = 'дней'
                        M[9] = str(7 * int(A[y + 1]))
                if y == len(A) - 2:
                    if A[i + 1] in Years:
                        M[8] = A[i + 1]
                        M[9] = '1'
                        G = M[8]
                        M[8] = G[0:3]
                        if G[0] == 'г':
                            M[8] = 'лет'
                        if G[0] == 'д':
                            M[8] = 'дней'
                        if G[0] == 'н':
                            M[8] = 'дней'
                            M[9] = '7'
                    if A[i + 1] in Days:
                        M[8] = 'дней'
                        M[9] = '7'

    return M


def find_word_data(s, etalon):
    x = 0
    for j in range(0, len(s), 1):  # Находим ключевые слова (сегодня, завтра и т. п)
        for i in range(0, len(etalon), 1):
            if s[j] == etalon[i]:
                x += 1
                word = etalon[i]

    if x >= 2:
        print('Ошибка даты. В предложении 2 и более слов, обозначающих дату. Введите предложение с одним таким словом')
        word = ''
    if x == 0:
        # print('Не найдено слова, обозначающего дату')
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
        #print('Не найдено слова, обозначающего дату')
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
            if (len(B) == 5) or (len(B) == 4):
                if B[2] == ':':
                    C[0] = B[0] + B[1]
                    C[1] = B[3] + B[4]
                    C[2] = True
                elif B[1] == ':':
                    C[0] = B[0]
                    C[1] = B[2] + B[3]
                else:
                    print('Неправильно указан формат времени')
            if (C[0] == '') and (C[1] == ''):
                print('Неправильно указан формат времени')
            return C
    return C


def change_plus(
        A):  # переводит строку в дату, если была использована вункция find_through или в строке было слово сегодня, завтра или послезавтра
    k = datetime.datetime.today()
    if A[6] == 'сег':
        k = plus_day(k, 0)
    if A[6] == 'зав':
        k = plus_day(k, 1)
    if A[6] == 'пос':
        k = plus_day(k, 2)
    if A[6] in Week0:
        A[6] = ''
        A[8] = 'ден'
    if A[8] in Days0:
        A[8] = 'ден'

    for i in range(0, len(A), 1):
        B = A[i]
        if A[i] != '':
            if B[0] == '+':
                x = B[1]
                for j in range(2, len(B), 1):
                    x = x + B[i]
                x = int(x)
                y = A[8]
                if y == 'мин':
                    k = plus_minute(today, x)
                if y == 'час':
                    k = plus_hour(today, x)
                if y == 'ден':
                    k = plus_day(today, x)
                if y == 'нед':
                    k = plus_day(today, x)
                if y == 'мес':
                    k = plus_month(today, x)
                if y == 'год':
                    k = plus_year(today, x)
                if y == 'лет':
                    k = plus_year(today, x)
                K = format_data_in_massiv(k)
                for z in range(0, 5, 1):
                    A[z] = K[z]
                    A[6] = K[5]
                    A = weekday_of_massived_data(A)
                    if A[7] == 'нет повтора':
                        A[8] = '-'

    return A


def reduct_date(A):  # Находит ближайшую дату, если введены не все параметры
    if (A[3] == '') or (A[4] == ''):
        A[3] = A[4] = '00'
    if (A[1].isnumeric() == False) and (A[1] != ''):
        A[1] = month_in_date(A[1])
    tuple_in_str(A)
    if A[0] == A[1] == A[2] == '':
        A[0] = str(today.year)
        A[1] = str(today.month)
        A[2] = str(today.day)
        A[6] = str(today.weekday())
        k = format_massiv_in_data(A)
        if k < today:
            k = plus_day(k, 1)
    if A[0] == A[1] == '':
        A[0] = str(today.year)
        A[1] = str(today.month)
        k = format_massiv_in_data(A)
        if k < today:
            k = plus_month(k, 1)
    if A[0] == '':
        A[0] = str(today.year)
        k = format_massiv_in_data(A)
        if k < today:
            k = plus_year(k, 1)
    if 'k' in locals():
        A[0] = str(k.year)
        A[1] = str(k.month)
        A[2] = str(k.day)
        A[6] = str(k.weekday())
        A = weekday_of_massived_data(A)

    return A


def weekday_0(A):
    if A[3] == A[4] == '':
        A[3] = A[4] = '00'
    k = format_massiv_in_data(A)
    n = k.weekday()
    A[6] = str(n)
    return A


def reduct_next(A):
    for i in range(0, len(A), 1):
        if A[i] in Next:
            A[i] = '1'
            A[i - 1] = 'через'
    return A


def plus_one_weekend(s):
    A = deсover_string(s)
    for i in range(0, len(A), 1):
        if A[i] == 'через':
            A[i] = 'через 1'
        if A[i] in Every:
            A[i] = 'каждый 1'
        if A[i] in Weekend:
            A[i] = 'суббота'
    s = cover_string(A)
    return s


def check_daytime(s, A):
    E = deсover_string(s)
    for i in range(0, len(E), 1):
        if E[i] in Morning:
            A[3] = '09'
            A[4] = '00'
        if E[i] in Noon:
            A[3] = '12'
            A[4] = '00'
        if E[i] in Evening:
            A[3] = '16'
            A[4] = '00'
        if E[i] in Night:
            A[3] = '00'
            A[4] = '00'
    k = format_massiv_in_data(A)
    if k < today:
        print('Возможно, напоминание в прошлом')
        A[3] = str(today.hour)
        A[4] = str(today.minute)
    return A

def FIND(s,
         M):  # Общая функция, содержащяя в себе предыдущие. Получает на вход строку, выдаёт упорядоченный массив формата (год, месяц, день, час, минута, само действие}
    A = deсover_string(s)
    low(A)
    s = cover_string(A)
    s = plus_one_weekend(s)
    A = deсover_string(s)
    A = reduct_next(A)
    # A = destroy_mistake(A)
    if M[0] == M[1] == M[2] == M[3] == M[4] == M[6] == '':
        M = find_through_every(A, M)
        Word = find_word_data(A, Days)
        M[6] = Word
        B = M[6]
        M[6] = B[0:3]
        if M[6] != '':
            M = weekday_of_today(M)

    if M[0] == M[1] == M[2] == M[3] == M[4] == M[6] == '':
        C = find_month(A, Months)
        M[0] = C[0]
        M[1] = C[1]
        M[2] = C[2]

    if M[0] == M[1] == M[2] == '':
        C = find_data(A)
        if C != None:
            M[0] = C[0]
            M[1] = C[1]
            M[2] = C[2]
    C = find_time(A)
    if C[0] != '':
        M[3] = C[0]
        M[4] = C[1]
    if M[0] == M[1] == M[2] == M[3] == M[4] == M[6] == '':
        for i in range(0, len(A), 1):
            if A[i].isnumeric() == True:
                B = A[i]
                if len(B) == 2:
                    M[2] = B
                if len(B) == 4:
                    M[0] = B

    # if M[0] == M[1] == M[2] == M[3] == M[4] == M[6] == '':
    # print('Не введено даты или слов, указывающих на неё')
    M[5] = inf(A)
    if M[5] == '':
        print('Не введено задачи')
    elif M[7] == '':
        M[7] = 'нет повтора'
        if M[8] == '':
            M[8] = '-'
        M[9] = '-'
    L1 = M[3]
    L2 = M[4]
    M = change_plus(M)
    M = tuple_in_str(M)
    M = reduct_date(M)
    M = destroy_mistake(M)
    if M[6] == '':
        M = weekday_0(M)
        M = weekday_of_massived_data(M)
    if M[3] != L1:
        M[3] = L1
    if M[4] != L2:
        M[4] = L2
    if M[3] == M[4] == '':
        M[3] = M[4] = '00'
    M = check_daytime(s, M)
    if M[9] in Days:
        M[9] = '7'
    if (M[8] in Month0) or (M[8] in May0) or (M[9] in Months):
        M[8] = 'мес'
        M[9] = '1'
    for i in range(0, len(A) - 1, 1):
        if (A[i].isnumeric() == True) and (A[i + 1] in WEEK):
            M[8] = 'нед'
            M[9] = A[i]

    return M


def print_result_1(A):
    print('{"STATUS": SUCCESS , "TEXT":', A[5], '"PARAMS": {}, "DATE": {"year":', A[0], ', "month":', A[1], ', "day":',
          A[2],
          ', "hour":', A[3], ', "minute":', A[4], '}}')


def print_result_2(A):
    print('{"STATUS": SUCCESS , "TEXT":', A[5], '"PARAMS": {"WEEKDAY":', A[6], '}}')


def print_result_3(A):
    if A[8] == 'ден':
        print('{"STATUS": SUCCESS , "TEXT":', A[5], '"PARAMS": {}, "DATE": "hour":', A[3], ', "minute":', A[4],
              '"frequency"', A[9], '}}')
    if A[8] == 'мес':
        print('{"STATUS": SUCCESS , "TEXT":', A[5], '"PARAMS": {}, "DATE": "day":', A[2],
              ', "hour":', A[3], ', "minute":', A[4], '"frequency"', A[9], '}}')
    if (A[8] == 'год') or (A[8] == 'лет'):
        print('{"STATUS": SUCCESS , "TEXT":', A[5], '"PARAMS": {}, "DATE": "month":', A[1],
              ', "day":', A[2],
              ', "hour":', A[3], ', "minute":', A[4], '"frequency"', A[9], '}}')

print()
print('Сегодняшняя дата: ', today)
print()
s0 = input('Введите предложение, включающее дату и задачу ')
# s0 = 'Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01'
print(s0)
G = FIND(s0, List_of_Doing)
if G[5] != '':
    if G[7] == 'нет повтора':
        print_result_1(G)
    if ((G[8] == 'ден') and (G[9] == '7')) or ((G[8] == 'нед') and (G[9] == '1')):
        print_result_2(G)
    else:
        print_result_3(G)

# See PyCharm help at https://www.jetbrains.cm/help/pycharm/
# quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
