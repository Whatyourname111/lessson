# a = int(input())
# b = int(input())
# while a <= b:
#     print(a)
#     a = a + 1



 #a = []1
# for i in range (1,101):
 #    a.append(i)
#
# for i in range(1,101):
#     if i % 2 !=0:
#         a.remove(i)
# print(a)
#
# for i in range(1,101):
#     a.append(i)
#     if i % 2 == 0:
#         a.remove(i)
# # print(a)

# a = int(input("a:"))
# b = int(input("b:"))

# for i in range(a , b+1 , 1):
#     print(i)

# a = int(input("a:"))
# b = int(input("b:"))
# if a < b:
#     print(b)
# else:
#     print("a кичинекей болушу шарт")



# try:
#     a = int(input("a:"))
#     b = int(input("b:"))
#     if a < b:
#         for i in range(a, b+1, 1 ):
#             print(i)
#     else:
#         print("a саны b санынан кичине болушу керек")
# except:
#     print("тамга емес сан болушу шарт")

################алгоритм сортировка пузыроков#########################
# def bSort(array):
#     length = len(array)
#     for i in range(length):
#         for j in range(0, length-i-1):
#             if array[j] > array [j +1]:
#                 if array[j] > array[j+1]:
#                     temp = array[j]
#                     array[j] = array[j+1]
#                     array[j+1] = temp

# array = [3,4,6,7,5,3,2,4,6,8]
# bSort(array)
# print(array)


def sel_sort(row):
    n = len(row)
    for i in range(n-1):
        m = i
        for i in range (i +1,n):
            if row[j] < row[m]:
                m = j 
        temp = row[i]
        row[i] = row[m]
        row[m] = temp
    print(row)
row = [6,3,2,1,3,9,5]
sel_sort(row)
print(a)
