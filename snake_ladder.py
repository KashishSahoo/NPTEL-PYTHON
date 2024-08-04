from PIL import Image
import random
end=100
def show_board():
    img=Image.open('snake_ladder.jpg')
    img.show()

def check_ladder(points):
    if points==7:
        print("Ladder")
        return 30
    elif points==16:
        print("Ladder")
        return 33
    elif points==20:
        print("Ladder")
        return 38
    elif points==36:
        print("Ladder")
        return 83
    elif points==50:
        print("Ladder")
        return 68
    elif points==63:
        print("Ladder")
        return 81
    elif points==71:
        print("Ladder")
        return 89
    elif points==86:
        print("Ladder")
        return 97
    else:
        return points
    
def check_snake(points):
    if points==25:
        print("Snake")
        return 3
    elif points==42:
        print("Snake")
        return 1
    elif points==56:
        print("Snake")
        return 48
    elif points==61:
        print("Snake")
        return 43
    elif points==92:
        print("Snake")
        return 67
    elif points==95:
        print("Snake")
        return 12
    elif points==98:
        print("Snake")
        return 80
    else:
        return points

def reached_end(points):
    if points==end:
        return True
    else:
        return False



def play():
    p1_name=input("Player 1:Enter Your Name=")
    p2_name=input("Player 2:Enter Your Name=")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            #Player 1 Turn
            print(p1_name,"Yours Turn")
            c=input("Press 1 To Continue And 0 To Quit.")
            if c==0:
                print(p1_name,"Scored",pp1)
                print(p2_name,"Scored",pp2)
                print("Quitting The Game And Thanks For Playing")
                break
            dice=random.randint(1,6)
            print("Dice Showed",dice)
            pp1=pp1+dice

            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)

            #Check If Player Goes Beyond Board
            if pp1>end:
                pp1=end
            print(p1_name,"Your Score",pp1)
            print()

            if reached_end(pp1):
                print(p1_name,"Won")
                break

        else:
              #Player 2 Turn
            print(p2_name,"Yours Turn")
            c=input("Press 1 To Continue And 0 To Quit.")
            if c==0:
                print(p1_name,"Scored",pp1)
                print(p2_name,"Scored",pp2)
                print("Quitting The Game And Thanks For Playing")
                break
            dice=random.randint(1,6)
            print("Dice Showed",dice)
            pp2=pp2+dice

            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)

            #Check If Player Goes Beyond Board
            if pp2>end:
                pp2=end
            print(p2_name,"Your Score",pp2)
            print()

            if reached_end(pp2):
                print(p2_name,"Won")
                break
        turn=turn+1
show_board()
play()