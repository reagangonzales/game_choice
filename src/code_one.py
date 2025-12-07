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
    
    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)
    
    def filter_games(self, user_profile):
        filtered = []
        for game in self.games:
            # Genre check (matches at least one)
            genre_ok = any(g in user_profile.preferred_genres for g in game.genre)
            # Length check
            length_ok = (
                user_profile.max_game_length is None or
                game.length_hours <= user_profile.max_game_length)
            # Skill level check
            skill_ok = (
                user_profile.skill_level is None or
                game.difficulty.lower() == user_profile.skill_level.lower())
            # Platform check
            platform_ok = any(p in user_profile.platforms for p in game.platforms)
            # Multiplayer check
            mp_ok = (
                user_profile.multiplayer_preference is None or
                game.multiplayer == user_profile.multiplayer_preference)
            # Only add if ALL criteria are satisfied
            if genre_ok and length_ok and skill_ok and platform_ok and mp_ok:
                filtered.append(game)
        if not filtered:
            print("No games match your filters.\n")
        else:
            print("Filtered Games:")
            for game in filtered:
                print(f"- {game.name}")

    print("\nTo view more details about a game, call:")
    print("    game.display_info()")
    
    def rank_games(self, user_profile):
        ranked = []

        for game in self.games:
            score = 0
            # Genre match
            for g in game.genre:
                if g in user_profile.preferred_genres:
                    score += 2
            # Length match
            if (user_profile.max_game_length is None) or (game.length_hours <= user_profile.max_game_length):
                score += 1
            # Platform match
            for p in game.platforms:
                if p in user_profile.platforms:
                    score += 1
            # Multiplayer match
            if game.multiplayer == user_profile.multiplayer_preference:
                score += 1

            ranked.append((score, game))
        # Sort by descending score
        ranked.sort(reverse=True)
        for score, game in ranked:
            print(f"- {game.name}: {score} points matched")
        print("\nTo view more details about a game, call:")
        print("    game.display_info()")