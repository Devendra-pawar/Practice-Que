# # Python Input and Output Exercises-

# Pynative
# # Exercise 1

# # n1 = int(input("1st no.="))
# # n2 = int(input("2st no.="))
# # ------------------------------------------------------------------------------
# # Exercise 2

# # a= ('my','name','is','Dev')
# # b= ('my','name','is','Devs')
# # c= input('name-')
# # d= input('surname-')
# # print('your full name is ' + c , d , sep='_')

# # ---------------------------------------------------------------------------
# # Exercise 3
# # num = 8
# # print('%o' % num)

# #------------------------------------------------------------------------------
# #Exercise 4

# # a= float(input('Enter the float No. '))
# # print('%.2f' %a)

# #---------------------------------------------------------------------------------
# #Exercise 5

# # a= []

# # for i in range(1,6):
# #      item = float(input("Enter number at location :"))
# #      a.append(item)

# # print(a)
# #-------------------------------------------------------------------------------------
# #Exercise 6-

# # a=open(r'C:\Users\kreez\Desktop\practice\test.txt', 'r' )


# # print(a.readlines())

# #                                                                    not done yet 
# #---------------------------------------------------------------------------------
# #Exercise 7

# # a= input('Enter three string ')
# # print(a)

# # str1, str2, str3 = input("Enter three string").split()
# # print('Name1:', str1)
# # print('Name2:', str2)
# # print('Name3:', str3)

# #------------------------------------------------------------------------------------
# #Exercise 8

# # totalMoney= 1000
# # quantity = 3
# # price = 450

# # aa= "I have {1} dollar so I can buy {0} football for {2} dollars." 
# # print(aa.format(quantity,totalMoney,price))
# # ---------------------------------------------
# #Exercise 9
# #Exercise 10
# #                                                                    Not done yet
# #------------------------------------------------------------------------------------




# #-------------------------------------------------------------------------------------
#                                 Next chapter
# #-------------------------------------------------------------------------------------





# # Python if else, for loop, and range() Exercises-

# #Exercise 1

# # a= 1
# # while  a<=10:
# #     print(a)
# #     a += 1
# # #----------------------------------------------------------------------------------
# #Exercise 2

# # for i in range(1,5+1):
# #     for j in range(1,i+1):
# #         print(j,end=' ')
# #     print("")
# #------------------------------------------------------------------------------------
#Exercise 3

# a= int(input("enter the number "))

# s= 0
# for i in range(1,a+1):
#      s+=i
# print(s)

# b= sum(range(1,a+1))
# print(b)

# ----------------------------------------------------------------------------------------
#Exercise 4

# a= int(input("enter the number "))

# for i in range(1,11):
#     print(i*a)
# ----------------------------------------------------------------------------------------
#Exercise 5

# n = [12, 75, 150, 180, 145, 525, 50]

# for i in n: 
#    if    i>500:
#          break
#    elif  i>150:
#          continue
#    elif  i%5==0:
#          print(i)
# ----------------------------------------------------------------------------------------
#Exercise 6

# n= 7586945
# c= 0 

# while n !=0:
#     n = n//10
#     c +=1
# print(c)
# ----------------------------------------------------------------------------------------
#Exercise 7

# n= 5
# k= 5
# for i in range(0,n):
#     for j in range(k-i,0,-1):
#          print(j,end=" ")
#     print()
#                                                                          look again
# ----------------------------------------------------------------------------------------- 
#Exercise 8

# l1 = [10, 20, 30, 40, 50]

# s= len(l1) -1
# for i in range(s,-1,-1):
#     print(l1[i])
# ----------------------------------------------------------------------------------------
#Exercise 9 

# a= -10
# for i in range(a,0,1):
#     print(i)
# ----------------------------------------------------------------------------------------
#Exercise 10

#
#   for i in range(5):
#     print(i)
#  else:
#          print("done")
# -----------------------------------------------------------------------------------------
#Exercise 11

# s= 25
# e= 50 
# for i in range(s,e+1):
#     if i>1:
#         for j in range(2,i):
#             if (i%j)==0:
#                 break 
#         else:
#                print(i)
# -------------------------------------------------------------------------------
#Exercise 12

