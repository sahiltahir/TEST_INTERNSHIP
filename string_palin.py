s=input("Enter a string:")

rev_obj=reversed(s)
print(rev_obj)
rev=list((rev_obj))
print(rev)


for i in rev:
   x="".join(rev) 
print(x)

if s==x:
   print("its a palindrome")
else:
   print("not a palindrome")