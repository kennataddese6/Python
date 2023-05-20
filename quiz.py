questions = {"What day is today?" : "B",
             "What is capital of Ethiopia" : "A",
             "When was the revolution" : "C",
             "Who is the new oscar winner" : "D"
             }

twoarray = [
    ["A : Monday ","B : Tuesday","C : Wensday","D : Friday"] ,
    ["A : Addis Ababa ","B : Mombasa","C : Cairo","D : Johannesberg"] ,
    ["A : 1998 ","B : 2007","C : 1549","D :1326"],
    ["A : Jim Carey ","B : Brad Pit","C : Jennifer Ani","D : Tom Cruise"]
]
while True:
    row = -1
    result = 0
    for key, value in questions.items():
        print("-------")
        print(key)
        answers=value
        row += 1
        for coloumn in range(0,4):
            print(twoarray[row][coloumn],end=" ")
        print("")
        answer = input("Answer : ").upper()
        if answer == answers:
            result += 1
        #print(result)
    print("You have scored " + str(result*25) + "%")

    playagain = input("Do you want to play again?(yes/no) : ").lower()
    if playagain != "yes":
        break







