#fungsi sorting dataset menggunakan MergeSort
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = []#list kosong untuk nampung nilai

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

#fungsi mencari element x memakai JumpSearch
def jumpSearch(arr, x):
    n = len(arr)
    step = int(n ** 0.5)

    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    while arr[prev] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev

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
        kolom = jumpSearch(datasetsorted[index], x)
        if kolom != -1 : print(f'{x} berada di array index ke - {index} kolom {kolom}')
    else :
        if datasetsorted[index] == x : print(f'{x} berada di array index ke - {index}')