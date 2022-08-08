
print()
print()
# KBC game
print("Hello")
# take input from user for users name
player = input('enter your name :-')
print('Welcome to the KBC game', player)
print()
#  print the Rules for user in for loop
print("Here are the Rules of the Game")
print()
print("This is amount which you win if you give right answers")
que_amount=["Questions      Amount",
            "1:Que:        5,000",
            "2:Que:        10,000 milestone questions",
            "3:Que:        20,000",
            "4:Que:        40,000",
            "5:Que:        80,000",
            "6:Que:        1,60,000",
            "7:Que:        3,20,000 milestone questions",
            "8:Que:        6,40,000",
            "9:Que:        12,50,000",
            "10:Que:       25,00,000",
            "11:Que:       50,00,000",
            "12:Que:       1 Corores",
            "13:Que:       5 Corores",]
for list in que_amount:
    print(list) 
print()
rules = ["1:- You have total 13 Question in this Game.", "2:- Each Question has 4 options and only one of them is Correct.",
         "3:- In this game you win total cash prize is Rs 5 Crores", "4:- You have 2 Milestone questions in this game.", "5:- If you have crossed the milestone question, you are guaranteed to win that amount.",
         "6:- For Example: If you have answered the 2nd question correctly, and you got the 5th question wrong., you will win Rs 10,000.similarly, if you crossed the 7th question, then you are guaranteed to win Rs 3,20,000.",
         "7:- If you want quit this Game then press 0.",
         "8:- If you want lifeline then press L.",
         "9:- You have 2 lifeline in this game and you can't use 1 lifeline 2 time Ex:-if you have used 50-50 lifeline then next time you can't used this again"]
for r in rules:
    print(r)
print()
print("GAME START")
print("This is your first question ")
print()
# using list and in list we stored multiply Dictionarys in the dictionarys stored different keys and value.
kbc = [
    {

        "question": "Q.1:- Which state produces maximum soyabean?",
        "options": ["A:-Madhya pradesh", "B:-Uttar pradesh", "C:-Bihar", "D:-Rajasthan"],
        "answer":"A",
        "quit":"",
        "50_50":["A:-Madhya pradesh", "D:-Rajasthan"],
        "hint":"( largest city by areawise )",
        "amount":"you win Rs 5,000",
        "Milestone":""
    },
    {
        "question": "Q.2:- Which of the following is the capital of Arunachal Pradesh?",
        "options": ["A:-Itanagar", "B:-Dispur", "C:-Imphal", "D:-Panaji"],
        "answer":"A",
        "quit":"5,000",
        "50_50":["A:-Itanagar", "C:-Imphal"],
        "hint":"(its fine Tibetan architecture and varied tribal culture)",
        "amount":"You have crossed milestone Question and you win Rs 10,000",
        "Milestone":"5,000"
    },
    {
        "question": "Q.3:- Who wrote Vande Mataram?",
        "options": ["A. Rabindranath Tagore", "B. Bankimchandra Chatterjee", "C. Sharat chandra chattopadhyay", "D. None of the above"],
        "answer":"B",
        "quit":"10,000",
        "50_50":["B. Bankimchandra Chatterjee", " None of the above"],
        "hint":"(he was the author of the 1882 Bengali language novel Anandamath, which is one of the landmark of modern  Bengali and Indian literaure) ",
        "amount":"you win Rs 20,000",
        "Milestone":"10,000"
    },
    {
        "question": "Q.4:-Which of the following states is not located in the North?",
        "options": ["A.Jharkhand", "B. Jammu and Kashmir", "C. Himachal Pradesh", "D. Haryana"],
        "answer":"A",
        "quit":"20,000",
        "50_50":["A.Jharkhand", "B.Jammu and Kashmir"],
        "hint":"This is famous for its rich mineral resources like Uranium, ,Mica, Bauxite etc.",
        "amount":"you win Rs 40,000",
        "Milestone":"10,000"
    },
    {
        "question": "Q.5:-In which state is the main language Khasi?",
        "options": ["A. Mizoram", "B. Nagaland", "C. Meghalaya", "D. Tripura"],
        "answer":"C",
        "quit":"40,000",
        "50_50":["B. Nagaland", "C.Meghalaya"],
        "hint":"this state also known as the about of clouds, falls in one of the richest biodiversity areas in the world.",
        "amount":"you win Rs 80,000",
        "Milestone":"10,000"
    },
    {   "question": " Q.6:- Which is the largest coffee producing state of India?",
        "options": ["A. Kerala", "B. Tamil Nadu", "C. Karnataka", "D. Arunachal Pradesh"],
        "answer":"C",
        "quit":"80,000",
        "50_50":["A.Kerala", "C.Karnataka"],
        "hint":"It is primarily known for its Heritage destinations and its Wildlife National Parks",
        "amount":"you win Rs 1,60,000",
        "Milestone":"10,000"
    },
    {   "question": "Q.7:- The 2014 football world cup is scheduled to be held in? ",
        "options": ["A. China", "B. Australia", "C. Japan", "D. Brazil"],
        "answer":"D",
        "quit":"1,60,000",
        "50_50":["A.China", "D.Brazil"],
        "hint":"It is famous for its iconic carnival festival and its talented soccer players like Pelé and Neymar.",
        "amount":"You have crossed milestone Question and you win Rs 3,20,000",
        "Milestone":"10,000"
    },
    {   "question": "Q.8:-Guru Gopi Krishna is popular for which form of Indian dance?",
        "options": ["A. Bharatanatyam", "B. Kuchipudi", "C. Kathak", "D. Manipuri"],
        "answer":"A",
        "quit":"3,20,000",
        "50_50":["A.Bharatanatyam", "C.Kathak"],
        "hint":" This dance form is performed by both men and women.",
        "amount":"you win Rs 6,40,000",
        "Milestone":"10,000"
    },
    {   "question": " Q.9:- Which state has the largest population?",
        "options": ["A. Uttar Pradesh", "B. Maharastra", "C. Bihar", "D. Andra Pradesh"],
        "answer":"A",
        "quit":" 6,40,000",
        "50_50":["A.Uttar Pradesh", "D.Andra Pradesh"],
        "hint":"The state is famous for its top tourist attractions such as Taj Mahal (One of the seven wonders of the world)",
        "amount":"you win Rs 12,50,000",
        "Milestone":"3,20,000"
    },
    {   "question": "Q.10:-The language spoken by the people by Pakistan is ?",
        "options": ["A. Hindi", "B. Palauan", "C. Sindhi", "D. Nauruan"],
        "answer":"C",
        "quit":"12,50,000",
        "50_50":["A. Hindi", "C. Sindhi"],
        "hint":"It has a total of 52 letters.",
        "amount":"you win Rs 25,00,000",
        "Milestone":"3,20,000"
    },
    {   "question": "Q.11:-Who is popularly called as the Iron Man of India?",
        "options": ["A. Subhash Chandra Bose", "B. Sardar Vallabhbhai Patel", "C. Jawaharlal Nehru", "D. Govind Ballabh Pant"],
        "answer":"B",
        "quit":"25,00,000",
        "50_50":["B.Sardar Vallabhbhai Patel", "C.Jawaharlal Nehru"],
        "hint":"He played a leading role in the Indian freedom struggle and became the first Deputy Prime Minister and Home Minister of India. He is credited with achieving political integration of India. ",
        "amount":"you win Rs 50,00,000",
        "Milestone":"3,20,000"
    },
    {   "question": "Q.12:-Film and TV institute of India is located at?",
        "options": ["A. Pune(Maharashtra)", "B. Rajkot(Gujarat)", "C. Pimpri(Maharashtra)", "D. Perambur(Tamilnadu)"],
        "answer":"A",
        "quit":"50,00,000",
        "50_50":["A.Pune(Maharashtra)", "C. Pimpri(Maharashtra)"],
        "hint":"Shaniwar Wada Palace. A prominent historical landmark in there is Shaniwarwada which is considered as one of the best tourist places. ",
        "amount": "you win Rs 1 Crore",
        "Milestone":"3,20,000"
    },
    {   "question": "Q.13:-Name the national river of India",
        "options": ["A.Gangotri", "B. Narmada", "C. Ganga", "D. Godavari"],
        "answer":"c",
        "quit":"1 Crore",
        "50_50":["A.Gangotri", "C.Ganga"],
        "hint":"This is the longest river in India, ",
        "amount":"you win Rs 5 Crore ",
        "Milestone":"3,20,000"
     }
]
# Difine list
b = []
# difine list for Lifeline
life = ["1:-50_50", "2:-Expert hint"]

