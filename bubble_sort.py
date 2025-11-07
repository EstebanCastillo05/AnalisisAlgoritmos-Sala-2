def bubble_sort(arr):

    n = len(arr)

    sorted_arr = arr.copy()
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
                swapped = True
                
        if swapped == False:
            break

    return sorted_arr

if __name__ == "__main__":
    arr = [13, 5, 6, 20, 27,33, 5, 8, 10]
    
    print("Array original:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()
    
    sorted_arr = bubble_sort(arr)
    
    print("Array ordenado:")
    for i in range(len(sorted_arr)):
        print("%d" % sorted_arr[i], end=" ")
    print()
    
    print("Array original (debe ser igual al inicial):")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")