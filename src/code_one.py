class Game():
    def __init__(self,name,genre,length_hours, difficulty, platforms, multiplayer):
        self.name = name
        self.genre = genre
        self.length_hours = length_hours
        self.difficulty = difficulty
        self.platforms = platforms
        self.multiplayer = multiplayer
    # Printing methods to better output a game
    def __str__(self):
        return f"{self.name} ({', '.join(self.genre)})"
    def __repr__(self):
        return self.__str__()
    def display_info(self):
        print(f"""Game Information: {self.name}
                  Genre(s): {self.genre}
                  Length: {self.length_hours} hour(s)
                  Difficulty: {self.difficulty}
                  Platforms: {self.platforms}
                  Multiplayer: {self.multiplayer}""")
        
class GameLibrary():
    def __init__(self):
        self.games = []
    def display_info(self):
        if not self.games:
            print("No games in the library.")
        else:
          for game in self.games:
            game.display_info()
    def add_game(self, game):
        self.games.append(game)
    def remove_game(self, game_or_name):
        """
        Removes a game from the library.
        Can accept either a Game object or a string (game name).
        """
        if isinstance(game_or_name, Game):
            # Remove by matching Game object attributes
            self.games = [g for g in self.games if g.name != game_or_name.name]
        elif isinstance(game_or_name, str):
            # Remove by name
            self.games = [g for g in self.games if g.name != game_or_name]
        else:
            raise ValueError("Argument must be a Game object or a string (game name).")
    def filter_games(self, user_profile,
                     filter_genre=True,
                     filter_length=True,
                     filter_skill=True,
                     filter_platform=True,
                     filter_multiplayer=True):
        filtered = []
        for game in self.games:
            # Genre check
            if filter_genre and user_profile.preferred_genres:
                if not any(g in user_profile.preferred_genres for g in game.genre):
                    continue
            # Length check
            if filter_length and user_profile.max_game_length is not None:
                if game.length_hours > user_profile.max_game_length:
                    continue
            # Skill check
            if filter_skill and user_profile.skill_level:
                if game.difficulty.lower() != user_profile.skill_level.lower():
                    continue
            # Platform check
            if filter_platform and user_profile.platforms:
                if not any(p in user_profile.platforms for p in game.platforms):
                    continue
            # Multiplayer check
            if filter_multiplayer and user_profile.multiplayer_preference is not None:
                if game.multiplayer != user_profile.multiplayer_preference:
                    continue
            filtered.append(game)
        # Sort filtered
        filtered.sort()
        # Print Results
        if filtered:
            for game in filtered:
                game.display_info()
        else:
            print("No games matched your filters.")

        print("To view more details about a specific game, call game.display_info()")
        # Return for testing
        return filtered
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
                score += 2
            # Difficulty match
            if game.difficulty == user_profile.skill_level:
                score += 2
            ranked.append((score, game))
        # Sort by descending score
        ranked.sort(key=lambda x: x[0], reverse=True)
        # Print results
        for score, game in ranked:
            print(f"{game.name}: {score} points matched")
        
        print("To view more details about any game, call game.display_info()")
        # Return list for testing
        return ranked
