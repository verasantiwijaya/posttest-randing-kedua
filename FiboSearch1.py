#fungsi sorting dataset menggunakan MergeSort
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #variable mecah list
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

#fungsi mencari element x memakai FibonacciSearch
def fib(n):
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def Fibonaccisearch(arr,x):
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        print("Current Element : ",arr[i])
        if (x > arr[i]):
            n = n -1
            offset = i
        elif (x < arr[i]):
            n = n - 2
        else :
            return i
    if(fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1

#fungsi memisahkan antara list dan string
def sort_nested_dataset(dataset) :
    datasetsorted = []
    nesteddataset = {} 
    for i in range(len(dataset)) :
        if type(dataset[i]) == str :
            datasetsorted.append(dataset[i])
        else :
            nesteddataset[i] = mergesort(dataset[i])

    datasetsorted = mergesort(datasetsorted)

    for i in nesteddataset :
        datasetsorted.insert(i, nesteddataset[i])

    return datasetsorted
    

dataset = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
datasetsorted = sort_nested_dataset(dataset)
x = str(input("SILAHKAN MASUKKAN NAMA : "))

print(f"Dataset awal      : {dataset}\nDataset disorting : {datasetsorted}\n")

#index dan kolom dari element x
for index in range(len(datasetsorted)) :
    if type(datasetsorted[index]) == list :
        kolom = Fibonaccisearch(datasetsorted[index], x)
        if kolom != -1 : print(f'{x} berada di array index ke - {index} kolom {kolom}')
    else :
        if datasetsorted[index] == x : print(f'{x} berada di array index ke - {index}')