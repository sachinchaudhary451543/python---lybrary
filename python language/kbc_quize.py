questions = [
    ["which language is used to make facebook:","python","JAVA","C++","None", 4],
    ["which language is used to make facebook:","python","JAVA","C++","None", 4],
    ["which language is used to make facebook:","python","JAVA","C++","None", 4],
    ["which language is used to make facebook:","python","JAVA","C++","None",4]
    ]

level = [1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    
    print(f"\n\n question for Rs. {level[i]}")
    print(f"a. {question[1]}                b. {question[2]}")
    print(f"a. {question[3]}                b. {question[4]}")

    reply = int(input("Enter your answer (1-4): "))
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {level[i]}")
    else:
        print(f"wrong answer")

        if(i == 4):
            money = 10000

        elif(i == 9):
            money = 32000

        elif(i == 14):
            money = 100000

        else:
            print("wrong answer!")

            break
print(f"your take home money is {money}")

