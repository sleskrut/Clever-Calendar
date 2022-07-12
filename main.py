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
Days = ['сегодня', 'Завтра', 'Послезавтра', 'Понедельник', 'Понедельника', 'Понедельнику', 'Понедельником', 'Понедельнике', 'Понедельники', 'Понедельников', 'Понедельникам', 'Понедельниками', 'Понедельниках', 'Вторник', 'Вторника', 'Вторнику', 'Вторником', 'Вторнике', 'Вторники', 'Вторников', 'Вторнику', 'Вторниками', 'Вторниках', 'Среда', 'Среды', 'Среде', 'Среду', 'Средой', 'Сред', 'Средам', 'Средами', 'Средах', 'Четверг', 'Четверга', 'Четвергу', 'Четвергом','Четверге', 'Четверги', 'Четвергов', 'Четвергам', 'Четвергами','Четвергах', 'Пятница', 'Пятниц', 'Пятнице', 'Пятницу', 'Пятницой', 'Пятницы', 'Пятницам','Пятницами','Пятницах', 'Суббота', 'Субботы', 'Субботе', 'Субботу', 'Субботой', 'Суббот', 'Субботам', 'Субботами', 'Субботах', 'Вокресенье', 'Вокресенья', 'Вокресенью', 'Вокресеньем', 'Вокресений', 'Вокресеньям', 'Вокресеньями', 'Вокресеньях']
for i in range(0, len(Days), 1):
     Days[i] = Days[i].lower()  # Понижение регистра первой буквы
#Year = ['День,']
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
            A[j]=''.join(q)

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
        print('Ошибка даты. В предложении 2 и более слов обозначающих дату. Введите предложение с одним таким словом')
        word = ''
    if x == 0:
        print('Не найдено слова, обозначающего дату')
        word = '0'
    return word

s0 = 'Сегодня полить цветы'

List_of_words = deсover_string(s0)
for i in range(0, len(List_of_words), 1):
    List_of_words[i] = List_of_words[i].lower()
print(List_of_words)

Word = find_word(List_of_words, Days)
print(Word)

s00 = s0
s00 = s00.lower()

for i in range(0, len(s00), 1):
    if s00[i] == Word:
       del s00[i]
print(s00)

List_of_Doing = ['', '', '', '', '', '', '']


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
