#######################Рекурсия-оз озун кайтало##################
# def f (n):
    # if n == 1:
        # return 1
    # return n - f(n-1)
# print(f(100))


# def f (n):
#      print(n)
#      if n == 100:
#          return 100
#      return f(n+1)
# print(f(1))#        

# # a = 1
# # b = 0
# # c = 0

# # try:
# #     c = a/b
# #     print(c)
# # except ZeroDivisionError:
# #     print("0 саны болунбойт")


# def miner (a,b,c):
#     if a > b and a > c:
#         print("a")
#     elif b > a and b > c:
#         print("b")
#     else:
#         print("с")

    
# a = int(input('a'))
# b = int(input('b'))
# c = int(input('c'))

# print(miner(a,b,c))
 


# a = [2,3,4,5,6,5,4,3,2,6,7,5,67,7,67,6,655,4,4,333,22,2,2,2,2,2,2,2,2,2,2,2]
 

 #     колдонучу x =3 саныын ьергенде экра\нга 3 эгерде бир дагы эллемень жок болсо
#                 #табылган жок билдиру чыксын

# def rrrr(array):

#     for i in range(len(array)):
#         if array[i] == b:
#             print(b)
#         else:
#             print("ошибка ощибка ощибка")

# b = int(input())

# array = [1,2,3,4,5,5,5,55,6,677,8,]
# # print(array)
    
# a = [ 2,3,4,5,6,7,8,6,3,233,44,5,6,2,]
# x = int(input("x;"))

# for i in range (len(a)):
#     if a[i] == x:
#         print(f"сиш ср")


# my_list = [11,22,3,4,4,56,6,779,99,88,7,66,55,44,3]
# result = []
# min_element = 15
# max_element = 50 
# for i in my_list:
#     if i < min_element  or i > max_element:
#         result.append(i)

# print(result)

""" with open (*бул жерде файлдын аты " " бул жерге режим корсотулот)as file:
open бул файлдар менен иштоо даяр функция 
my_file обектиге берилген ат режимди 3 туру бар
1 "w" бул соз (write) жазуу учун ачканда колдонобуз
2 "r" бул соз (read) оку учун колдонбуз
3 "a" бул соз (append) маалыматы кошуу учун колдонобуз


"""

# with open(r"C:\Users\Acer\PycharmProjects\leason2\leeee\mirbek.txt", "r") as file:
#     text = ("salam Mirbek !!!")
#     result = file.readlines()
#     for element in result:
#         for element in result:
#             if element == text:
#                 print(f"six idegen file bar!{element}")

# print(element)

################файлды код менен ачуу####################

# with open ("minerr.txt", "w")as file :
#      file.write("AAAAAAAAAAAAAAAAAAAAAAAAAA\n")
#      file.write("ahaahahhahahaahahahahahahaahaahahaha\n")

##########################файлды кошшуу###############

# with open ("miner.txt","a")as file :
#     file.append("eeeeeeeeeeeeeeeeeeeee")
    
# def work_with_file(name, w):

#     with open (name, 'w') as file :

#         file.write(w)

# print(work_with_file("index.txt","salam Beka"))

def koshuu(a , b):
    result = a = b
    return result

        