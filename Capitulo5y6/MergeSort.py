def merge_sort(arr):  
    if len(arr) > 1:  
        mid = len(arr) // 2  # Encontrar el punto medio  
        left_half = arr[:mid]  # Dividir en la mitad izquierda  
        right_half = arr[mid:]  # Dividir en la mitad derecha  

        merge_sort(left_half)  # Ordenar la mitad izquierda  
        merge_sort(right_half)  # Ordenar la mitad derecha  

        # Comenzar el proceso de combinación  
        i = j = k = 0  

        while i < len(left_half) and j < len(right_half):  
            if left_half[i] < right_half[j]:  
                arr[k] = left_half[i]  
                i += 1  
            else:  
                arr[k] = right_half[j]  
                j += 1  
            k += 1  

        # Copiar los elementos restantes, si hay alguno  
        while i < len(left_half):  
            arr[k] = left_half[i]  
            i += 1  
            k += 1  

        while j < len(right_half):  
            arr[k] = right_half[j]  
            j += 1  
            k += 1  

# Ejemplo de uso  
data = [38, 27, 43, 3, 9, 82, 10]  
merge_sort(data)  
print("Arreglo ordenado es:", data)