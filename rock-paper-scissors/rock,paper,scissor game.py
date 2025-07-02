import random
while True:
    choice= input("choose who you want to play with computer or player 2")
    if choice=="computer":
        choose=["rock","paper","scissor"]
        computer =random.choice(choose)
        player1=False
        while player1 not in choose:
            player1=input("choose rock,paper,scissor?:").lower()
        if player1==computer:
            print("computer:",computer)
            print("player:",player1)
            print("Tie!")
        elif player1=="rock":
            if computer=="paper":
                print("computer:",computer)
                print("player:",player1)
                print("you lose!")
            if computer=="scissor":
                print("computer:",computer)
                print("player:",player1)
                print("you win!")
                
        elif player1=="scissor":
            if computer=="rock":
                print("computer:",computer)
                print("player:",player1)
                print("you lose!")
            if computer=="paper":
                print("computer:",computer)
                print("player:",player1)
                print("you win!")            
                
        elif player1=="paper":
            if computer=="scissor":
                print("computer:",computer)
                print("player:",player1)
                print("you lose!")
            if computer=="rock":
                print("computer:",computer)
                print("player:",player1)
                print("you win!")
    elif choice=="player2":
            player1=input("player 1 please choose (rock,paper,scissor):").lower()
            player2=input("player 2 please choose (rock,paper,scissor):").lower()
            if player1==player2:
                print("player1:",player1)
                print("player2:",player2)
                print("Tie!")
            elif player1=="rock":
                if player2=="paper":
                    print("player1:",player1)
                    print("player2:",player2)
                    print("player2 wins!")
                if player2=="scissor":
                    print("player1:",player1)
                    print("player2:",player2)
                    print("player1 wins")
            elif player1=="scissor":
                if player2=="rock":
                    print("player1:",player1)
                    print("player2:",player2)
                    print("player2 wins")
                if player2=="paper":
                    print("player1:",player1)
                    print("player2:",player2)
                    print("player1 wins!")            
            elif player1=="paper":
                if player2=="scissor":
                    print("player1:",player1)
                    print("player2:",player2)
                    print("player2 wins")
                if player2=="rock":
                    print("player1:",player1)
                    print("player2:",player2)
                    print("player1 wins")
    play_again=input("do you want to play again? (Yes/No)")
    if play_again !="yes":
        break
    
print("Bye")
