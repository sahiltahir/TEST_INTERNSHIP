string="geeks for geeks"

lst=[]

for i in string.split(" "):
    lst.append(i)
print(lst)
min_len=[]
for i in lst:
    min_len.append(len(i))
min_length=min(min_len)
print(min_length)

min_word = [word for word in lst if len(word) == min_length]
print(min_word)  
print("Minimum length word(s):", min_word)