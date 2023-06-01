import random

print("Rock...".lower())
print("Paper...".lower()) 
print("Scissors...".lower())

print("------------------")

randomNumber = random.randint(0,2)



if randomNumber == 0 :
    computerMove = "Rock"

elif randomNumber == 1 :
    computerMove = "Paper"

else :
    computerMove = "Scissors"




#------------------------------------------------------------------------------
#you can use this code

""" if Player_1 == "Rock" and Player_2 == "Scissors" :
        print("Player_1 wins ...")
        Player1_wins +=1

    elif Player_1 == "Rock" and Player_2 == "Paper" :
        print("Player_2 wins ...")
        Player2_wins+=1 """

#insted of  :
"""
if Palyer_1 == "rock" :
    if Player == "Scissors"
        print("Player_1 wins ...")
    elif :
        print("Player_2 wins ...")
elif Player_1 == "Paper" ...

"""

#------------------------------------------------------------------------------
#Or use this 
""" if Player_1 == "rock" :
      print("Player_1 wins ...")  if Player_2 == "Scissors"  else  print("Player_2 wins ...")   """  

      #But i dont advice this  code for you !

#------------------------------------------------------------------------------

Player1_wins = 0 
Player2_wins = 0 

wining_score = 2

while Player1_wins <= wining_score and Player2_wins <= wining_score :

    print(f"Player1_score : {Player1_wins} \t Player2_score : {Player2_wins}")

    Player_1 = input("Player_1 ! Make your move : ")

#Player_2 = input("Player_2 ! Make your move :  ")

    print(f" computer Make your move : {computerMove} ")
    
#play whit computer
    Player_2 = computerMove

    


    if Player_1 == "Rock" and Player_2 == "Scissors" :
        print("Player_1 wins ...")
        Player1_wins +=1

    elif Player_1 == "Rock" and Player_2 == "Paper" :
        print("Player_2 wins ...")
        Player2_wins+=1

    elif Player_1 == "Paper" and Player_2 == "Rock":
        print("Player_1 wins ...")
        Player1_wins +=1

    elif Player_1 == "Paper" and Player_2 == "Scissors":
        print("Player_2 wins ...")
        Player2_wins+=1

    elif Player_1 == "Scissors" and Player_2 == "Paper":
        print("Player_1 wins ...")
        Player1_wins +=1

    elif Player_1 == "Scissors" and Player_2 == "Rock":
        print("Player_2 wins ...")
        Player2_wins+=1



    elif Player_1 == Player_2 :
        print("Thats a tie ...")

    else :
        print("Somthing was wrong ...")


    


print(f"Player1_score : {Player1_wins} \t Player2_score : {Player2_wins}")


if Player1_wins > Player2_wins :

    print("\nPalyer_1 Winner Winner Chicken dinner \U0001F60D")

else :
    
    print("\nPalyer_2 Winner Winner Chicken dinner \U0001F60D")

