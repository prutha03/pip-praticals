# a. Write a Python script to check whether a given key already exists in a dictionary.


# dic={"name":"hello",2:"to",3:"python world",4:123}
# input_key=(input("enter the key to check = "))
# if input_key in dic:  #ifin is used to check the key exist or not
#     print("key exist")
# else:
#     print("enter the valid key")


# b. Write a Python script to merge two Python dictionaries.


# dic1={1:"dog",2:"are",3:"clever"}
# dic2={4:"they",5:"are also",6:"cute"}
# dic1.update(dic2)
# print(dic1)


# c. Write a Python program to sum all the items in a dictionary.

dic1 = {"a":1,"b":2,"c":43}
# values=dic1.values() #that return value of dictonary
# total = sum(values)#using sum function
# print(total)

# sum=0
# i=0
# for i in dic1.values(): #using for loop
#     sum=sum+i
#     i+=1
# print(sum)
# d. Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# dic1={1:10,1:20,2:30}
# dic1[3]=20
# dic1[4]=40
# print(dic1)
# e. Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :

# dic1={1:10, 2:20}

# dic2={3:30, 4:40}

# dic3={5:50,6:60}

# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)
# Tuple

# a. Write a Python program to create a tuple with different data types.

# Mytuple=(1,"hello,",3.44)
# print(Mytuple)

# b. Write a Python program to create a tuple with numbers and print one item.

# Mytuple=(1,2,3)
# print(Mytuple[1])

# c. Write a Python program to add an item in a tuple.

# Mytuple1=(10,20,30)
# Mytuple2=(50,60)
# Mytuple3=Mytuple1+Mytuple2
# print(Mytuple3)

# d. Write a Python program to convert a tuple to a string.

# Mytuple1=(1,2)
# Mytuple=type(str(Mytuple1))
# print(Mytuple)

# e. Write a Python program to find the length of a tuple.
# Mytuple1=(1,2,3,4)
# Mytuple=len(Mytuple1)
# print(Mytuple)


# Set

# a. Write a Python program to add member(s) in a set and clear a set

# Myset={1,2,3}
# Myset.add(4)
# print(Myset)
# Myset.clear()
# print(Myset)

# b. Write a Python program to remove an item from a set if it is present in the set.

# Myset={1,2,3,4}
# Myset.remove(2)
# print(Myset)

# c. Write a Python program to create an intersection, Union, difference of sets.

# Myset1={1,2,3,4}
# Myset2={1,2}
# Myset3=Myset1.intersection(Myset2)
# Myset4=Myset1.union(Myset2)
# Myset5=Myset1.difference(Myset2)
# print(Myset3)
# print(Myset4)
# print(Myset5)

# d. Write a Python program to find maximum and the minimum value in a set.

# Myset1={1,2,3}
# print(max(Myset1))
# print(min(Myset1))

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# 1st for list
# Mylist=[1,2,3,4,5,3,2]                                           
# Mylist2 = list(set(Mylist))

# MaxNo = 0
# Maxvalue = list([])

# i = 0
# while i < len(Mylist2) :
#     if Mylist.count(Mylist2[i]) > MaxNo :
#         MaxNo = Mylist.count(Mylist2[i])
#     i += 1

# i = 0
# while i < len(Mylist2) :
#     if Mylist.count(Mylist2[i]) == MaxNo :
#         Maxvalue.append(Mylist2[i])
#     i += 1

# print("\n")
# i = 0
# while i < len(Maxvalue) :
#     print(f"{Maxvalue[i]} is repeated {MaxNo} times in List\n")
#     i += 1



# 2nd. Most common elements from tuple

# MyTuple = (1,2,3,3,4,2,1)

# Mylist = list(MyTuple)
# Mylist2 = list(set(Mylist))

# MaxNo = 0
# Maxvalue = list([])

# i = 0
# while i < len(Mylist2) :
#     if Mylist.count(Mylist2[i]) > MaxNo :
#         MaxNo = Mylist.count(Mylist2[i])
#     i += 1

# i = 0
# while i < len(Mylist2) :
#     if Mylist.count(Mylist2[i]) == MaxNo :
#         Maxvalue.append(Mylist2[i])
#     i += 1


# print("\n")
# i = 0
# while i < len(Maxvalue) :
#     print(f"{Maxvalue[i]} is repeated {MaxNo} times in Tuple\n")
#     i += 1


# 3rd. Most common elements from Dictionary

# Dic = {1:"Dhruv" , 2:"Prutha" , 3:"Jiya" , 4:"Samarth" , 5:"Dhruv" , 6 : "Samarth"}

# Mylist = list(Dic.values())
# Mylist2 = list(set(Mylist)) 

# MaxNo = 0
# Maxvalue = list([])

# i = 0
# while i < len(Mylist2) :
#     if Mylist.count(Mylist2[i]) > MaxNo :
#         MaxNo = Mylist.count(Mylist2[i])
#     i += 1

# i = 0
# while i < len(Mylist2) :
#     if Mylist.count(Mylist2[i]) == MaxNo :
#         Maxvalue.append(Mylist2[i])
#     i += 1

# print("\n")
# i = 0
# while i < len(Maxvalue) :
#     print(f"{Maxvalue[i]} is repeated {MaxNo} times in Dictionary\n")
#     i += 1