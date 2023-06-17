import random
import requests

base="https://od-api.oxforddictionaries.com/api/v2/entries/en-us/"
api_key="b39c34d7bd54d165f06de4b0ee8a51fa"

l=['abuse', 'adult', 'agent', 'beach', 'birth', 'block', 'chair', 'chest', 'chief', 'cover', 'cream', 'crime', 'dance', 'death', 'depth', 'drink', 'drive', 'earth', 'error', 'event', 'faith', 'fault', 'grant', 'grass', 'green', 'group', 'hotel', 'house', 'image', 'index', 'funny', 'judge', 'knife', 'lower', 'layer', 'level', 'mouth', 'music', 'night', 'noise', 'spine', 'owner', 'panel', 'queen', 'radio', 'truth', 'unity', 'value', 'world', 'youth']
i=random.randint(0,49)
word=l[i]
word_l=list(word)
guess=["-"]*5
chance=6
print()
other=[]
f=False
print("Chances left:",chance)
while chance>0:
    user=list(input("Guess the 5 letter word: ").lower())
    if len(user)!=5:
        print("Enter 5 letter word")
        print()
        continue
    endpoint=base+"".join(user)
    headers1={"app_id": "971a57f7", "app_key": api_key}
    res=requests.get(endpoint,headers=headers1)
    if res.status_code==404:
        print("Invalid Word. Try again")
        print()
        continue
    print()
    for i in range(5):
        if user[i]==word_l[i]:
            guess[i]=word_l[i]
            if user[i] in other:
                other.remove(user[i])
        elif user[i] in word_l:
            if user[i] not in other:
                other.append(user[i])
    chance-=1
    ans="".join(guess)
    print("Answer:",ans)
    print()
    if ans==word:
        f=True
        print("Congratulations. You win")
        break
    if other!=[]:
        print("Other characters present: ",end=" ")
        for k in other:
            print(k,end=" ")
        print()
        print()
    print("Chances left:",chance)
if f==False:
    print("Bad luck :(")
    print("Correct answer:",word)