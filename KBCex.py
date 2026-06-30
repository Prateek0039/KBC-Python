import random
import time

''''Question = [

    ["Which data structure works on LIFO principle?", 
     "A. Queue", "B. Stack", "C. Array", "D. Linked List", 
     "B", 1000],

    ["Which data structure works on FIFO principle?", 
     "A. Stack", "B. Tree", "C. Queue", "D. Graph", 
     "C", 2000],

    ["Time complexity of binary search?", 
     "A. O(n)", "B. O(log n)", "C. O(n^2)", "D. O(1)", 
     "B", 3000],

    ["Which is linear data structure?", 
     "A. Tree", "B. Graph", "C. Array", "D. Heap", 
     "C", 5000],

    ["Which data structure uses pointers?", 
     "A. Array", "B. Linked List", "C. Stack", "D. Queue", 
     "B", 8000],

    ["Which traversal is used in DFS?", 
     "A. Level Order", "B. Breadth First", "C. Depth First", "D. Sorting", 
     "C", 10000],

    ["Which data structure is used for recursion?", 
     "A. Queue", "B. Stack", "C. Graph", "D. Array", 
     "B", 15000]
]'''


Question = [

    ["Which team is known as 'Yellow Army' in IPL?",
     "A. Mumbai Indians", "B. Chennai Super Kings", "C. Kolkata Knight Riders", "D. Rajasthan Royals",
     "B", 1000],

    ["Who is called 'King Kohli' in cricket?",
     "A. Rohit Sharma", "B. MS Dhoni", "C. Virat Kohli", "D. KL Rahul",
     "C", 2000],

    ["Which IPL team is associated with Mumbai?",
     "A. CSK", "B. MI", "C. RCB", "D. KKR",
     "B", 3000],

    ["Who is famous as 'Captain Cool'?",
     "A. Virat Kohli", "B. MS Dhoni", "C. Hardik Pandya", "D. Rohit Sharma",
     "B", 5000],

    ["Which team wears red and is called RCB?",
     "A. Royal Challengers Bangalore", "B. Rajasthan Royals", "C. Delhi Capitals", "D. Punjab Kings",
     "A", 8000],

    ["Who is known for hitting maximum sixes in IPL history (popularly)?",
     "A. Chris Gayle", "B. Sachin Tendulkar", "C. Rahul Dravid", "D. Bhuvneshwar Kumar",
     "A", 10000],

    ["Which team is called 'Men in Purple'?",
     "A. CSK", "B. KKR", "C. MI", "D. SRH",
     "B", 15000],

    ["Who is known as 'Hitman' in cricket?",
     "A. Rohit Sharma", "B. Virat Kohli", "C. MS Dhoni", "D. Rishabh Pant",
     "A", 20000],

    ["Which team represents Chennai in IPL?",
     "A. Chennai Super Kings", "B. Gujarat Titans", "C. Lucknow Super Giants", "D. Delhi Capitals",
     "A", 25000],

    ["Who is famous wicketkeeper-batsman from India?",
     "A. Rishabh Pant", "B. Jasprit Bumrah", "C. Ravindra Jadeja", "D. Shubman Gill",
     "A", 30000],

    ["Which IPL team is based in Kolkata?",
     "A. KKR", "B. CSK", "C. MI", "D. DC",
     "A", 40000],

    ["Who is known for fast bowling yorkers (MI bowler)?",
     "A. Jasprit Bumrah", "B. Virat Kohli", "C. MS Dhoni", "D. KL Rahul",
     "A", 50000],

    ["Which team is called 'Orange Army'?",
     "A. SRH", "B. CSK", "C. RCB", "D. MI",
     "A", 80000],

    ["Who is known as 'Universe Boss'?",
     "A. AB de Villiers", "B. Chris Gayle", "C. David Warner", "D. Steve Smith",
     "B", 100000],

    ["Which IPL format is most popular for entertainment?",
     "A. Test", "B. ODI", "C. T20", "D. First Class",
     "C", 500000]
]

random.shuffle(Question)   #used to give random questions everytime

final_prize=0
correct=0
for i in Question:
    print("\n",i[0])
    j=1
    while j<5:
        print(i[j])
        j=j+1
    #answer=input("enter your choice (A,B,C,D) :")
    answer = input("enter your choice (A,B,C,D) :").strip().upper()

    while answer != "A" and answer != "B" and answer != "C" and answer != "D":
        print("❌ Invalid option! Please enter only A, B, C or D.")
        answer = input("enter your choice (A,B,C,D) :").strip().upper()
    if(answer=="A" or answer=="B" or answer=="C" or answer=="D"):
        if(answer==i[5]):
            final_prize+=i[6]
            correct+=1
            print("checking answer...")
            time.sleep(2)
            print("Nice!,Sahi jawab 👍")
            print(correct)
            print("🤑 Updated price :",final_prize)
        else:
            print("checking answer...")
            time.sleep(2)
            print("Oops!Galat ho gaya 😑")
            print("Game over.")
            print("💰 Final prize:",final_prize)
            break
    else:
        print("Please enter valid option")

print("\nGame Finished !!!")
print("💰 your total winning amount is:",final_prize)