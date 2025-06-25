from random import choice

temp = 37.7
print('Температура', temp,'-это много, это почти', int(temp)+1, '.')
a=4
if a == 5:
    print('а равно 5')
    print('Условие выполнийлось')
print('Вне условий')
print('Витязь на распутье')
print('Налево (L) пойдешь, вольную-волю обретешь...')
print('Направо (R) пойдешь, коня потеряешь...')
print('Прямо (F) пойдешь, сыт и весел будешь...')
choice = input ('Куда идем (L, R или F): ')
if choice == 'L' or choice == 'l' :
    print('вольную-волю обретешь')
elif choice == 'R' or choice == 'r' :
    print('коня потеряешь')
elif choice == 'F' or choice == 'f' :
    print('сыт и весел будешь')
else:
    print('выбор не ясен')
print('one')
