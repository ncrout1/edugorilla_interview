l="9bccdd27cdf841918a12c753fe"
list_data=list(l)
count_freq={}
a=set(list_data)
for i in a:
    
    count_freq[i]=list_data.count(i)
for char in count_freq:
    print("Character "+str(char)+" has occured "+str(count_freq[char])+" times ")
    print(char)
print(count_freq)
