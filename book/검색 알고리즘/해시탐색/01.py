def hash_search(arr, x):
    k = x % len(arr)
    while arr[k] is not 0:
        if arr[k] is x:
            return k
        else:
            k = (k+1) % len(arr)
    return 'Not Found'

array_d = [12, 25, 36, 20, 30, 8, 42]
array_h = hash_table(array_d)
print(array_h)
print(hash_search(array_h, 8))