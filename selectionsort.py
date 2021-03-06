import time

def selection_sort(arr, draw_data, canvas, sort, count, i_count):
    # Traverse through all array elements 
    for i in range(len(arr)): 
        
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)):
            count += 1
            i_count["text"] = f"{count}" # I put the count and update of count in the for loop since this is where the checks are happening
            
            if arr[min_idx] > arr[j]: 
                min_idx = j
                draw_data(arr, canvas, sort, ['green' if x == j or x == min_idx else 'blue' for x in range(len(arr))])
                time.sleep(0.5)
            else:
                draw_data(arr, canvas, sort, ['red' if x == j else 'blue' for x in range(len(arr))])
                time.sleep(0.5)

              
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_data(arr, canvas, sort, ['red' if x == i or x == min_idx else 'blue' for x in range(len(arr))])
        time.sleep(0.5)
    draw_data(arr, canvas, sort, ['red' for x in range(len(arr))])