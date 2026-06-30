import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
name=input("enter your name :")

if(hour>=0 and hour<12):
    print("Good Morning",name)
elif(hour>=12 and hour<17):
    print("Good Afternoon",name)
else:
    print("Good Night",name)

'''a = int(input("enter a no. : "))
match a:
    case _ if(a<0):
        print("Negative")
    case _ if(a>0):
        print("Positive")
    case _:
        print("zero")
i=0
while(i<=5):
    print(i)
    i=i+1;'''
        



