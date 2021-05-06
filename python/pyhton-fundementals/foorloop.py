# # Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# #     Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# # 1
# # list=[-1, 3, 5, -5]
# # def PO(list):
# #     for i in range(0,len(list)):
# #         if (list[i]>0):
# #             list[i]="big"
# #         else:continue
# #     return list
# # print(PO(list))
# # 2
# # Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# # (Note that zero is not considered to be a positive number).
# #     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# #     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# # list=[1,6,-4,-2,-7,-2]
# # def Pos(list):
# #     count=0
# #     for i in range(0,len(list)):
# #         if (list[i]>0):
# #             count+=1
# #     list.pop()
# #     list.append(count)
# #     print(list)
# # Pos(list)

# # 3
# # Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# #     Example: sum_total([1,2,3,4]) should return 10
# #     Example: sum_total([6,3,-2]) should return 7
# # list=[1,2,3,4]
# # def SumL(list):
# #     numsum=0
# #     for i in range(0,len(list)):
# #         numsum+=list[i]
# #     return numsum
# # print(SumL(list))

# # 4
# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
# list=[1,2,3,4]
# def Avg(list):
#     numsum=0
#     for i in range(0,len(list)):
#         numsum+=list[i]
#     avg=numsum/len(list)
#     return avg
# print(Avg(list))

# 5
# Length - Create a function that takes a list and returns the length of the list.
#     Example: length([37,2,1,-9]) should return 4
#     Example: length([]) should return 0
# list=[1,2,3,4]
# def Length(list):
#     count=0
#     for i in list:
#         count+=1
#     return count
# print(Length(list))

# 6
# Minimum - Create a function that takes a list of numbers 
# and returns the minimum value in the list. If the list is empty, have the function return False.
#     Example: minimum([37,2,1,-9]) should return -9
#     Example: minimum([]) should return False
# list=[]
# def Minimum(list):
#     a=list[0]
#     for i in range(len(list)):
#         if(a > list[i]):
#             a=list[i]
#     return a
# print(Minimum([2,2,3,1]))

# 7
# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, 
# have the function return False.
#     Example: maximum([37,2,1,-9]) should return 37
#     Example: maximum([]) should return False
# list=[]
# def Maxmum(list):
#     a=list[0]
#     for i in range(len(list)):
#         if(a < list[i]):
#             a=list[i]
#     return a
# print(Maxmum([2,2,3,1]))

# 8
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
# list=[]
# def Ult(list):
#     numsum=0
#     a=list[0]
#     b=list[0]
#     count=0
#     for i in list:
#         count+=1
#         numsum+=list[i]
#         if(a < list[i]):
#             a=list[i]
#         if(b > list[i]):
#             b=list[i]
#     avg=numsum/len(list)
#     dic={'sumTotal': numsum, 'average': avg, 'minimum': b, 'maximum': a, 'length': 4}
#     return dic
# print(Ult([2,2,3,1]))

# 9
# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

#     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
# def Rev(x):
#     l=int(len(x)/2)
#     for i in range(0,l,1):
#         temp=x[i]
#         x[i]=x[len(x)-1-i]
#         x[len(x)-1-i]=temp
#     return x
# x=[5,4,8,-5,6]
# print(Rev(x))