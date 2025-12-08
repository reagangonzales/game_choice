class UserProfile: 
    def __init__(self, preferred_genres = None, max_game_length = None, skill_level = None, platforms = None, multiplayer_preference = None):
        self.preferred_genres = preferred_genres or []
        self.max_game_length = max_game_length
        self.skill_level = skill_level 
        self.platforms = platforms or []
        self.multiplayer_preference = multiplayer_preference 
    def update_preferences(self, preferred_genres = None, max_game_length = None, skill_level = None, platforms = None, multiplayer_preference = None):
        if preferred_genres is not None: 
            self.preferred_genres = preferred_genres
        if max_game_length is not None: 
            self.max_game_length = max_game_length
        if skill_level is not None: 
            self.skill_level = skill_level
        if platforms is not None: 
            self.platforms = platforms
        if multiplayer_preference is not None: 
            self.multiplayer_preference = multiplayer_preference
    def display_preferences(self):
       preferences = {
           print(f"Your current preferred genres: {self.preferred_genres}"),
           print(f"Your current preferred maximum game length (in minutes): {self.max_game_length}"),
           print(f"Your current preferred skill level (beginner, intermediate, advanced): {self.skill_level}"), 
           print(f"Your current preferred gaming platforms: {self.platforms}"), 
           print(f"Your current preferred multiplayer condition (yes/no): {self.multiplayer_preference}")
        }
       return preferences
    

import random

class RecommendationEngine: 
    def __init__(self, rank_games):
        self.rank_games = rank_games
        self.top_games = []

    def get_top_games(self, rank_games):
        for games in rank_games: 
            if rank_games.score >= 4:
                self.top_games = self.top_games.append(games) 
            if rank_games.score < 4:
                return None
        return self.top_games 
    
    def get_random_game(games, top_games):
        random_game = random.choice(top_games)
        return random_game