hour = 35 # 0-23
# Если Время между 7-11 утра, то доброе утро.
# Если время между 12-17 дня , то добрый день.
# Если время между 18-22 вечера , то добрый вечер.
# в остальных слкучаях - доброй ночи.
""" if hour > 23:
    hour = 23
if hour < 0:
    hour = 0
"""
if hour >= 7 and hour <=11:
    print('доброе утро.')
elif hour >= 12 and hour <= 17:
    print('добрый день.')
elif hour >= 18 and hour <= 22:
    print('добрый вечер.')
else:
    print('доброй ночи.')
if 7<= hour  <= 11:
        print('доброе утро.')
elif hour >= 12 and hour <= 17:
        print('добрый день.')
elif hour >= 18 and hour <= 22:
        print('добрый вечер.')
else:
        print('доброй ночи.')

    """
    1. Залогиниться в Github в браузере
    2. Создать нужный репозиторий
    3. В Pycharm зайти File - Settings - Github - нажать "+"
    4. Log via Github (связали Github c PyCharm)
    5. В созданном репозитории копируем путь к нему
    6. Заходим в ленточном меню Git - Manage Remotes,
    нажать "+" и вставить путь
    """


   """ prompt = Витязь на распутье
    Налево (L) пойдёшь, вольну-волю обретёшь...
    Направо (R) пойдёшь, коня потеряешь...
    Прямо пойдёшь (F), сыт и весел будешь...
    print(prompt)
    choice = input('Куда идём (L, R или F): ')
    if choice == 'L' or choice == 'l':
        print('Вольная воля')
    elif choice == 'R':
        print('Конь сбежал')
    elif choice == 'F':
        print('Сыт и весел')
    else:
        print('Выбор не понятен')
        """
a = 3
b = 5
print('до:')
print('a =', a, 'b =', b)
temp = a
a = b
b = temp