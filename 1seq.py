list_elems = []
for i in range(int(input('Введите количество элементов: '))):
    list_elems.append(input(f'Введите {i + 1}-й элемент: '))
list_elems.sort()
print('Список по возрастанию:', list_elems)


