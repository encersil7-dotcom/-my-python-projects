import random

print("🎮 Rock Paper Scissors Game!")
print("--------------------------------")

while True:
    player = input("ရွေးပါ (rock / paper / scissors) သို့မဟုတ် quit: ")
    
    if player == "quit":
        print("ကစားပေးတဲ့အတွက် ကျေးဇူးတင်တယ်!")
        break
    
    if player not in ["rock", "paper", "scissors"]:
        print("rock, paper, သို့မဟုတ် scissors သာ ရိုက်ပါ!")
        continue
    
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer ရွေးတာ: {computer}")
    
    if player == computer:
        print("🤝 သရေ!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("🎉 သင်နိုင်တယ်!")
    else:
        print("😢 Computer နိုင်တယ်!")
    
    print("--------------------------------")