# a= 10
# f=0
# s=1
# for i in range(0,a):
#    print(f)
#    r= f+s
#    f=s
#    s=r

# ------------------------------------------------------------------------------
#Exercise 13

# n= 5
# f= 1
# for i in range(1,n+1):
#     if n >0:
#       f= f*i

# print(f)
# ----------------------------------------------------------------------------
#Exercise 14

# n= 76542
# b= 0
# while n>0:
#      a= n%10
#      b= (b*10)  + a
#      n= n//10
# print(b)
# -------------------------------------------------------------------------------
#Exercise 15

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in my_list[1::2]:
#     print(i,end=" ")
# --------------------------------------------------------------------------------
#Exercise 16

# a = 6
# for i in range(1,a+1):
#             print('current no is :',i, 'and the cube is', i**3)
# ----------------------------------------------------------------------------------
#Exercise 17

# n= 5
# a=2
# s= 0
# for i in range(1,n+1):
#      s= s+a
#      a= (a*10)+a
# print(s)
# ---------------------------------------------------------------------------------
#Exercise 18
# a=5
# for i in range(a):
#      for j in range(i):
#           print("*",end= ' ')
#      print()
# for i in range(5):
#      for j in range(a-i,0,-1):
#           print("*",end=" ")
#      print()
# --------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------
#                                Next chapter
# ---------------------------------------------------------------------------------


#Python Functions Exercise-

#Exercise 1

# def tary(name,age):
#      print(name,age)

# tary("dev",19)
#-----------------------------------------------------------------------------------
#Exercise 2

# def fun(*parameter):
#     for i in parameter:
#        print(i)
# fun(30,20,20)
# ----------------------------------------------------------------------------------
#Exercise 3

# def cal(a,b):
#      return a+b,a-b
# a,b=cal(40,10)
# print(a,b)
# ---------------------------------------------------------------------------------
#Exercise 4

# def se(name,salary=9000):
#      return (name,salary)
# a= se('dev',10000)
# b= se('dev2')
# print(a)
# ------------------------------------------------------------------------------
#Exercise 5

# def fun1(a,b):
#     def fun2(a,b):
#       return a+b
#     d= fun2(a,b)+5
#     print(d)
# fun1(1,2)
# ------------------------------------------------------------------------------
#Exercise 6

# def fun(n):
#      if n:
#           return n + fun(n-1)
#      else:
#           return 0
                 
# a= fun(10)
# print(a)
# -----------------------------------------------------------------------------
#Exercise 7

# def fun(name,age):
#      print(name,age)
# fun('dev',19)

# rec=fun
# rec("dev1",20)
# -----------------------------------------------------------------------------
#Exercise 8

# def fun(s,e):
#      l=[]
#      for i in range(4,30):
#           if (i%2)==0:
#                l.append(i)
#           else:
#                pass
#      return l
# a= fun(4,30)
# print(a)        
# ----------------------------------------------------------------------------
#Exercise 9

# x = [4, 6, 8, 24, 12, 2]
# print(max(x))
# -----------------------------------------------------------------------------



# ---------------------------------------------------------------------------
#                               Next Chapter
# ----------------------------------------------------------------------------

# Python String Exercise-

#Exercise 1

# s= 'james'
# a= s[0]
# b= s[int(len(s)/2)]
# c= s[-1]
# d= a+b+c
# print(d)
# -----------------------------------------------------------------------------
#Exercise 1

# s= "JhonDipPeta"

# m= int(len(s)/2)
# n= s[m+1]
# o= s[m-1]
# m= s[m]
# a= o+m+n
# print(a)
# -----------------------------------------------------------------------------
#Exercise 2
 
# s1 = "Ault"
# s2 = "Kelly"

# a= int(len(s1)/2)
# b= s1[:a]
# b= b+s2
# b= b+s1[a:]
# print(b)
# -----------------------------------------------------------------------------
#Exercise 3

