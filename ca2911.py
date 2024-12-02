print("amita",end=' ')
print("patil")
n=int(input("enter any number"))
for i in range(n):
    for j in range(n):
        print("0",end=' ')
    print("\n")
bag=''
bag+='0'
bag+='0'
bag+='0'
print(bag)
# i=0
# while i < 3:
#   print(bag)
i=1
for i in range(n+1):
    j=1
    for j in range(i):
        print(j,end=' ')
    print("\n")

               