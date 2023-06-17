import random

l=['abuse', 'adult', 'agent', 'beach', 'birth', 'block', 'chair', 'chest', 'chief', 'cover', 'cream', 'crime', 'dance', 'death', 'depth', 'drink', 'drive', 'earth', 'error', 'event', 'faith', 'fault', 'grant', 'grass', 'green', 'group', 'hotel', 'house', 'image', 'index', 'ones', 'judge', 'knife', 'laura', 'layer', 'level', 'mouth', 'music', 'night', 'noise', 'spite', 'owner', 'panel', 'queen', 'radio', 'truth', 'unity', 'value', 'world', 'youth']
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