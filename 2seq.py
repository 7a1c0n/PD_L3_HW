# Предполагается корректный ввод!

str_nums = input('Введите цифры через разделитель ( , | ; | / ): ')
# Промежуточный список из цифр-строк
lst_str_nums = str_nums.split(str_nums[1])
# список из цифр
lst_nums = []
for _ in lst_str_nums:
    lst_nums.append(int(_))
# список из уникальных цифр
uniq_nums = []
for _ in lst_nums:
    if _ not in uniq_nums:
        uniq_nums.append(_)
print('Уникальные цифры из введенного набора:', uniq_nums)
