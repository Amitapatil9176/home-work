# class A():
#     def show(self):
#         print("i am from class A")
# class B():
#     def show(self):
#         print("i am from class B")
# class child(A,B):
#     def show(self):
#         A.show(self)
#         B.show(self)
#         print("I am from class child")
# ch=child()
# ch.show()
# class A():
#     def show(self):
#         print("i am from class A")
# class B(A):
#     def show(self):
#         # A.show(self)
#         super().show()
#         print("i am from class B")
# class child(B):
#     def show(self):
#         super().show()
#         print("I am from class child")
# ch=child()
# ch.show()

# n=int(input("enter any number"))
# s=0
# for i in range(2,n):
#     if(n%i==0):
#         s+=1
# if(s>0):
#     print("number is not prime")
# else:
#     print("number is prime")
# n=int(input("enter any number"))
# s=0
# print("prime numbers =",end=" ")
# for i in range(1,n+1):
#     for j in range(2,i):
#       if(i%j==0):
#         s+=1
#     if(s==0):
#        print(i,end=" ")
     
#     else:
#        s=0
# print("prime numbers=", end=" ")
# for i in range(2, 20):
#     # check for prime
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")

# def add(a,b):
#   sum=0
#   sum=a+b
#   print("addition=",sum)
# add(5,6)
# def even():
#   list1=[1,2,3,4,5,6]
#   list2=[]
#   for i in list1:
#      if i %2==0:
#         list2.append(i)
#   return list2
# print(even())
# def even():
#   list1=[1,2,3,4,5,6]
#   list2=[]
#   for i in range(len(list1)):
#      if list1[i] %2==0:
#         list2.append(list1[i])
#   return list2
# print(even())  
nu=int(input("enter any number"))
