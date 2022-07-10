# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print('Hello world')
print('Добро пожаловать в умный календарь')
s0= ' '
Days_B = ['сегодня', 'Завтра', 'Послезавтра', 'Понедельник', 'Понедельника', 'Понедельнику', 'Понедельником', 'Понедельнике', 'Понедельники', 'Понедельников', 'Понедельникам', 'Понедельниками', 'Понедельниках', 'Вторник', 'Вторника', 'Вторнику', 'Вторником', 'Вторнике', 'Вторники', 'Вторников', 'Вторнику', 'Вторниками', 'Вторниках', 'Среда', 'Среды', 'Среде', 'Среду', 'Средой', 'Сред', 'Средам', 'Средами', 'Средах', 'Четверг', 'Четверга', 'Четвергу', 'Четвергом','Четверге', 'Четверги', 'Четвергов', 'Четвергам', 'Четвергами','Четвергах', 'Пятница', 'Пятниц', 'Пятнице', 'Пятницу', 'Пятницой', 'Пятницы', 'Пятницам','Пятницами','Пятницах', 'Суббота', 'Субботы', 'Субботе', 'Субботу', 'Субботой', 'Суббот', 'Субботам', 'Субботами', 'Субботах', 'Вокресенье', 'Вокресенья', 'Вокресенью', 'Вокресеньем', 'Вокресений', 'Вокресеньям', 'Вокресеньями', 'Вокресеньях']
Days_S = Days_B
for i in range(0, len(Days_S), 1):
    Days_S[i] = Days_S[i].lower()
#Year = ['День,']
def deсover_string(s):
    A = list()
    j = 0
    x = len(s)
    A.append(' ')
    for i in range(0, x, 1):
        if s[i] != ' ':
            A[j] = A[j] + s[i]
        else:

            q=A[j].split()
            A[j]=''.join(q)

            j = j + 1
            A.append(' ')

    q = A[j].split()
    A[j] = ''.join(q)
    return A

def find_word(s, etalon):
    x = 0
    print(s[0], '-')
    print(etalon[0], '-')
    for j in range(0, len(s), 1):
        for i in range(0, len(etalon), 1):
            if s[j] == etalon[i]:
                x = 1
                word = etalon[i]
    if x == 0:
        print('Не найдено слова, обозначающего дату')
        word = 'n'
    return word




s0 = 'Сегодня полить цветы'
Time = list()
Time = deсover_string(s0)
for i in range(0, len(Time), 1):
    Time[i] = Time[i].lower()
print(Time)
W = 'None'
W = find_word(Time, Days_B)
print(W)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
