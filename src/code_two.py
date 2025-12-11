class UserProfile: 
    """
    A class representing a user's gaming preferences, used for filtering
    and ranking games in a GameLibrary.

    Attributes
    ----------
    preferred_genres : list[str]
        List of preferred game genres.
    max_game_length : int or float
        Maximum game length (hours) preferred by the user.
    skill_level : str
        User's preferred skill level ("Beginner", "Intermediate", "Advanced").
    platforms : list[str]
        List of preferred gaming platforms (e.g., ["PC", "Xbox"]).
    multiplayer_preference : bool
        Whether the user prefers multiplayer games (True/False).
    """
    def __init__(self, preferred_genres = None, max_game_length = None, skill_level = None, platforms = None, multiplayer_preference = None):
        """
        Initialize a UserProfile object.

        Parameters
        ----------
        preferred_genres : list[str], optional
            User's preferred game genres (default: empty list).
        max_game_length : int or float, optional
            Maximum playtime in hours preferred by the user.
        skill_level : str, optional
            Preferred difficulty level.
        platforms : list[str], optional
            Preferred platforms for gaming.
        multiplayer_preference : bool, optional
            Preference for multiplayer games.
        """
        self.preferred_genres = preferred_genres or []
        self.max_game_length = max_game_length
        self.skill_level = skill_level 
        self.platforms = platforms or []
        self.multiplayer_preference = multiplayer_preference 
        
    def update_preferences(self, preferred_genres = None, max_game_length = None, skill_level = None, platforms = None, multiplayer_preference = None):
        """
        Update one or more attributes of the user profile.

        Parameters
        ----------
        preferred_genres : list[str], optional
            New preferred genres.
        max_game_length : int or float, optional
            New maximum game length.
        skill_level : str, optional
            New skill level.
        platforms : list[str], optional
            New preferred platforms.
        multiplayer_preference : bool, optional
            New multiplayer preference.

        Returns
        -------
        None
        """
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
        """
        Print the current user preferences in a readable format.

        Returns
        -------
        None
        """
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
    """
    A class to generate game recommendations based on ranked scores.

    Attributes
    ----------
    ranked_games : list[tuple[int, Game]]
        List of tuples containing (score, Game) returned from GameLibrary.rank_games().
    top_games : list[Game]
        List of games that meet a minimum score threshold.
    """
    def __init__(self, ranked_games):
        """
        Initialize the RecommendationEngine with a list of ranked games.

        Parameters
        ----------
        ranked_games : list[tuple[int, Game]]
            Ranked list of games from GameLibrary.rank_games().
        """
        # ranked_games = [(score, game), (score, game), ...]
        self.ranked_games = ranked_games
        self.top_games = []
        
    def get_top_games(self, min_score=4):
        """
        Filter and return games with a score greater than or equal to min_score.

        Parameters
        ----------
        min_score : int, optional
            Minimum score to qualify as a top game (default is 4).

        Returns
        -------
        list[Game]
            List of Game objects meeting the score threshold.
        """
        self.top_games = []
        for score, game in self.ranked_games:
            if score >= min_score:
                self.top_games.append(game)
        return self.top_games
        
    def get_random_game(self):
         """
        Return a random game from the top-scoring games.

        Returns
        -------
        Game or None
            A randomly chosen Game object from top_games, or None if no top games exist.
        """
         if not self.top_games:
                return None
         return random.choice(self.top_games)
