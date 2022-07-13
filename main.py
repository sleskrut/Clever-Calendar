def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print('Hello world')
print('Добро пожаловать в умный календарь')
s0= ' ' #Далее объявляются ключевые массивы
Word = 'None'
List_of_words = list()
Days = ['Сегодня', 'Завтра', 'Послезавтра', 'Понедельник', 'Понедельника', 'Понедельнику', 'Понедельником', 'Понедельнике', 'Понедельники', 'Понедельников', 'Понедельникам', 'Понедельниками', 'Понедельниках', 'Вторник', 'Вторника', 'Вторнику', 'Вторником', 'Вторнике', 'Вторники', 'Вторников', 'Вторнику', 'Вторниками', 'Вторниках', 'Среда', 'Среды', 'Среде', 'Среду', 'Средой', 'Сред', 'Средам', 'Средами', 'Средах', 'Четверг', 'Четверга', 'Четвергу', 'Четвергом','Четверге', 'Четверги', 'Четвергов', 'Четвергам', 'Четвергами','Четвергах', 'Пятница', 'Пятниц', 'Пятнице', 'Пятницу', 'Пятницой', 'Пятницы', 'Пятницам','Пятницами','Пятницах', 'Суббота', 'Субботы', 'Субботе', 'Субботу', 'Субботой', 'Суббот', 'Субботам', 'Субботами', 'Субботах', 'Вокресенье', 'Вокресенья', 'Вокресенью', 'Вокресеньем', 'Вокресений', 'Вокресеньям', 'Вокресеньями', 'Вокресеньях']
#Year = ['день, дня, дню, днём',]
def low(s): # Понижение регистра всех букв
    for i in range (0, len(s), 1):
        s[i] = s[i].lower()
    return s
low(Days)
def inf(s, moment_word):
    for i in range(0, len(s), 1):
        if s[i] == moment_word:
            s[i] = ''
    return s
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

def find_word(s, etalon):
    x = 0
    for j in range(0, len(s), 1):  # Находим ключевые слова (сегодня, завтра
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


def cover_string(A):  # Функция собирает отдельные элементы обратно в строку
    S = ' '
    for i in range(0, len(A), 1):
        if A[i] != ' ':
            S = S + A[i]
            S = S + ' '
    return S

s0 = 'полить цветы сегодня'

List_of_words = deсover_string(s0)
List_of_words = low(List_of_words)
print(List_of_words)
Word = find_word(List_of_words, Days)
print(Word)

s00 = List_of_words
s00 = inf(s00, Word)
print(s00)
p = cover_string(s00)
print(p)
List_of_Doing = ['', '', '', '', '', '', '']


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
