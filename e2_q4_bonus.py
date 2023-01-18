import requests   
import random
s=["Abuse","Adult","Agent","Anger","Apple","Award","Basis","Beach","Birth","Block","Blood","Board","Brain","Bread","Break","Brown","Buyer","Cause","Chain","Chair"]
rnd_word=random.choice(s)
rnd_list=list(rnd_word)
print(rnd_list)
l1=["-","-","-","-","-"]
j=5
while j>0:
    k=input("Enter 5 letter word:")
    url=requests.get(f'''https://api.dictionaryapi.dev/api/v2/entries/en/{k}''')
    op=url.json()
    s=list(k)
    if s==rnd_list:
        print("You Won")
        break
    else:
        for i in range(5):
            if type(op) is list:
                if s[i]==rnd_list[i]:
                    k=s.index(s[i])
                    l1[k]=s[i]                
        if type(op) is dict:
            print("Enter a valid word")
            j+=1
    j=j-1
    print(j)
    for i in l1:
        print(i,end="")
    print()         
