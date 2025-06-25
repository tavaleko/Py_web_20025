a = input('Введите слово менее четырёх букв')

if len(a) <= 4:
    print('слово меньше четырёх букв')

else:
    print('слово больше четырех букв')

word = input('Ввведите слово для анализа длинны или словослишком короткое ')
if not word or len(word) <4 :
    print('Вы ни чего не ввели')
if len(word) > 3:
    print('Длина слова "' + word + '"=' , len(word) )

a = len(str('"Привет"'))
print(a)