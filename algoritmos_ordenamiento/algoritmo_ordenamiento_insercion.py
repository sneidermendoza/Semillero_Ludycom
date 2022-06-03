def insertion_sort(array):
    for i in range(1, len(array)):
        posicion_actual = array[i]
        j = i-1
        while j >= 0 and array[j]> posicion_actual:
            array [j+1] = array[j]
            j -= 1
        array[j+1] = posicion_actual
    return array

array =[5, 3, 4, 8, 7, 5, 1, 2, 3]
a = insertion_sort(array)
print(a)