pm=int(input("enter value of n"))
i=2
sum=0
while i<pm:
   if(pm%i==0):
      sum+=1
   else:
      break
   i=i+1   
if(sum>0):
   print("not prime")
else:
   print("prime")