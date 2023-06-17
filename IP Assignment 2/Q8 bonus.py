#A trivia game which asks 5 random questions and gives a score out of 5 and gives a gif according to whether user's response is correct or wrong

import requests
import random

url="https://the-trivia-api.com/api/questions?limit=5" #trivia
api_key="NLHU9ZUi2miBmuxGblqdMxsu7b8OfZst" #giphy
base="https://api.giphy.com/v1/gifs/search" #giphy
correct="well+done"
incorrect="better+luck+next+time"
endpoint1=base+"?api_key="+api_key+"&q="+correct+"&limit=5"
endpoint2=base+"?api_key="+api_key+"&q="+incorrect+"&limit=5"
res1=requests.get(endpoint1)
res2=requests.get(endpoint2)
gif_correct=res1.json()["data"]
gif_incorrect=res2.json()["data"]
l_corr=[]
l_incorr=[]
for i in gif_correct:
    l_corr.append(i["url"])
for i in gif_incorrect:
    l_incorr.append(i["url"])
res=requests.get(url)
data=res.json()
score=0
q=1
for i in data:
    print("Question",str(q)+":",end=" ")
    print(i["question"])
    print("Category:",i["category"])
    if "difficulty" in i:
        print("Difficulty:",i["difficulty"])
    print()
    incorrect1,incorrect2,incorrect3=i["incorrectAnswers"]
    options=list(set([i["correctAnswer"],incorrect1,incorrect2,incorrect3]))
    opt=65
    d_ans={}
    for j in options:
        print(chr(opt)+"-",j)
        d_ans[chr(opt)]=j
        opt+=1
    print()
    ans=input("Select an option: ")
    if d_ans[ans]==i["correctAnswer"]:
        score+=1
        print("Correct answer")
        i=random.randint(0,4)
        print("Click to view gif-->",l_corr[i])
    else:
        print("Wrong Answer")
        print("Correct Answer:",i["correctAnswer"])
        i=random.randint(0,4)
        print("Click to view gif-->",l_incorr[i])
    print()
    q+=1
print("Your score:",str(score)+"/5")
if score<=2:
    print("Better luck next time :(")
    endpoint=base+"?api_key="+api_key+"&q=bad+luck&limit=1"
    res=requests.get(endpoint)
    data=res.json()["data"]
    for i in data:
        print("Click to view gif-->",i["url"])
elif score==3:
    print("You were almost there")
    endpoint=base+"?api_key="+api_key+"&q=almost+there&limit=1"
    res=requests.get(endpoint)
    data=res.json()["data"]
    for i in data:
        print("Click to view gif-->",i["url"])
elif score==4:
    print("Well done! That was so close")
    endpoint=base+"?api_key="+api_key+"&q=well+done&limit=1"
    res=requests.get(endpoint)
    data=res.json()["data"]
    for i in data:
        print("Click to view gif-->",i["url"])
elif score==5:
    print("AMAZING!! Great job")
    endpoint=base+"?api_key="+api_key+"&q=brilliant+amazing&limit=1"
    res=requests.get(endpoint)
    data=res.json()["data"]
    for i in data:
        print("Click to view gif-->",i["url"])
print()
print("Thank you for playing")