# def fun(a,b):
#      q=a[0]
#      w= int(len(a)/2)
#      w1= a[w]
#      e= a[-1]

#      z=b[0]
#      x= int(len(b)/2)
#      x1= b[x]
#      c= b[-1]
     
#      total =  q+z+w1+x1+e+c
#      return(total)

# a=fun("America",'Japan')
# print(a)
# ---------------------------------------------------------------------------
#Exercise 4

# a=  'PyNaTive'
# l=[]
# u=[]

# for i in a :
#      if i.islower():
#        l.append(i)
#      else:
#           u.append(i)

# ss= ''.join(l+u)
# print(ss)
# ----------------------------------------------------------------------------
#Exercise 5

# s="P@#yn26at^&i5ve"
# char=0
# symbol=0
# digit=0
# for i in s:
#      if i.isalpha():
#           char += 1
#      elif i.isdigit():
#           digit +=1
#      else:
#           symbol +=1
# print('char',char)
# print('digit',digit)
# print('symbol',symbol)
# ----------------------------------------------------------------------------
#Exercise 6

# def fun(s1,s2):

#      start= s1[0]+s2[-1]
#      mid= s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
#      end= s1[-1]+s2[0]

#      total= start+mid+end
#      return(total)

# s1 = "Abc"
# s2 = "Xyz"
# print(fun(s1,s2))
# ----------------------------------------------------------------------------
#Exercise 7

# s1 = "Yn"
# s2 = "PYnative"
# Flag= True
# for i in s1:
#      if i in s2:
#          continue
#      else:
#           Flag= False
# print(Flag)
# ----------------------------------------------------------------------------
#Execise 8

# str1 = "Welcome to USA. usa awesome, isn't it?"
# temp= str1.lower()
# find="usa"
# count= temp.count(find)
# print(count)         
# ----------------------------------------------------------------------------
#Exercise 9

# str1 = "PYnative29@#8496" 
# digit= 0
# count=0
# for i in str1:
#      if i.isdigit():
#           digit += int(i)
#           count +=1
# avg= digit/count
# print('sum is :',digit,'and average is:',avg)
# ---------------------------------------------------------------------------
#Exercise 10

# str1 = "Apple"
# temp = dict()
# for i in str1:
#      count= str1.count(i)
#      temp[i]= count
# print(temp)
# ----------------------------------------------------------------------------
#Exercsie 11

# str1 = "PYnative"

# a= ''.join(reversed(str1))
# print(a)
# -----------------------------------------------------------------------------
#Exercise 12

# str1 = "Emma is a data scientist who knows Python. Emma works at google."

# print(str1.rfind("Emma")
# -----------------------------------------------------------------------------
#Exercise 13
# str1 = 'Emma-is-a-data-scientist'
# a= str1.split("-")
# for i in a:
#      print(i)
# ------------------------------------------------------------------------------
#Exercise 14

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# x= list(filter(None,str_list))
# print(x)
# ------------------------------------------------------------------------------
#Exercise 15

                                                                 #not done yet
#-------------------------------------------------------------------------------
#Exercise 16

# str1 = 'I am 25 years and 10 months old'
# digit = 0
# for i in str1:
#      if i.isdigit():
#           digit = int(digit*10)+ int(i)
# print(digit)
# ------------------------------------------------------------------------------
#Exercise 17

# str1 = "Emma25 is Data scientist50 and AI Expert"
# final=[]
# temp = str1.split()
# for i in temp:
#      if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
#           final.append(i)

# for i in final:
#      print(i)
# ------------------------------------------------------------------------------
#Exercise 18
# import string
# str1 = '/*Jon is @developer & musician!!'

# for i in string.punctuation:
#      str1= str1.replace(i,"#")
# print(str1)
# ------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
#                              Next Chapter
# ------------------------------------------------------------------------------- 
# Python List Exercise

#Exercise 1

# list1 = [100, 200, 300, 400, 500]

# list1.reverse()
# print(list1)
# -----------------------------------------------------------------------------
#Exercise 2

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# x= [i+j for i ,j in zip(list1,list2)]
# print(x)
# ------------------------------------------------------------------------------
#Exercise 3

