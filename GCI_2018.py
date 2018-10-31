for i in range(10):
    print('GCI is great')
    
name=input('Hi! What is your name?')

rev_name='' #empty string to store characters in reverse order

for j in range (-1,-len(name)-1,-1):#reverse indexing
    rev_name+=name[j]

print('Hello',name,', pleased to meet you! Did you know that your name backwards is',rev_name,'?')
    


