import pandas as pd
df = pd.read_csv("full_steam_api.csv")
game_detail = df[df["Game_id"]==570]
print(game_detail["Image_Link"])