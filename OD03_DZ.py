
# Пузырькова сортировка
mas1 = [7,6,10,5,9,8,3,4]
mas = mas1
n = len(mas)
iter1 = 0
iter3 = 0
while iter1 < n:
    iter2 = 0
    while iter2 < n - iter1 -1 :
        if mas[iter2] > mas[iter2 + 1]:
            mas[iter2], mas[iter2 + 1] = mas[iter2 + 1], mas[iter2]
        iter2 = iter2 + 1
        iter3 = iter3 + 1
    iter1 = iter1 + 1
print("Пузырьковая сортировка:")
print(f"массив {mas}")
print(f"Количество итераций: {iter3}\n")

# Быстрая сортировка
mas1 = [7,6,10,5,9,8,3,4]
iter1 = 0
def quicksort(array):
    global iter1
    iter1 += 1  # Увеличиваем счетчик на каждой итерации
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print("Быстрая сортировка:")
print(f"массив {quicksort(mas1)}\n")
print(f"Количество итераций: {iter1}\n")

# Сортировка выбором
mas1 = [7,6,10,5,9,8,3,4]
iter1 = 0
for i in range(len(mas1)):
    min = i
    for j in range(i + 1, len(mas1)):
        iter1 = iter1 + 1
        if mas1[j] < mas1[min]:
            min = j
    mas1[i], mas1[min] = mas1[min], mas1[i]
print("Сортировка выбором:")
print(f"массив {mas1}")
print(f"Количество итераций: {iter1}\n")

# Сортировка вставками
mas1 = [7,6,10,5,9,8,3,4]
iter1 = 0
for i in range(1, len(mas1)):
    j = i
    while j > 0 and mas1[j - 1] > mas1[j]:
        iter1 = iter1 + 1
        mas1[j], mas1[j - 1] = mas1[j - 1], mas1[j]
        j = j - 1
print("Сортировка вставками:")
print(f"массив {mas1}")
print(f"Количество итераций: {iter1}\n")




