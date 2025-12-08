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
           print(f"Your current preferred maximum game length: {self.max_game_length} hour(s)"),
           print(f"Your current preferred skill level (Beginner, Intermediate, Advanced): {self.skill_level}"), 
           print(f"Your current preferred gaming platforms: {self.platforms}"), 
           print(f"Your current preferred multiplayer condition (True,False): {self.multiplayer_preference}")
        }
       return preferences

import random
class RecommendationEngine:
    def __init__(self, ranked_games):
        # ranked_games = [(score, game), (score, game), ...]
        self.ranked_games = ranked_games
        self.top_games = []
    def get_top_games(self, min_score=4):
        """Return games where score >= min_score."""
        self.top_games = []
        for score, game in self.ranked_games:
            if score >= min_score:
                self.top_games.append(game)
        return self.top_games
    def get_random_game(self):
        """Return a random game from top-scoring games."""
        if not self.top_games:
            return None
        return random.choice(self.top_games)
