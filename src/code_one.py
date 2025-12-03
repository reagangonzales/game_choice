class Game():
    def __init__(self,name,genre,length_hours, difficulty, platforms, multiplayer):
        self.name = name
        self.genre = genre
        self.length_hours = length_hours
        self.difficulty = difficulty
        self.platforms = platforms
        self.multiplayer = multiplayer
        
    def display_info(self):
        print(f"""Game Information:
              Title: {self.name}
              Genre(s): {self.genre}
              Length: {self.length_hours} hour(s)
              Difficulty: {self.difficulty}
              Platforms: {self.platforms}
              Multiplayer: {self.multiplayer}""")
        
class GameLibrary():
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)
        return self.games
    
    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)
        return self.games
    
    def filter_games(self, user_profile):
        filtered = []
        for game in self.games:
            # Matches preferred genres
            genre_match = any(g in user_profile.preferred_genres for g in game.genre)
            # Matches length
            length_match = game.length_hours <= user_profile.max_game_length
            # Matches platform
            platform_match = any(p in user_profile.platforms for p in game.platforms)
            # Matches multiplayer
            mp_match = (game.multiplayer == user_profile.multiplayer_preference)
            if genre_match and length_match and platform_match and mp_match:
                filtered.append(game)
            return filtered
    
    def rank_games(self, user_profile):
        pass


