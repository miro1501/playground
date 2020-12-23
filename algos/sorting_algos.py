import time

"""
Bubble Sort Applications
--------------------------------------------------
Bubble sort is used in the following cases where:
1. the complexity of the code does not matter.
2. a short code is preferred.
"""
def bubbleSort(data):
    for i in range(len(data)):
        #print("----> ", data[i])
        for j in range(len(data)-i-1):
            if data[j]>data[j + 1]:
                (data[j],data[j+1]) = (data[j+1], data[j])

    print("Sorted list with bubble sort: ", data)




data = [-2, 45, 0, 11, -9]
print("Executing bubble sort") 
print("--------------------") 
start_time = time.time()
bubbleSort(data)
end_time = time.time()
print("time --> ", end_time-start_time)