# using for loop for display the questions and Answer
for x in kbc:
    print(x["question"])
    for y in (x["options"]):
        print(y)
    print(" ")
    # user input from the user for answer, quit and for lifeline.
    lifeline = "press L for lifeline"
    if life == b:
        lifeline = ""
    ans = input('enter your answer /' + lifeline + '/press 0 for quit:-')
    # Stop Condition for lifeline
    if life == b:
        if ans == "L":
            print("Opps sorry you have all ready used lifeline")
            ans = input('enter your answer /press 0 for quit:-')
     # Condition for the lifeline
    elif ans == "L":
        for l in life:
            print(l)
        ans1 = input("enter please:-")
        print(" ")
        if ans1 == "1":
            for f in (x["50_50"]):
                print(f)
        # use remove function for  remove elements from the list
            life.remove("1:-50_50")
            ans = input("Enter your answer :-")
        elif ans1 == "2":
            print(x["hint"])

            life.remove("2:-Expert hint")
            ans = input("Enter your answer :-")
    print("  ")
    #  input for lock the question
    sure = input("Are you sure then enter YES OR NO:- ")
    if sure == "YES" and ans == (x["answer"]):
        print("Congraculation", x["amount"])
        print("  ")
    elif sure == "NO":
        ans = input("Enter your answer:-")
        if ans == (x["answer"]):
            print("Congraculation", x["amount"])
            print(" ")
        elif ans != (x["answer"]):

            print("Sorry Wrong Answer...Better luck next time... ")
            break
    # condition  for quit
    elif ans == "0":

        print("Okay Bye Better luck next time...")
        print(x["quit"])
        break
    elif ans!=(x["answer"]):
         print("Sorry Wrong Answer...Better luck next time... ")
         print("You win total amount",x["Milestone"])
         break
    elif ans==(x["answer"]):
        print("Congraculation",x["amount"])
        print(" ")







          




