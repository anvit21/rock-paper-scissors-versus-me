import random as rd

player_wins = 0
anvit_wins = 0
draws = 0


def counter(): 
    print("\n" + "=" * 25)
    print("         SCORE")
    print("=" * 25)
    print(f"Player wins : {player_wins}")
    print(f"Anvit wins  : {anvit_wins}")
    print(f"Draws       : {draws}")
    print("=" * 25)

def play_again():
    a = input("\n🔄 Think you can beat me again? (yes/no): ").lower()
    if a in ["yes", "y", "yup"]:
        print("\n👀 oh you're brave...\n")
        rocksciss()
    elif a in ["no", "nope", "nah"]:
        print("\n😂 smart choice. nobody beats Anvit.\n")
    else:
        print("\n🤷 didn't get that, but i'll take it as a no~\n")

def rocksciss():
    global player_wins , anvit_wins ,draws
    w = ["rock", "paper", "scissors"]

    print("=" * 40)
    print("   🎮 ROCK PAPER SCISSORS vs ANVIT 🎮")
    print("=" * 40)

    player = input("\n✊ Your move (rock / paper / scissors): ").lower().strip()

    if player not in w:
        print("\n❌ bro that's not even a valid move~")
        play_again()
        return

    anvit = rd.choice(w)

    print(f"\n⚡ You threw:    {player.upper()}")
    print(f"🤖 Anvit threw:  {anvit.upper()}\n")

    if player == anvit:
        draws += 1
        print("🤝 a draw? i'll let you have that~")
        

    elif (player == "rock" and anvit == "scissors") or \
         (player == "scissors" and anvit == "paper") or \
         (player == "paper" and anvit == "rock"):
        player_wins += 1
        print("😤 okay fine, you got lucky this time~")
        

    else:
        anvit_wins += 1
        print("😎 lmao you thought~ nobody beats me.")
        

    counter()

    play_again()


rocksciss()