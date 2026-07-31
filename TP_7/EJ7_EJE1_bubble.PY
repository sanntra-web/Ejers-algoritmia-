def bubble_sort_while(arr):
    n = len(arr)
    var_bool = True

    while var_bool:
        var_bool = False
        for j in range(0, n - 1):

            if arr[j] > arr[j + 1]:

                aux = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = aux

                var_bool = True

        n -= 1 

    return arr
def bubble_sort_for(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                aux = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = aux

    return arr