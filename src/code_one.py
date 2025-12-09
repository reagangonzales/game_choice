class Game():
    """
    A class representing an individual video game with metadata used for
    filtering, ranking, and displaying information.

    Attributes
    ----------
    name : str
        The name of the game.
    genre : list[str]
        A list of genre tags associated with the game.
    length_hours : int or float
        Estimated number of hours required to complete or enjoy the game.
    difficulty : str
        The game's difficulty level (e.g. "Beginner", "Intermediate", "Advanced").
    platforms : list[str]
        A list of platforms the game is available on (e.g. ["PC", "Xbox"]).
    multiplayer : bool
        Whether or not the game includes multiplayer functionality.
    """
    def __init__(self,name,genre,length_hours, difficulty, platforms, multiplayer):
        """
        Initialize a Game object.

        Parameters
        ----------
        name : str
            The title of the game.
        genre : list[str]
            One or more genre labels describing the game.
        length_hours : int or float
            Estimated playtime in hours.
        difficulty : str
            Difficulty rating ("Beginner", "Intermediate", "Advanced").
        platforms : list[str]
            Supported platforms for the game.
        multiplayer : bool
            Indicates whether the game offers multiplayer features.
        """
        self.name = name
        self.genre = genre
        self.length_hours = length_hours
        self.difficulty = difficulty
        self.platforms = platforms
        self.multiplayer = multiplayer
        
    # Printing methods to better output a game
    def __str__(self):
        """
        Return a readable string representation of the game.

        Returns
        -------
        str
            A formatted string with the game's name and genres.
        """
        return f"{self.name} ({', '.join(self.genre)})"
        
    def __repr__(self):
        """
        Return a representation suitable for debugging or lists.

        Returns
        -------
        str
            Same formatted output as __str__.
        """
        return self.__str__()
        
    def display_info(self):
        """
        Print formatted information about the game.

        Returns
        -------
        None
        """
        print(f"""Game Information: {self.name}
                  Genre(s): {self.genre}
                  Length: {self.length_hours} hour(s)
                  Difficulty: {self.difficulty}
                  Platforms: {self.platforms}
                  Multiplayer: {self.multiplayer}""")
        
class GameLibrary():
    """
    A class representing a collection of Game objects. Supports adding,
    removing, filtering, and ranking games based on a UserProfile.

    Attributes
    ----------
    games : list[Game]
        A list storing all Game objects in the library.
    """
    
    def __init__(self):
        """
        Initialize an empty GameLibrary.

        Returns
        -------
        None
        """
        self.games = []
        
    def display_info(self):
        """
        Print detailed information for all games currently in the library.

        Returns
        -------
        None
        """
        if not self.games:
            print("No games in the library.")
        else:
          for game in self.games:
            game.display_info()
              
    def add_game(self, game):
        """
        Add a Game object to the library.

        Parameters
        ----------
        game : Game
            The game to be added.

        Returns
        -------
        None
        """
        self.games.append(game)
        
    def remove_game(self, game_or_name):
        """
        Remove a game from the library, based on either the Game object
        or the game's name.

        Parameters
        ----------
        game_or_name : Game or str
            The game to remove, provided either as a Game instance or
            a string containing the game's name.

        Raises
        ------
        ValueError
            If the argument is neither a Game object nor a string.

        Returns
        -------
        None
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
        """
        Filter the library's games based on a UserProfile and various
        optional filter criteria.

        Parameters
        ----------
        user_profile : UserProfile
            The user profile containing preferences used for filtering.
        filter_genre : bool, optional
            Whether to filter based on genre match. Default is True.
        filter_length : bool, optional
            Whether to filter based on maximum length. Default is True.
        filter_skill : bool, optional
            Whether to filter based on difficulty. Default is True.
        filter_platform : bool, optional
            Whether to filter based on platform availability. Default is True.
        filter_multiplayer : bool, optional
            Whether to filter based on multiplayer preference. Default is True.

        Returns
        -------
        list[Game]
            A list of games that meet the filter criteria.

        Notes
        -----
        Games are sorted alphabetically by default via built-in sorting.
        """
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
        """
        Assign a match score to each game based on how well it matches
        the user's preferences, then rank all games accordingly.

        Scoring System
        --------------
        +2 per matching genre  
        +1 if game length is within user's max length  
        +1 per matching platform  
        +2 if multiplayer preference matches  
        +2 if difficulty matches  

        Parameters
        ----------
        user_profile : UserProfile
            The profile whose preferences determine the scoring.

        Returns
        -------
        list[tuple[int, Game]]
            A list of tuples containing (score, Game), sorted by score
            in descending order.
        """
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
