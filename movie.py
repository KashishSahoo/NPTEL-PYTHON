import random

movies=["border","dangal","mary kom","neerja","dhoni","milkha","taare zameen par"]

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return(qn)


def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]=='' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if qn_list=="*":
                temp.append("*")
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new


def play():
    p1_name=input("Player1:Please Enter Your Name=")
    p2_name=input("Player2:Please Enter Your Name=")

    pp1=0
    pp2=0

    turn=0

    will=True
    while will:
        if(turn%2==0):
            #player1
            print(p1_name,"Your Turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            m_qn=qn

            not_said=True
            while not_said:
                letter=input("Your Letter=")

                if(is_present(letter,picked_movie)):
                    m_qn=unlock(m_qn,picked_movie,letter)
                    print(m_qn)
                    d=int(input("Press 1 To Guess The Movie or 2 To Unlock Another Letter="))
                    if d==1:
                        ans=input("Your Answer=")
                        if (ans==picked_movie):
                            pp1=pp1+1
                            print("Correct")
                            not_said=False
                            print(p1_name,"Your Score=",pp1)
                        else:
                            print("Wrong Answer,Try Again") 
                else:
                    print(letter,"not found")
            c=int(input("Please 1 To Continue or 0 to Quit="))
            if c==0:
                print(p1_name,"Your Score=",pp1)
                print(p2_name,"You Score=",pp2)
                print("Thank You For Playing")
                print("Have A Nice Day")
                will=False
            
        
        else:
            print("Player2")
             #player2
            print(p2_name,"Your Turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            m_qn=qn

            not_said=True
            while not_said:
                letter=input("Your Letter=")

                if(is_present(letter,picked_movie)):
                    m_qn=unlock(m_qn,picked_movie,ch)
                    print(m_qn)
                    d=int(input("Press 1 To Guess The Movie or 2 To Unlock Another Letter="))
                    if d==1:
                        ans=input("Your Answer=")
                        if (ans==picked_movie):
                            pp2=pp2+1
                            print("Correct")
                            not_said=False
                            print(p2_name,"Your Score=",pp2)
                        else:
                            print("Wrong Answer,Try Again") 
                else:
                    print(letter,"not found")
            c=int(input("Please 1 To Continue or 0 to Quit="))
            if c==0:
                print(p1_name,"Your Score=",pp1)
                print(p2_name,"You Score=",pp2)
                print("Thank You For Playing")
                print("Have A Nice Day")
                will=False

        turn=turn+1
play()