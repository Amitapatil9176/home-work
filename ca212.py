#1. Datatypes in python
#integer
num_int=42
print(num_int)
print(type(num_int))
#string
str='amita'
print(str)
print(type(str))
#float
num_float=3.14
print(num_float)
print(type(num_float))
#complex
num_comp=2+2j
print(num_comp)
print(type(num_comp))
#boolian
num_var=True
print(num_var)
print(type(num_var))
#set
my_set={1,2,3,1,4,5,6}
print(my_set)
print(type(my_set))
#information set
my_dict={'name':'John','Age':33,'City':'New York'}
print(my_dict)
print(type(my_dict))
#list
numset= [1,2,3,'amita',[1,2,3],{'a',12}]
print(numset)
print(type(numset))
#Tuple
my_tuple=(1,3.0)
print(my_tuple)
print(type(my_tuple))
#sets
diss={'a':1,'b':2,'c':3 ,'d':4}
print(diss)
print(type(diss))
name='amita '
print(type(name))
#2. what is difference between list and tuple
listo=[1,2,99,77,88]
print(listo)
tupleo=(3,4,2,1,2.5)
print(tupleo)
listo[2]=110
print(listo)
#4.#deep copy and shallow copy
import copy
original=[[1,2],[3,4]]
shalow= copy.copy(original)
dep= copy.deepcopy(original)
print(original)
print("**********")
shalow[1][1]=50
print(original)
print(shalow)
original[0][1]=100
print(shalow)
print(dep)
#5 what is decorator in python
def deco_fun(original_fun):
    def wrapp_fun():
        print("wrapper executed before riginal function.")
        return original_fun()
    return wrapp_fun()
@deco_fun
def display():
    print("Original function executed")
# 7what are pythons '*args' and'**kwargs 
def exmp_fun(*args,**kwargs):
    print("positional arguments:",args)
    print("keyward arguments:",kwargs)
exmp_fun(1,2,3,name="amita",age=33)
# 9what is difference between / and // 
a=12/5
b=12//5
print("div" ,a)
print("divi=",b)
