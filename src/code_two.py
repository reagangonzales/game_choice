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