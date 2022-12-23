# Предполагается корректный ввод!

# список из обоих списков
lsts = [[], []]
# поочередное заполнение списков
for i in range(2):
    str_nums = input(f'Введите элементы {i + 1}-го списка через ",": ')
    # Промежуточный список из цифр-строк
    lst_str_nums = str_nums.split(',')
    # список из цифр
    for _ in lst_str_nums:
        lsts[i].append(int(_))
# проверка и удаление
for i in lsts[1]:
    # удаление всех возможных вхождений
    while lsts[0].count(i) > 0:
        lsts[0].remove(i)
print('Результат:', str(lsts[0])[1:-1].replace(' ', ''))
