import random

#choosing random words
def choose():
    words=["condition","player","hello","water","science","mathematics","board","program","reverse","computer","keyboard"]
    pick=random.choice(words)
    return pick

#jumbling
def jumble(word):
    jumbled="".join(random.sample(word,len(word))) #join use to terminate spaces #sample is used to jumble words # to remove commas and all
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"your score is = ",p1)
    print(p2n,"your score is = ",p2)
    print("thanks for playing")
    print("have a nice day")

#player plays
def play():
    p1name=input("player 1 enter your name = ")
    p2name=input("player 2 enter your name = ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_word=choose()
        #create the question
        qn=jumble(picked_word)
        print(qn)
        #player 1
        if turn%2==0:
            print(p1name,"your turn")
            ans=input("what is in my mind?")
            if ans==picked_word:
                pp1=pp1+1
                print("your score is = ",pp1)
            else:
                print("better luck next time the correct word is = ",picked_word )
                c=input("press 1 to continue and 0 to quit = ")
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
        #player 2
        else:
            print(p2name,"your turn")
            ans=input("what is in my mind?")
            if ans==picked_word:
                pp2=pp2+1
                print("your score is = ",pp2)
            else:
                print("better luck next time the correct word is = ",picked_word )
                c=input("press 1 to continue and 0 to quit = ")
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
            turn=turn+1
play()