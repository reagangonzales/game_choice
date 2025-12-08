from code_one import Game, GameLibrary
from code_two import UserProfile, RecommendationEngine

# -----------------------------------------------
# UserProfile Class
# 1. Create UserProfile
profile = UserProfile(
    preferred_genres=["FPS","Action", "Simulation"],
    max_game_length=30,
    skill_level="Beginner",
    platforms=["PC","Xbox"],
    multiplayer_preference=True
)
# UserProfile Methods
print("------------------------------")
print("Display Preferences")
profile.display_preferences()
print("------------------------------")
print("Update Preferences")
profile.update_preferences(max_game_length=40)
profile.display_preferences()
# ------------------------------------------------
# Game + GameLibrary
library = GameLibrary()
# One way to add games
apex_legends = Game("Apex Legends", ["Shooter"], 30, "Advanced", ["PC"], True)
library.add_game(apex_legends)
# Other way to add games
library.add_game(Game("God of War", ["Action"], 25, "Intermediate", ["PlayStation"], False))
library.add_game(Game("Stardew Valley", ["Simulation"], 50, "Beginner", ["PC"], False))
print("------------------------------")
print("Display Game Library Method")
library.display_info()
## Way one allows for this
# Game class method
print("------------------------------")
print("Game Display Method")
apex_legends.display_info()
# Remove games - lets switch out a game
print("------------------------------")
print("Remove and add to Game Library")
library.remove_game("Stardew Valley")
# library.remove_game(Game("Stardew Valley", ["Simulation"], 50, "Beginner", ["PC"], False))
library.add_game(Game("Minecraft", ["Simulation"], 60,"Beginner",["PC","Xbox","PlayStation"], True))
library.display_info()
# Filter games
print("------------------------------")
print("Filtering Game Library - perfect match ignoring game length")
filtered = library.filter_games(profile, filter_length=False)
# Rank games
print("------------------------------")
print("Ranking Game Library by my user profile")
ranked = library.rank_games(profile)
# -----------------------------------------------
# Recommendation Engine
engine = RecommendationEngine(ranked)
top_games = engine.get_top_games(min_score=4)
print(top_games)
random_pick = engine.get_random_game()
print("Random recommended game:", random_pick.name)