# numbers = [1, 2, 3, 4, 5, 6, 7]

# x= [i**2 for i in numbers]
# print(x)
# ------------------------------------------------------------------------------
#Exercise 4

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# x=[]
# for i in list1:
#     for j in list2:
#         b= i+j
#         x.append(b)
# #x= [i+j for i in list1 for j in list2]  can do like this
# print(x)
# ------------------------------------------------------------------------------
#Exercise 5

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# x= zip(list1,list2[::-1])
# c= tuple(x)
# for i,j in c:
#    # for i,j in zip(list1,list2[::-1]): 
#   print(i,j)
# -------------------------------------------------------------------------------
#Exercise 6

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1= filter(None,list1)
# print(list(list1))
# ------------------------------------------------------------------------------
#Exercise 7

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
# ------------------------------------------------------------------------------
#Exercise 8

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)
# print(list1)
# -------------------------------------------------------------------------------
#Exercise 9

# list1 = [5, 10, 15, 20, 25, 50, 20]
# index= list1.index(20)
# list1[index]=200
# print(list1)
# -------------------------------------------------------------------------------
#Exercise 10

# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#      list1.remove(20)
# print(list1)
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
#                              Next Chapter
# ------------------------------------------------------------------------------- 
#Python Tuple Exercise

#Exercise 1

# tuple1 = (10, 20, 30, 40, 50)
# tuple1 = tuple1[::-1]
# print(tuple1)
# -------------------------------------------------
#Exercise 2

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])
# -------------------------------------------------
#Exercise 3

# t= (50,)
# print(t)
# print(type(t))
# -------------------------
#Exercsie 4

# tuple1 = (10, 20, 30, 40)
# for i in tuple1:
#     print(i)
# --------------------------------
#Exercise 5

# tuple1 = (11, 22)
# tuple2 = (99, 88)

# temp= tuple1
# tuple1=tuple2
# tuple2= temp
# #tuple1,tuple2 = tuple2, tuple1
# print(tuple1)
# print(tuple2)
# ---------------------------------
#Exercise 6

# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:5]
# print(tuple2)
# ---------------------------------
#Exercise 7

# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]= 222
# print(tuple1)
# -----------------------------------
#Exercise 8

# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
#                                                           not done yet
# ------------------------------------------------------------------------- 
#Exercise 9

# tuple1 = (50, 10, 60, 70, 50)
# print(tuple1.count(50))
# -----------------------------------
#Exercise 10

#                                                           not done yet
#------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                              Next Chapter
# -------------------------------------------------------------------------------

#Python Set Exercise

#Exercise 1

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# print(sample_set)
# --------------------------------------------
#Exercise 2

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)

# print(set1)
# ----------------------------------
#Exercise 3

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.union(set2))
# ---------------------------------
#Exercise 4

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set1.difference_update(set2)
# print(set1)
# --------------------------------
#Execsie 5

# set1 = {10, 20, 30, 40, 50}

# set1.difference_update({10,20,30})
# print(set1)
# -------------------------------------
#Execise 6

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.symmetric_difference(set2))
# ---------------------------------------
#Exercise 7

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# if set1.isdisjoint(set2):
#     print("two sets have no items in common")
# else:
#     print("two sets have items in common")

# print(set1.intersection(set2))
#----------------------------------------------------
#Exercise 8

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1.symmetric_difference_update(set2)
# print(set1)
#-------------------------------------------------
#Exercise 9

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1.intersection_update(set2)
# print(set1)                                            #learn methods of set
# -----------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                              Next Chapter
# -------------------------------------------------------------------------------

#Python dictonary exercise

#Exercise 1 

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# d= dict()

# for i in range(len(keys)):
#           d.update({keys[i]: values[i]})
# print(d)
# -----------------------------------------
#Exercise 2

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)
# -------------------------------------------------
#Exercise 3
# sampleDict={"class":{"student":{"name":"Mike","marks":{
# "physics":70,"history":80 }}}}

