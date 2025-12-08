from code_one import Game, GameLibrary
from code_two import UserProfile, RecommendationEngine

# -----------------------------------------------
# UserProfile Class
# 1. Create UserProfile
profile = UserProfile(
    preferred_genres=["FPS","Action"],
    max_game_length=30,
    skill_level="Beginner",
    platforms=["PC","Xbox"],
    multiplayer_preference=True
)
# UserProfile Methods
profile.display_preferences()
profile.update_preferences(max_game_length=40)
# ------------------------------------------------
# Game + GameLibrary
library = GameLibrary()
# One way to add games
apex_legends = Game("Apex Legends", ["Shooter"], 30, "Advanced", ["PC"], True)
library.add_game(apex_legends)
# Other way to add games
library.add_game(Game("God of War", ["Action"], 25, "Intermediate", ["PlayStation"], False))
library.add_game(Game("Stardew Valley", ["Simulation"], 50, "Beginner", ["PC"], False))
## Way one allows for this
# Game class method
apex_legends.display_info()
# Remove games - lets switch out a game
library.remove_game(Game("Stardew Valley", ["Simulation"], 50, "Beginner", ["PC"], False))
library.add_game(Game("Minecraft", ["Simulation"], 60,"Beginner",["PC","Xbox","PlayStation"], True))
# Filter games
filtered = library.filter_games(profile)
# Rank games
ranked = library.rank_games(profile)
# -----------------------------------------------
# Recommendation Engine









