from ..code_one import GameLibrary, Game
from ..code_two import UserProfile, RecommendationEngine 

#Test UserProfile class 
def test_user_initialization_defaults():
    user = UserProfile()

    assert user.preferred_genres == [] 
    assert user.max_game_length is None
    assert user.skill_level is None
    assert user.platforms == []
    assert user.multiplayer_preference is None

def test_user_initialization():
    user = UserProfile(
        preferred_genres=["Simulation"], 
        max_game_length=40, 
        skill_level="Advanced", 
        platforms=["PS"], 
        multiplayer_preference=True
    )
    
    assert user.preferred_genres == ["Simulation"]
    assert user.max_game_length == 40 
    assert user.skill_level == "Advanced"
    assert user.platforms == ["PS"]
    assert user.multiplayer_preference is True 


def test_update_preferences():
    user = UserProfile() 

    user.update_preferences(
        preferred_genres=["RPG"], 
        max_game_length=80, 
        skill_level="Intermediate", 
        platforms=["PC"], 
        multiplayer_preference=False
    )

    assert user.preferred_genres == ["RPG"]
    assert user.max_game_length == 80
    assert user.skill_level == "Intermediate"
    assert user.platforms == ["PC"]
    assert user.multiplayer_preference is False


#Test RecommendationEngine class 
def test_recommendation_initialization(): 
    """Making sure the ranked games are stored correctly"""

    ranked_games = [
        (3, Game("God of War", ["Action"], 25, "Intermediate", ["PlayStation"], False)), 
        (5, Game("Apex", ["Shooter"], 10, "Advanced", ["PC"], True)), 
        (7, Game("Minecraft", ["Simulation"], 80, "Beginnger", ["PC"], True))
    ]
    engine = RecommendationEngine(ranked_games)

    assert engine.ranked_games == ranked_games
    assert engine.top_games == []

def test_get_top_games():
    ranked_games = [
        (3, Game("God of War", ["Action"], 25, "Intermediate", ["PlayStation"], False)), 
        (5, Game("Apex", ["Shooter"], 10, "Advanced", ["PC"], True)), 
        (7, Game("Minecraft", ["Simulation"], 80, "Beginnger", ["PC"], True))
    ]

    engine = RecommendationEngine(ranked_games)

    top_games = engine.get_top_games(min_score = 4)

    names = [g.name for g in top_games]

    assert "Minecraft" in names
    assert "Apex" in names     
    assert "God of War" not in names
    assert len(top_games) == 2

def test_get_random_game():
    ranked_games = [
        (3, Game("God of War", ["Action"], 25, "Intermediate", ["PlayStation"], False)), 
        (5, Game("Apex", ["Shooter"], 10, "Advanced", ["PC"], True)), 
        (7, Game("Minecraft", ["Simulation"], 80, "Beginnger", ["PC"], True))
    ]

    engine = RecommendationEngine(ranked_games)

    engine.get_top_games()

    random_game = engine.get_random_game()

    assert random_game in engine.top_games