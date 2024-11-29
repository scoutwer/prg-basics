computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

i = 0

computer_games = sorted(computer_games)

while i < len(computer_games):
    print(f"{i + 1}.{computer_games[i]}")
    i += 1


