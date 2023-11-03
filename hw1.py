# Дан список целых чисел array. Необходимо написать в императивном стиле процедуру для сортировкий 
# числа в списке в порядке убывания. Можно использовать либой алгоритм сортировки


array = [123, 54, 756, 32, 43, 65]

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

print(array)





# Написать точно такую же процедуру, но в декларативном стиле
array1 = [13, 51, 7432, 332, 43, 5655]

array1 = sorted(array1)
array1.reverse()
print(array1)
