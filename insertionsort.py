import time

def insertion_sort(arr, draw_data, canvas, sort, count, i_count): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                count += 1
                i_count["text"] = f"{count}"
                draw_data(arr, canvas, sort, ['red' if x == j or x == j + 1 else 'blue' for x in range(len(arr))])
                time.sleep(0.5)
        arr[j+1] = key
    draw_data(arr, canvas, sort, ['red' for x in range(len(arr))])
