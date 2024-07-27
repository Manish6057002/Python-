#rock , paper and scissor game
import random
x = ["rock", "paper", "scissor"]
p = input("Choose: rock, paper, or scissor:")
c = random.choice(x)
print("player choose:",p)
print("computer choose:", c)
if p==c:
    print("Match Tie")
elif p=="rock" and c =="paper":
    print("Computer wins")
elif p=="rock" and c=="scissor":
    print("Player wins")
elif p=="paper" and c=="rock":
    print("player wins")
elif p=="paper" and c=="scissor":
    print("computer wins")
elif p=="scissor" and c=="paper":
    print("player wins")
elif p=="scissor" and c=="rock":
    print("computer wins")
else:
    print("Invalid move")
