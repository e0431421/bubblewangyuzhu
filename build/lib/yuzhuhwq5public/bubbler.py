def bubbleSort(arr):
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# #testing
# arr = [31, 2, 11, 23, 8, 7, 11,14,20]
 
# bubbleSort(arr)
 
# print ("sorted:")
# for i in range(len(arr)):
#     print ("%d" %arr[i]),