# print(sampleDict['class']['student']['marks']['history'])
# -----------------------------------------------------------
#Exercise 4

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# a= dict.fromkeys(employees,defaults)
# print(a)
# ----------------------------------------------------------
#Exercise 5

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# d= dict()

# for i in sample_dict:
#     if i in keys:
#         d.update(i)
# print(d)
                                                                    # not done yet
# ---------------------------------------------------------------------------------
#Exercise 6

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)
# ---------------------------
#Exercise 7

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("200 present in dict")
# ----------------------------------------------
#Execise 8

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location']= sample_dict.pop('city')
# print(sample_dict)
# ------------------------------------------------
#Exercsie 9

# sample_dict = {
#   'Physics': 82,
#   'Mathematics': 88,
#   'history': 75
# }

# print(min(sample_dict))
#                                                                not done yet
# ----------------------------------------------------------------------------
#Exercsie 10

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }

# sample_dict['emp3']['salary']= 8500
# print(sample_dict)
# ---------------------------------------------

# -------------------------------------------------------------------------------
#                              Next Chapter
# -------------------------------------------------------------------------------

#Python Pandas Exercise

#Data location-
# import pandas as pd
# a=pd.read_csv('C:\\Users\\kreez\\Downloads\\Automobile_data.csv')


#Exercise 1

# import pandas as pd

# a = pd.read_csv('C:\\Users\\kreez\\Downloads\\Automobile_data.csv')

# print(a.head(10))
# print(a.tail(10))
# ---------------------------------------------------------------
#Exercise 2

# import pandas as pd
# a = pd.read_csv('C:\\Users\\kreez\\Downloads\\Automobile_data.csv')
#                                                                 not done yet
#--------------------------------------------------------------------------
#Exercise 3

# import pandas as pd
# a = pd.read_csv('C:\\Users\\kreez\\Downloads\\Automobile_data.csv')

# a = a[['company','price']][a.price==a['price'].max()]
# print(a)
# ---------------------------------------------------------------------
#Exercise 4

# import pandas as pd
# a = pd.read_csv('C:\\Users\\kreez\\Downloads\\Automobile_data.csv')

# car = a.groupby('company')
# b = car.get_group('toyota')
# print(b)
# ----------------------------------------------------------------------
#Exercise 5
# import pandas as pd
# a = pd.read_csv('C:\\Users\\kreez\\Downloads\\Automobile_data.csv')

# print(a['company'].value_counts())
# ---------------------------------------------------------------------
#Exercise 6

# c=  a.groupby('company')
# d= c['company','price'].max()
# print(d)
# --------------------------------
#Exercise 7

# c= a.groupby('company')
# d= c['company','average-mileage'].mean()
# print(d)
# ------------------------------------------
#Exercise 8

# b= a.sort_values(by=['price'],ascending = False)
# print(b)
# ------------------------------------------------
#Exercise 9

# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

# b= pd.DataFrame.from_dict(GermanCars)
# c= pd.DataFrame.from_dict(japaneseCars)

# d= pd.concat([b,c],keys = ['German','Japan'])
# print(d)
# -----------------------------------------------------------------
#Exercise 10

# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

# b= pd.DataFrame.from_dict(Car_Price)
# c= pd.DataFrame.from_dict(car_Horsepower)

# d= pd.merge(b,c,on='Company')
# print(d)
# ------------------------------------------------

# -------------------------------------------------------------------------------
#                              Next Chapter
# -------------------------------------------------------------------------------

# Python OOPS Exercise

# Exercise 1

# class Vehicle():
#   def __init__(self,max_speed,mileage):
#     self.speed = max_speed
#     self.mileage = mileage
    
# a = Vehicle(140,40)

# print(a.speed,a.mileage)
# ------------------------------------------ 
# Exercise 2

# class Vehicle():
#   pass
# a = Vehicle()
# print(a)
# ------------------
# Exercise 3

# class Vehicle():
#   def __init__(self,name,speed,mileage):
#     self.name = name
#     self.speed =speed
#     self.mileage = mileage
#   def carname():
#     pass
# class Bus(Vehicle):
#   pass

