name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32
weight = 92.
# 1 cпособ(плейсхолдеры)
# %s - string
# %d - digit (целое число)
# %f - float
print('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))

#2 способ
print('Имя: {}, E-mail: {}, Возраст: {}'.format(name, email,age))
#3 cспособ
print(f'Имя: {name}, E-mail: {email}, Возраст: {age}, Вес: {weight:.3f}')

name: Игорь
email: aaa@bbb.ru
age: 32
weight: 92.

