# game_choice
Final project SDS 271 - python package created by Reagan Gonzales &amp; Itzel Aleman Flores

GameChoice is a simple recommendation system for video games. Users create a UserProfile with their preferred genres, difficulty level, platforms, and play style.
The package includes:

* A Game class

* A GameLibrary for storing, filtering, ranking games

* A RecommendationEngine for selecting top games or random suggestions

It can be used for:

* Small recommendation apps

* Learning OOP

* Personal game trackers

# Importing

To use this package, copy the repository onto your local device
Then open up the folder on your local device through the terminal, for example, for mac users:
```
cd game_choice
```

Then in Python,

```
from code_one import Game, GameLibrary
from code_two import UserProfile, RecommendationEngine
```
# Example Usage

1. First import the package
```
from code_one import Game, GameLibrary
from code_two import UserProfile, RecommendationEngine
```

2. Then create a user profile
```
profile = UserProfile(
    preferred_genres=["Action", "Simulation"],
    max_game_length=30,
    skill_level="Beginner",
    platforms=["PC", "Xbox"],
    multiplayer_preference=True
)

profile.display_preferences()
```

3. Create game library
```
library = GameLibrary()

library.add_game(Game("Minecraft", ["Simulation"], 60, "Beginner",
                       ["PC","Xbox"], True))

library.add_game(Game("Apex Legends", ["Shooter"], 30, "Advanced",
                       ["PC"], True))

library.add_game(Game("Stardew Valley", ["Simulation"], 50, 
                       "Beginner", ["PC"], False))

library.display_info()
```

4. Filtering
```
filtered = library.filter_games(profile, filter_length=False)
```

5. Ranking
```
ranked = library.rank_games(profile)
```

6. Recommenndation Engine
```
ranked = library.rank_games(profile)
```
