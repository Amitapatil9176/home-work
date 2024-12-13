list=[1,2,3,4,5,6,7,8,9,55]
t=int(input("enter any number"))
i=1
l=len(list)
while i<=l:
    if(list[i]==t):
        print(list[i])
        print("index=",i)
        break
    i+=1
print("******************")
listo=[45,25,5.5,8,90.5,32,80.5,4.5]
min=listo[0]
max=listo[0]
le=len(listo)
i=1
j=1
while i<le:
    if(min>listo[i]):
        min=listo[i]
    i+=1
while j<le:
    if(max<listo[j]):
        max=listo[j]
    j+=1 
print("Minimum number of list is",min)
print("Maximum number of list is",max)

