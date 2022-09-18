from random import randint
 
array = [randint(-5, 30) for i in range(30)]
pos_1 = 0
pos_2 = 0
for i in range(len(array)):
    if pos_1 and pos_2:
        break
    elif array[i] > 0 and not pos_1:
        pos_1 = i
    elif array[i] > 0 and not pos_2:
        pos_2 = i
 
modified_array = [i for i in array if i] + [0] * array.count(0)
 
print(f'Максимальный по модулю: {max(array, key=abs)}')
print(f'Сумма между: {sum(array[i] for i in range(pos_1, pos_2 + 1))}' if pos_1 and pos_2 else 'В массиве один или ноль положительных элементов')
print(f'Массив со смещением нулей: {modified_array}')
