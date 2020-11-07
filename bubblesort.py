import time

def bubble_sort(arr, draw_data, canvas, sort):
    n = len(arr)   
    for i in range(n):  
        for j in range(0, n - i - 1): 
            if arr[j] > arr[j + 1] : 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                draw_data(arr, canvas, sort)
                time.sleep(0.2)