# a= Vehicle("school_volvo",180,12)
# print("vehicle name:", a.name ,
#  "speed:", a.speed, "mileage:", a.mileage)
# --------------------------------------------
# Exercise 4

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)

# a = Bus("bus",80,30)
# print(a.seating_capacity())
# ------------------------------------------------------------------------
#Exercise 5

# class Vehicle:
#     colour = "white"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#      pass
# class Car(Vehicle):
#     pass

# a = Bus("volvo",180,12)
# b = Car("audi Q5",240,18)

# print(a.colour,a.name,a.max_speed,a.mileage)
# print(b.colour,b.name,b.max_speed,b.mileage)
# ---------------------------------------------------
#Exercise 6

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#      def fare(self):
#         amount = super().fare()
#         amount += amount*10/100
#         return amount

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())
# ------------------------------------------------------
#Exercise 7

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(type(School_bus))
# ----------------------------------------
#Exercise 8

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(isinstance(School_bus,Vehicle))
#--------------------------------------------------------
#--------------------------------------------------------
# Star pattern exercise 

#     my great learning
#Que 1
# a=5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")

#Que 2
# a=5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

#Que 3
# a = 5
# for i in range(a):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")

#Que 4
# a = 5
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         print(i,end=' ')
#     print("")
#     a = a-1

    #or 

# a = 5
# b = 0
# for i in range(a,0,-1):
#     b = b+1
#     for j in range(1,i+1):
#         print(b,end=" ")
#     print("")

#Que 5
# a = 5
# for i in range(a,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print("")

#Que 6
# a = 5
# for i in range(1,a+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("")

#Que 7
# a = 65
# for i in range(1,4):
#     for j in range(1,i+1):
#         alpha= chr(a)
#         print(alpha,end="")
#         a +=1
#     print(" ")

#Que 8
# a = 65
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(chr(a),end="")
#     a +=1
#     print(" ")

#Que 9
# for i in range(1,3+1):
#     a =65
#     for j in range(1,i+1):
#         print(chr(a),end=" ")
#         a+=1
#     print(" ")
    
#Que 10
# a= 5
# c=0
# for i in range(a,0,-1):
#     b= 65
#     for j in range(i,0,-1):
#         print(chr(b+c),end=" ")
#         b+=1
#     c+=1
#     print("")

#-------------------------------------------------

# Pynative
# pattern

#Que 1
# a= 5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("")

#que 2
# a= 5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

#que 3
# a= 5
# for i in range(1,a+1):
#     for j in range(a,0,-1):
#         print(i,end=" ")
#     print("")
#     a-=1

#que 4
# a= 5
# b=5
# for i in range(1,a+1):
#     for j in range(a,0,-1):
#         print(b,end=" ")
#     print("")
#     a-=1

#que 5
# a= 5
# for i in range(a):
#     for j in range(a+1):
#         print(j,end=" ")
#     print("")
#     a-=1

#Que 6
# a= 5
# b=1
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(b,end=" ")
#     print("")
#     b+=2


#Que 7
# a= 5
# b=a
# for i in range(a,0,-1):
#     for j in range(i):
#         print(b,end=" ")
#     print("")
#     b-=1

#Que 8
# a= 5
# for i in range(1,a+1):
#     b=i
#     for j in range(1,i+1):
#         print(b,end=" ")
#         b-=1
#     print("")
    

#Que 9
# a= 5
# for i in range(a,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")        
#     print("")

#Que 10




#Que 11
# a = 5
# for i in range(1,a+1):
#     num=1
#     for j in range(a,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num+=1
#     print("")

# Que 12


#star pattern 
#Que 1

# a= 5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
    
#Que 2

# a= 5
# k = 2*a -2
# for i in range(1,a+1):
#     for j in range(1,k+1):
#         print("",end=" ")
#     k= k-2
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
#result    
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

#Que 3


# a= 5
# k = 0
# for i in range(a,0,-1):
#     # for j in range(k):
#     #     print(" ")
#     # k+=1

#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print("")
# #result    

#que 4

# size = 8
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     # decrementing m after each loop
#     m = m - 1
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")


#que 5















































































